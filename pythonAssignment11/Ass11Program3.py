def SumOfDigits(Value):
    Sum = 0
    while(Value > 0):
        Digit = Value % 10
        Sum += Digit
        Value = Value // 10
    return Sum

def main():
    No = 0
    Result = False
    print("Enter the number : ")
    No = int(input())
    Result = SumOfDigits(No)
    print("Sum Of All Digits in ",No, " is : ",Result)

if __name__ == "__main__":
    main()