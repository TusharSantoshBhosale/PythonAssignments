
check_length = lambda value : len(value) > 5

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
        print(f"enter {i+1} value  : ")
        str = input()
        data.append(str)

    fData = user_filter(check_length,data)
    print(" String having length greater than 5  : ",fData)

if __name__ == "__main__":
    main()