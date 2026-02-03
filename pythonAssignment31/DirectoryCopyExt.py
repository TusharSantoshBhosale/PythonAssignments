import sys
import os
import shutil

def DirectoryCopyMethod(DirName1,DirName2,Extention):
    log = open("DirectoryCopyExtLogFile","w")

    if not os.path.isdir(DirName1):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    if not os.path.isdir(DirName2):
        os.mkdir(DirName2)

    Count = 0
    for FolderName, SubFolder, FileName in os.walk(DirName1):
        for fname in FileName:
            if(fname.endswith(Extention)):
                Count += 1
                oldFolder = os.path.join(DirName1,fname)
                NewFolder = os.path.join(DirName2,fname)
                shutil.copy2(oldFolder,NewFolder)
                log.write(f"Files are copied into {DirName2}")
            if(Count == 0):
                log.write(f"There is no {Extention} files")
        
    log.close

def main():
    if(len(sys.argv) != 4):
        print("Usage : DirectoryFileSearch.py DirName1 DirName2 Extension")
        return
    
    DirectoryCopyMethod(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()