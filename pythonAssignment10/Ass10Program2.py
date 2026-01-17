def Summation(Value):
    sum = 0
    for i in range(Value+1):
        sum += i
    return sum

def main():
    No1 = 0
    print("Enter number number : ")
    No1 = int(input())
    Result = Summation(No1)
    print("Sum of first ",No1, " natural numbers is : ",Result)

if __name__ == "__main__":
    main()