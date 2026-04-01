import ftplib

FTP_HOST = "ftpupload.net"
FTP_USER = "if0_41386054"
FTP_PASS = "1UhaKvJpQS"
FTP_DIR = "htdocs"

# Files and directories we want to keep
KEEP_FILES = ['index.html', 'facilities.html', 'academy.html', 'contact.html', 'files for your website should be uploaded here!']
KEEP_DIRS = ['assets']

def delete_dir(ftp, dir_name):
    try:
        ftp.cwd(dir_name)
    except ftplib.error_perm:
        return # Not a directory or doesn't exist

    files = ftp.nlst()
    for file in files:
        if file in ['.', '..']: continue
        try:
            ftp.delete(file)
            print(f"Deleted file {dir_name}/{file}")
        except ftplib.error_perm:
            delete_dir(ftp, file)

    ftp.cwd('..')
    try:
        ftp.rmd(dir_name)
        print(f"Deleted directory {dir_name}")
    except ftplib.error_perm as e:
        print(f"Error deleting directory {dir_name}: {e}")

try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.cwd(FTP_DIR)

    files = ftp.nlst()

    for file in files:
        if file in ['.', '..']:
            continue
        if file not in KEEP_FILES and file not in KEEP_DIRS:
            try:
                # Try to delete as a file
                ftp.delete(file)
                print(f"Deleted file {file}")
            except ftplib.error_perm:
                # If it fails, try deleting as a directory
                print(f"{file} might be a directory, attempting to delete...")
                delete_dir(ftp, file)

    ftp.quit()
    print("Cleanup complete.")
except Exception as e:
    print(f"FTP error occurred: {e}")
