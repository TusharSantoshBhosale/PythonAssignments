import os

def LineCount(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print(f"{FileName} : File does not exist in current Directory ")
        return

    fobj = open(FileName,"r")
    Data = fobj.readlines()
    print("Total number of Lines is : ",len(Data)) 

def main():
    print("Enter the file name : ")
    fname = input()
    LineCount(fname)

if __name__ == "__main__":
    main()