def Addition(list):
    sum = 0
    for num in list:
        sum += num
    return sum

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
    
    Ret = Addition(list)
    print("Addition of numbers is : ",Ret)

if __name__ == "__main__":
    main()