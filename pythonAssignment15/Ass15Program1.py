
check_square = lambda No : No**2

def user_map(Task,Elements):
    Result = list()

    for no in Elements:
        Ret =  Task(no)
        Result.append(Ret)

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
    
    mData = list(user_map(check_square,data))
    print("Squares are : ",mData)
    
if __name__ == "__main__":
    main()