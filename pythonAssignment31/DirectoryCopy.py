import sys
import os
import shutil

def DirectoryCopyMethod(DirName1,DirName2):
    log = open("DirectoryCopyLogFile","w")

    if not os.path.isdir(DirName1):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    if not os.path.isdir(DirName2):
        os.mkdir(DirName2)

    for FolderName, SubFolder, FileName in os.walk(DirName1):
        for fname in FileName:
            oldFolder = os.path.join(DirName1,fname)
            print(oldFolder)
            NewFolder = os.path.join(DirName2,fname)
            print(NewFolder)


            if(os.path.isfile(oldFolder)):
                shutil.copy2(oldFolder,NewFolder)
                log.write(f"Files are copied into {DirName2}")
        
    log.close

def main():
    if(len(sys.argv) != 3):
        print("Usage : DirectoryFileSearch.py DirName1 DirName2 ")
        return
    
    DirectoryCopyMethod(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()