
check_minimum = lambda no1,no2 : no2 if no1 > no2 else no1

def user_reduce(Task,Elements):
    Result = Elements[0]

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
    rData = user_reduce(check_minimum,data)
    print("Minimum number is  : ",rData)

if __name__ == "__main__":
    main()