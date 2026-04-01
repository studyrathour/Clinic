import ftplib
FTP_HOST = "ftpupload.net"
FTP_USER = "if0_41386054"
FTP_PASS = "1UhaKvJpQS"
FTP_DIR = "htdocs"

try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    print("Connected successfully.")

    ftp.cwd(FTP_DIR)
    print("Listing files in htdocs:")
    ftp.retrlines('LIST')
    ftp.quit()
except Exception as e:
    print(f"FTP error occurred: {e}")
