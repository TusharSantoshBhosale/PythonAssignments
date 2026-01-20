
count_even_numbers= lambda no : no % 2== 0   

def user_filter(Task,Elements):
    Result = list()

    for value in Elements:
        Ret = Task(value)
        if(Ret == True):
            Result.append(value)
    return len(Result)

def main():
    data = []
    print("Enter how many elements you want : ")
    Value = int(input())

    for i in range(Value):
        print(f"enter {i+1} numbers  : ")
        no = int(input())
        data.append(no)

    fData = user_filter(count_even_numbers,data)
    print("count of even numbers is : ",fData)

if __name__ == "__main__":
    main()