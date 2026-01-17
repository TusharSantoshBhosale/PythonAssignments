def ChkGreater(Value1,Value2):
    if(Value1 > Value2):
        return Value1
    else :
        return Value2

def main():
    No1 = 0
    No2 = 0
    Result = 0 

    print("Enter the first number : ")
    No1 = int(input())
    print("Enter the second number : ")
    No2 = int(input())
    Result = ChkGreater(No1,No2)
    print(Result, " is Greater Number")

if __name__ == "__main__":
    main()