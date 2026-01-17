def Square(Value1):
    return Value1**2

def main():
    No1 = 0
    No2 = 0
    Result = 0 

    print("Enter the first number : ")
    No1 = int(input())
    Result = Square(No1)
    print("Sqaure of ",No1," is : ",Result)

if __name__ == "__main__":
    main()