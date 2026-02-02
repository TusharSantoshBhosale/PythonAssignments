import os
import sys
import filecmp

def SearchString(FileName,searchStr):
    Count = 0
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} : File does not exist in current Directory ")
        return
    
    fobj = open(FileName,"r")
    Data = fobj.read().lower()

    words = Data.split()

    for str in words:
        if(str == searchStr):
            Count += 1
    return Count
  
def main():
    
    print("Please specify the name of file : ")
    fname = input()

    print("Enter String to be searched : ")
    strSearch = input()

    Ret = SearchString(fname,strSearch)

    print(f"Count of {strSearch} in {fname} is : ",Ret)


if __name__ == "__main__":
    main()