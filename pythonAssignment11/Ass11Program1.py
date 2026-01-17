def ChkPrime(Value):
    if(Value <= 1):
        return False
    for i in range(2,Value):
        if(Value % 2 == 0):
            return False
    return True
        

def main():
    No = 0
    Result = False
    print("Enter the number : ")
    No = int(input())
    Result = ChkPrime(No)
    if(Result == True):
        print(No, " Is Prime Number")
    else :
        print(No, " Is NotPrime Number")

if __name__ == "__main__":
    main()