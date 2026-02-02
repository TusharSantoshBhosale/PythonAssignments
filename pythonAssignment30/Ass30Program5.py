import os

def WordSearch(FileName1,input):
    Ret = os.path.exists(FileName1)

    if(Ret == False):
        print(f"{FileName1} : File does not exist in current Directory ")
        return

    with open(FileName1,"r") as fobj:
        data = fobj.read()
        Ret = data.split()
        if input in Ret:
            print(f"'{input}' is found in the {FileName1}.")
        else:
            print(f"'{input}' is not found in the {FileName1}.")
    

def main():
    print("Enter the Existing file name : ")
    fname1 = input()
    print("Enter the new file name : ")
    Value = input()
    WordSearch(fname1,Value)

if __name__ == "__main__":
    main()