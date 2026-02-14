import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import psutil
import smtplib
from email.message import EmailMessage


def make_zip(folder, log_file):
    timestamp = time.strftime("%Y-%m%d_%H-%M-%S")
    zip_name = folder + "-" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)
            zobj.write(full_path, relative)

    zobj.close()

    log_file.write(f"Zip file created : {zip_name}\n")

    return zip_name


def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


def BackupFiles(Source, Destination, log_file):
    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            if file.endswith((".tmp", ".log", ".exe")):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if ((not os.path.exists(dest_path)) or
                (calculate_hash(src_path) != calculate_hash(dest_path))):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
                log_file.write(f"Copied : {relative}\n")

    return copied_files


def update_history(file_count, zip_name):
    with open("backup_history.txt", "a") as f:
        f.write(f"Date : {time.ctime()}\n")
        f.write(f"Files Copied : {file_count}\n")
        f.write(f"Zip Name : {zip_name}\n")
        f.write("-" * 40 + "\n")


def show_history():
    if os.path.exists("backup_history.txt"):
        with open("backup_history.txt", "r") as f:
            print(f.read())
    else:
        print("No backup history found.")


def restore_backup(zipfile_name, destination):
    if not os.path.exists(zipfile_name):
        print("Zip file not found!")
        return

    with zipfile.ZipFile(zipfile_name, 'r') as z:
        z.extractall(destination)

    print("Backup restored successfully.")


def send_email(log_filename, zip_name):

    sender = "bhosalet0520@gmail.com"
    password = "mmdh ipso fthc dfpd"
    receiver = "bhosale0520@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Backup Completed Successfully"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(f"Backup completed.\nZip File : {zip_name}")

    with open(log_filename, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(log_filename))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Email sending failed:", e)
    print("sends ......")

def CreateLogFolder():
    folder = "Log"
    os.makedirs(folder, exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"MarvellousBackup_{timestamp}.log")

    return open(filename, "w"), filename


def MarvellousDataShieldStart(Source="Data"):

    Border = "-" * 50
    BackupName = "MarvellousBackup"

    log_file, log_filename = CreateLogFolder()

    log_file.write(Border + "\n")
    log_file.write("Marvellous Data Shield System\n")
    log_file.write("Backup started at : " + time.ctime() + "\n")
    log_file.write(Border + "\n")

    log_file.write("\nSystem Usage Info\n")
    log_file.write(f"CPU Usage : {psutil.cpu_percent()} %\n")
    log_file.write(f"RAM Usage : {psutil.virtual_memory().percent} %\n")
    log_file.write(Border + "\n")

    files = BackupFiles(Source, BackupName, log_file)
    zip_file = make_zip(BackupName, log_file)

    log_file.write("Backup Completed Successfully\n")
    log_file.close()

    update_history(len(files), zip_file)
    send_email(log_filename, zip_file)


def main():

    Border = "-" * 50
    print(Border)
    print("---------- Marvellous Data Shield System ---------")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--H"):
            print("This script is used to : ")
            print("1 : Take automatic backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")
            print("4 : Show backup history")
            print("5 : Restore previous backup")

        elif sys.argv[1] in ("--u", "--U"):
            print("Use the automation script as:")
            print("Backup Scheduler : python script.py 5 SourceFolder")
            print("Restore Backup   : python script.py --restore zipfile destination")
            print("Show History     : python script.py --history")

        elif sys.argv[1] == "--history":
            show_history()

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif len(sys.argv) == 3:

        try:
            interval = int(sys.argv[1])
            source = sys.argv[2]

            print("Inside Project logic")
            print("Time interval :", interval)
            print("Directory name :", source)

            schedule.every(interval).minutes.do(MarvellousDataShieldStart, source)

            print(Border)
            print("Data Shield System started successfully")
            print("Time interval in minutes :", interval)
            print("Press Ctrl + C to stop the execution")
            print(Border)

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Time interval must be an integer.")

    elif len(sys.argv) == 4:

        if sys.argv[1] == "--restore":
            restore_backup(sys.argv[2], sys.argv[3])
        else:
            print("Invalid option for restore.")

    else:
        print("Invalid number of command line arguments")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()
