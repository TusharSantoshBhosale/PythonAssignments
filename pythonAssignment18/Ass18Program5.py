import MarvellousNum

def ListPrime(list):
    Sum = 0
    for num in list:
        if MarvellousNum.ChkPrime(num):
            Sum += num

    return Sum


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
    
    Ret = ListPrime(list)
    print("Addition of Prime numbers is : ",Ret)

if __name__ == "__main__":
    main()