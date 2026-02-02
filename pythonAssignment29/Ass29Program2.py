import os

def Display(FileName):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("File does not exist in current Directory")
        return
    
    fobj = open(FileName,"r")
    Data = fobj.read()
    print(Data)
    fobj.close()
        
def main():
    fname = str
    print("Enter the file name : ")
    fname = input()
    Display(fname)


if __name__ == "__main__":
    main()