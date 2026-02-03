import sys
import os
import CheckSumModule

def DeleteDuplicate(DirName):
    Duplicate = {}
    log = open("DirectoryDuplicateRemovalLog.log","w")

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
    DeleteDuplicate(sys.argv[1])
    
if __name__ == "__main__":
    main()