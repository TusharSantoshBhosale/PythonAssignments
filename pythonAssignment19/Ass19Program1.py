
ChkPower = lambda no : no**2

def main():
    num = 0
    print("Enter the number : ")
    num = int(input())
    
    Ret = ChkPower(num)
    print("Power of ",num,"is : ",Ret)


if __name__ == "__main__":
    main()