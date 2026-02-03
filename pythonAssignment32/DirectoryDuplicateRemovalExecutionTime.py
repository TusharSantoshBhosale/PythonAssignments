import sys
import os
import CheckSumModule
import time

def DeleteDuplicate(DirName):
    Duplicate = {}
    log = open("DirectoryDuplicateRemovalExicutionLog.log","w")

    if not os.path.exists(DirName):
        log.write("There is no such Directory... \n")
        log.close()
        return

    if not os.path.isdir(DirName):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Ret = CheckSumModule.CheckSumNumber(fname)

            if(Ret in Duplicate):
                os.remove(fname)
                log.write(fname + "\n")
            else:
                Duplicate[Ret] = fname

    log.close()
    
def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemoval.py DirectoryName")
        return
    start_time = time.time()
    DeleteDuplicate(sys.argv[1])
    end_time = time.time()

    print("Execution time:", end_time - start_time)

if __name__ == "__main__":
    main()