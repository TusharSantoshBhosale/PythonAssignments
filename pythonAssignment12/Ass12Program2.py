def Factorial(Value):
    for i in range(1,Value + 1):
        if(Value % i == 0):
            print(i,end=" ")

def main():
    Result = False
    print("Enter the number : ")
    No = int(input())
    Factorial(No)
    
if __name__ == "__main__":
    main()