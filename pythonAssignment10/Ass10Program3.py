def Factorial(Value):
    fact = 1
    for i in range(1,Value+1):
        fact *= i
    return fact

def main():
    No1 = 0
    print("Enter number number : ")
    No1 = int(input())
    Result = Factorial(No1)
    print("Factorial of ",No1," is : ",Result)

if __name__ == "__main__":
    main()