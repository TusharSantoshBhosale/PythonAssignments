import os
import sys

def CopyContent(FileName):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("File does not exist in current Directory")
        return
    
    fobj = open(FileName,"r")
    Data = fobj.read()

    cobj = open("Demo.txt","w")
    cobj.write(Data)
    fobj.close()
    cobj.close()
        
def main():
    
    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("Please specify the name of Directory")
        return

    CopyContent(sys.argv[1])


if __name__ == "__main__":
    main()