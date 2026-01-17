def Cube(Value1):
    return Value1**3

def main():
    No1 = 0
    No2 = 0
    Result = 0 

    print("Enter the first number : ")
    No1 = int(input())
    Result = Cube(No1)
    print("Cube of ",No1," is : ",Result)

if __name__ == "__main__":
    main()