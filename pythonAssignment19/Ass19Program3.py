from functools import reduce

def ChkFilter(num):
    return num >= 70 and num <= 90 
    

def ChkMap(num):
    return num + 10

def ChkReduce(num1, num2):
    return num1 * num2
    

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
    
    fData = list(filter(ChkFilter,Data))
    print("Data is greater than equals 70 and less than equals 90 are : ",fData)

    mData = list(map(ChkMap,fData))
    print("Increase each number by 10 : ",mData)

    rData = reduce(ChkReduce,mData)
    print("Increase each number by 10 : ",rData)

if __name__ == "__main__":
    main()