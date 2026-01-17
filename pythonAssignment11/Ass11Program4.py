def Reverse(Value):
    Reverse = 0 
    while(Value > 0):
        Digit = Value % 10
        Reverse = Reverse * 10 + Digit
        Value = Value // 10
    return Reverse

def main():
    No = 0
    Result = False
    print("Enter the number : ")
    No = int(input())
    Result = Reverse(No)
    print("Reverse of ",No, " is : ",Result)

if __name__ == "__main__":
    main()