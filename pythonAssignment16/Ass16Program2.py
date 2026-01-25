
def ChkNum(value):
    if(value % 2 == 0):
        return True
    else:
        return False
    
def main():
    no = 0
    Ret = False
    print("Enter the number : ")
    no = int(input())
    Ret=ChkNum(no)

    if(Ret==True):
        print("Even Number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()