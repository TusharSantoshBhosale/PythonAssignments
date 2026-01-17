def Addition(No1,No2):
    return No1+No2

def Substraction(No1,No2):
    return No1-No2

def Multiplication(No1,No2):
    return No1*No2

def Division(No1,No2):
    return No1/No2

def main():
    Value1 = 0
    Value2 = 0
    Result = 0
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Result = Addition(Value1,Value2)
    print("Addition is : ",Result)

    Result = Substraction(Value1,Value2)
    print("Substraction is : ",Result)

    Result = Multiplication(Value1,Value2)
    print("Multiplication is : ",Result)

    Result = Division(Value1,Value2)
    print("Division is : ",Result)

if __name__ == "__main__":
    main()