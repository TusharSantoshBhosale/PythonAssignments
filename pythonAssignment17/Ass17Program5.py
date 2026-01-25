def ChkPrime(no):
    if(no <= 1):
        return False
    for i in range(2,no):
        if(no % i == 0):
            return False
    return True

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    Ret = ChkPrime(no)
    if(Ret == True):
        print("Prime number")
    else:
        print("not prime number")

if __name__ == "__main__":
    main()