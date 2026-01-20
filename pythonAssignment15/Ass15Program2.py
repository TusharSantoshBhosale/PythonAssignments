
check_even = lambda No : No % 2 == 0

def user_filter(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
    return Result

def main():
    value  = 0
    data = []
    print("Enter the number how many element you want : ")
    value = int(input())

    for i in range(value):
        print(f"Enter the Number : {i+1}")
        no = int(input())
        data.append(no)
    
    fData = list(user_filter(check_even,data))
    print("Even numbers are : ",fData)
    
if __name__ == "__main__":
    main()