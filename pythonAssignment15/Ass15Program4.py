
check_addition = lambda no1,no2 : no1+no2 

def user_reduce(Task,Elements):
    Result = 0

    for no in Elements:
        Result = Task(Result,no)
    return Result

def main():
    Value = 0
    data = []
    print("Enter how many elements you want : ")
    Value = int(input())

    for i in range(Value):
        print(f"enter {i+1} number : ")
        iNo = int(input())
        data.append(iNo)
    rData = user_reduce(check_addition,data)
    print("Addition of all elements is : ",rData)

if __name__ == "__main__":
    main()