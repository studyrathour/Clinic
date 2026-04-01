import ftplib
import os

FTP_HOST = "ftpupload.net"
FTP_USER = "if0_41386054"
FTP_PASS = "1UhaKvJpQS"
FTP_DIR = "htdocs"
LOCAL_DIR = "/app/public"

def upload_dir(ftp, local_dir, remote_dir):
    try:
        ftp.cwd(remote_dir)
        print(f"Changed to remote directory: {remote_dir}")
    except ftplib.error_perm:
        try:
            ftp.mkd(remote_dir)
            ftp.cwd(remote_dir)
            print(f"Created and changed to remote directory: {remote_dir}")
        except ftplib.error_perm as e:
            print(f"Error creating directory {remote_dir}: {e}")
            return

    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                print(f"Uploading file: {item} to {remote_dir}")
                try:
                    ftp.storbinary(f'STOR {item}', f)
                except Exception as e:
                    print(f"Failed to upload {item}: {e}")
        elif os.path.isdir(local_path):
            upload_dir(ftp, local_path, item)
            ftp.cwd("..")

def main():
    print(f"Connecting to FTP server {FTP_HOST}...")
    try:
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        print("Connected successfully.")

        # Verify if htdocs exists
        try:
            ftp.cwd(FTP_DIR)
            print(f"Changed to root directory: {FTP_DIR}")
        except ftplib.error_perm:
            print(f"Error: Could not change to directory {FTP_DIR}.")
            # Let's see what directories exist at root
            print("Current directories:", ftp.nlst())
            return

        print("Starting upload process...")
        # Since we are already in htdocs, we just upload the contents of LOCAL_DIR here
        for item in os.listdir(LOCAL_DIR):
            local_path = os.path.join(LOCAL_DIR, item)
            if os.path.isfile(local_path):
                with open(local_path, 'rb') as f:
                    print(f"Uploading root file: {item}")
                    ftp.storbinary(f'STOR {item}', f)
            elif os.path.isdir(local_path):
                upload_dir(ftp, local_path, item)
                ftp.cwd("..")

        print("Upload completed successfully.")
        ftp.quit()
    except Exception as e:
        print(f"FTP error occurred: {e}")

if __name__ == "__main__":
    main()
