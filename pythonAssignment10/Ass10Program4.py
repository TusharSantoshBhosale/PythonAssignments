def ChkEven(Value):
    list = []
    for i in range(1,Value+1):
         if(i % 2 == 0):
             list.append(i)
    return list

def main():
    No1 = 0
    print("Enter number number : ")
    No1 = int(input())
    Result = ChkEven(No1)
    print("Even Number upto ",No1 ," is : ",Result)

if __name__ == "__main__":
    main()