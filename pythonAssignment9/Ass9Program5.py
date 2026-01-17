def Divisible(Value1):
    if(Value1 % 3 == 0 & Value1 % 5 == 0):
        return True
    else:
        return False

def main():
    No1 = 0
    No2 = 0
    Result = False 

    print("Enter the first number : ")
    No1 = int(input())
    Result = Divisible(No1)
    if(Result == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is Not divisible by 3 and 5")

if __name__ == "__main__":
    main()