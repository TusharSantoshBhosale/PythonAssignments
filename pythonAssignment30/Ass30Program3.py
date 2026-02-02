import os

def DisplayLines(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print(f"{FileName} : File does not exist in current Directory ")
        return

    fobj = open(FileName,"r")
    for line in fobj:
        print(line,end=" ")


def main():
    print("Enter the file name : ")
    fname = input()
    DisplayLines(fname)

if __name__ == "__main__":
    main()