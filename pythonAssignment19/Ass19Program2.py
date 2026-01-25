
ChkMultiplication = lambda no1,no2 : no1*no2

def main():
    num1 = 0
    num2 = 0
    print("Enter first number : ")
    num1 = int(input())

    print("Enter second number : ")
    num2 = int(input())
    
    Ret = ChkMultiplication(num1,num2)
    print("Multiplication of numbers is : ",Ret)


if __name__ == "__main__":
    main()