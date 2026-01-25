Minimum = lambda No1,No2 : No2 if No1 > No2 else No1

def user_reduce(Task,Elements):
    result = Elements[0]

    for no in Elements:
        result = Task(result,no)
    return result

def main():
    value = 0
    print("enter how many elements you want : ")
    value = int(input()) 
    no = 0
    list = []
    for i in range(value):
        print(f"Enter the {i+1} Element : ")
        no = int(input())
        list.append(no)
    
    Ret = user_reduce(Minimum,list)
    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()