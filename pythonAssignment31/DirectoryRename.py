import sys
import os

def RenameFileExt(DirName,Ext,Doc):
    log = open("DirectoryRenameLogFile","w")

    if not os.path.isdir(DirName):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fName in FileName:
            if fName.endswith(Ext):
                oldFile = os.path.join(DirName,fName)
                newFile = os.path.join(DirName,fName.replace(Ext,Doc))
                os.rename(oldFile,newFile)
                log.write(fName + " File Renamed \n")
    log.close()

def main():
    
    if(len(sys.argv) != 4):
        print("Usage : DirectoryFileSearch.py DirName ExtensionTxt Docs")
        return
    
    RenameFileExt(sys.argv[1],sys.argv[2],sys.argv[3])


if __name__ == "__main__":
    main()