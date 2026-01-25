
def ChkLength(str):
    return(len(str))
    
 
def main():
    print("Enter the name : ")
    str = input()
    Ret = ChkLength(str)
    print("Length of ",str," is ",Ret)

if __name__ == "__main__":
    main()