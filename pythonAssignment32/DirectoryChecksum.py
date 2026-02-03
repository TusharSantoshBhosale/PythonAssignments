import sys
import os
import CheckSumModule

def DirectoryCheckSum(DirName):

    log = open("DirectoryChecksum.log","w")
    
    if not os.path.isdir(DirName):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)
            CheckSum = CheckSumModule.CheckSumNumber(fName)
            print(f"Checksum of {fName} is : {CheckSum}")

def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryChecksum.py DirectoryName")
        return
    DirectoryCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()