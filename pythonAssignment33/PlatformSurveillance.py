import sys
import os
import schedule
import time
import psutil
import smtplib
from email.message import EmailMessage


# -------------------- Sorting Functions --------------------

def SortByMemory(process):
    return process["memory_percent"]

def SortByCPU(process):
    return process["cpu"]

def SortByThreads(process):
    return process["threads"]

def SortByOpenFiles(process):
    if isinstance(process["open_files"], int):
        return process["open_files"]
    return 0


# -------------------- Process Scanner --------------------

def ProcessScan():
    process_list = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = {}

            info["name"] = proc.name()
            info["pid"] = proc.pid
            info["cpu"] = proc.cpu_percent()
            info["memory_percent"] = proc.memory_percent()

            memory = proc.memory_info()
            info["rss"] = memory.rss
            info["vms"] = memory.vms

            info["threads"] = proc.num_threads()

            try:
                info["open_files"] = len(proc.open_files())
            except:
                info["open_files"] = 0

            process_list.append(info)

        except:
            pass

    process_list = sorted(process_list, key=SortByMemory, reverse=True)

    return process_list[:10]


# -------------------- Summary Generator --------------------

def CreateSummary(processes):

    summary = "\nSystem Surveillance Summary\n"
    summary += "-" * 50 + "\n"
    summary += f"Total Processes : {len(processes)}\n\n"

    summary += "Top CPU Processes:\n"
    top_cpu = sorted(processes, key=SortByCPU, reverse=True)

    for p in top_cpu[:5]:
        summary += f"{p['name']} (PID {p['pid']}) - {p['cpu']:.2f}%\n"

    summary += "\nTop Memory Processes:\n"
    top_memory = sorted(processes, key=SortByMemory, reverse=True)

    for p in top_memory[:5]:
        summary += f"{p['name']} (PID {p['pid']}) - {p['memory_percent']:.2f}%\n"

    summary += "\nTop Thread Count Processes:\n"
    top_threads = sorted(processes, key=SortByThreads, reverse=True)

    for p in top_threads[:5]:
        summary += f"{p['name']} (PID {p['pid']}) - {p['threads']} threads\n"

    summary += "\nTop Open File Processes:\n"
    top_files = sorted(processes, key=SortByOpenFiles, reverse=True)

    for p in top_files[:5]:
        summary += f"{p['name']} (PID {p['pid']}) - {p['open_files']}\n"

    summary += "-" * 50 + "\n"

    return summary


# -------------------- Log File Creator --------------------

def createLog(FolderName):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(FolderName, f"LogFile_{timestamp}.log")

    processes = ProcessScan()

    with open(filename, "w") as f:

        f.write("Platform Surveillance System Log\n")
        f.write("Created At : " + time.ctime() + "\n")
        f.write("-" * 50 + "\n\n")

        for proc in processes:
            f.write(f"Process Name      : {proc['name']}\n")
            f.write(f"PID               : {proc['pid']}\n")
            f.write(f"CPU %             : {proc['cpu']:.2f}\n")
            f.write(f"Memory (RSS)      : {proc['rss']} bytes\n")
            f.write(f"Memory (VMS)      : {proc['vms']} bytes\n")
            f.write(f"Threads Count     : {proc['threads']}\n")
            f.write(f"Open Files Count  : {proc['open_files']}\n")
            f.write("-" * 50 + "\n")

        summary = CreateSummary(processes)
        f.write(summary)

    return filename, summary


# -------------------- Email Sender --------------------

def SendMail(receiver, logfile, summary):

    sender_email = "bhosalet0520@gmail.com"
    app_password = "mmdh ipso fthc dfpd"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver
    msg["Subject"] = "Platform Surveillance System Report"

    msg.set_content(summary)

    # Attach log file
    with open(logfile, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(logfile)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        print("Email Sent Successfully")

    except Exception as e:
        print("Error sending mail:", str(e))


# -------------------- Surveillance Task --------------------

def SurveillanceTask(FolderName, Receiver):

    logfile, summary = createLog(FolderName)
    SendMail(Receiver, logfile, summary)

    print("Log Created and Email Sent Successfully")

def main():

    Border = "-"*50
    print(Border)
    print("---------- Platform Surveillance System ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("1 : Scan running processes")
            print("2 : Generate log file of top resource consuming processes")
            print("3 : Send log file with summary via Email")
            print("4 : Perform periodic monitoring using scheduler")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print("ScriptName.py LogFolder ReceiverEmail TimeInterval")
            print("LogFolder     : Name of directory where log file will be created")
            print("ReceiverEmail : Email address to receive report")
            print("TimeInterval  : Time in minutes for periodic scheduling")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    elif(len(sys.argv) == 3):
        print("Error : Time interval argument is missing.")
        print("Correct usage :")
        print("ScriptName.py LogFolder ReceiverEmail TimeInterval")
        print("Example :")
        print("ScriptName.py Logs test@gmail.com 5")

    elif(len(sys.argv) == 4):
        print("Inside Projects logic")
        print("Log Folder     : ", sys.argv[1])
        print("Receiver Email : ", sys.argv[2])
        print("Time Interval  : ", sys.argv[3])
        
        #   Apply the schdular
        schedule.every(int(sys.argv[3])).minutes.do(SurveillanceTask, sys.argv[1], sys.argv[2])

        print(Border)
        print("Platform Surveillance System started successfully")
        print("Time interval in minutes : ", sys.argv[3])
        print("Press Ctrl + C to stop the execution")
        print(Border)


        #   Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

    
if __name__ == "__main__":
    main()