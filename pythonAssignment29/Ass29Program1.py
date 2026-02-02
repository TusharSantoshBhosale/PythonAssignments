import os

def CurrentDirectory(FileName):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("File does not exist in current Directory")
    else:
        print("File exist in current Directory")

def main():
    fname = str
    print("Enter the file name : ")
    fname = input()
    CurrentDirectory(fname)


if __name__ == "__main__":
    main()