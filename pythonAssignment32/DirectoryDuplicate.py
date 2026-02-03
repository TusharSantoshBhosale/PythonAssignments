import sys
import os
import CheckSumModule

def DirectoryDuplicateFiles(DirName):
    duplicate = {}
    log = open("DirectoryDuplicateLog.log","w")

    if not os.path.isdir(DirName):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    if not os.path.exists(DirName):
        log.write("There is no such Directory... \n")
        log.close()
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Ret = CheckSumModule.CheckSumNumber(fname)

            if(Ret in duplicate):
                log.write("Duplicate file: " + fname + "\n")
            else:
                duplicate[Ret] = fname
                
                

def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicate.py DirectoryName")
        return
    DirectoryDuplicateFiles(sys.argv[1])

if __name__ == "__main__":
    main()