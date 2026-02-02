import os

def WordCount(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print(f"{FileName} : File does not exist in current Directory ")
        return

    fobj = open(FileName,"r")
    Data = fobj.read()
    Ret = Data.split()
    print("Total number of Lines is : ",len(Ret)) 


def main():
    print("Enter the file name : ")
    fname = input()
    WordCount(fname)

if __name__ == "__main__":
    main()