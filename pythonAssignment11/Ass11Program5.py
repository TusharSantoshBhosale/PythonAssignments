def ChkPallindrome(Value):
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
    Result = ChkPallindrome(No)
    if Result == No:
        print("Number is Pallindrome")
    else:
        print("Number is Not Pallindrome")

if __name__ == "__main__":
    main()