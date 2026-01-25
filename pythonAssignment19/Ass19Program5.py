from functools import reduce

def ChkPrime(num):
    if num < 2:
        return
    
    for no in range(2,num):
        if num % no == 0:
            return

    return num 
    

def ChkMultiply(num):
    return num*2

def ChkMaximum(num1, num2):
    return num1 if num1 > num2 else num2
    

def main():
    value = 0
    print("enter how many elements you want : ")
    value = int(input()) 
    no = 0
    Data = []
    for i in range(value):
        print(f"Enter the {i+1} Element : ")
        no = int(input())
        Data.append(no) 
    
    fData = list(filter(ChkPrime,Data))
    print("Prime numbers are : ",fData)

    mData = list(map(ChkMultiply,fData))
    print("Each number multiply by 2 : ",mData)

    rData = reduce(ChkMaximum,mData)
    print("Maximum numbers is : ",rData)

if __name__ == "__main__":
    main()