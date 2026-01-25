def SumFactors(no):
    sum = 0 
    for i in range(1,no):
        if(no % i == 0):
            sum+=i
    return sum

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    Ret = SumFactors(no)
    print("sum of factors of ",no," is : ",Ret)

if __name__ == "__main__":
    main()