
check_divisible= lambda no : no % 3== 0  and no % 5 == 0 

def user_filter(Task,Elements):
    Result = list()

    for value in Elements:
        Ret = Task(value)
        if(Ret == True):
            Result.append(value)
    return Result

def main():
    data = []
    print("Enter how many elements you want : ")
    Value = int(input())

    for i in range(Value):
        print(f"enter {i+1} numbers  : ")
        no = int(input())
        data.append(no)

    rData = user_filter(check_divisible,data)
    print("number is divisible by 3 and 5 are : ",rData)

if __name__ == "__main__":
    main()