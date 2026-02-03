import sys
import os

def FileWithExt(DirName,Extension):
    log = open("LogFile","w")

    if not os.path.isdir(DirName):
        log.write("Invalid Directory \n")
        log.close()
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(Extension):
                log.write(fname + "\n")
    log.close()

def main():

    if(len(sys.argv) != 3):
        print("Usage : DirectoryFileSearch.py DirName Extension")
        return

    FileWithExt(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()