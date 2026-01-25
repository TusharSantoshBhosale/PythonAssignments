from functools import reduce

def ChkEven(num):
    if num % 2 == 0:
        return num
    

def ChkSquare(num):
    return num**2

def ChkAddition(num1, num2):
    return num1 + num2
    

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
    
    fData = list(filter(ChkEven,Data))
    print("Even numbers are : ",fData)

    mData = list(map(ChkSquare,fData))
    print("Square of each element is : ",mData)

    rData = reduce(ChkAddition,mData)
    print("Addition is : ",rData)

if __name__ == "__main__":
    main()