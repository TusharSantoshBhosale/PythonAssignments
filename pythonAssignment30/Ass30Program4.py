import os

def CopyContent(FileName1,FileName2):
    Ret = os.path.exists(FileName1)

    if(Ret == False):
        print(f"{FileName1} : File does not exist in current Directory ")
        return

    with open(FileName1,"r") as fobj:
        data = fobj.read()

    with open(FileName2,"w") as wobj:
        Ret = wobj.write(data)
        if(Ret):
            print(f"Contents of {FileName1} copied into {FileName2}")



def main():
    print("Enter the Existing file name : ")
    fname1 = input()
    print("Enter the new file name : ")
    fname2 = input()
    CopyContent(fname1,fname2)

if __name__ == "__main__":
    main()