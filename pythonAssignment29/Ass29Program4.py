import os
import sys
import filecmp

def CompareContent(FileName1,FileName2):
    Ret = os.path.exists(FileName1)
    if(Ret == False):
        print(f"{FileName1} : File does not exist in current Directory ")
        return
    Ret = os.path.exists(FileName2)
    if(Ret == False):
        print(f"{FileName2} : File does not exist in current Directory ")
        return
    

    if filecmp.cmp(FileName1, FileName2):
        print("Success")
    else:
        print("Failure")
        
def main():
    
    if(len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Please specify the name of Directory")
        return

    CompareContent(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()