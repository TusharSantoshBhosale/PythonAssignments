
check_product= lambda no1,no2 : no1 * no2

def user_filter(Task,Elements):
    Result = Elements[0] 

    for no in Elements:
        Result = Task(Result,no)
    return Result

def main():
    data = []
    print("Enter how many elements you want : ")
    Value = int(input())

    for i in range(Value):
        print(f"enter {i+1} numbers  : ")
        no = int(input())
        data.append(no)

    fData = user_filter(check_product,data)
    print("Product of all numbers are : ",fData)

if __name__ == "__main__":
    main()