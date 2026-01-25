def AddInNumbers(no):
    sum = 0
    while(no > 0):
        temp = no % 10
        sum += temp
        no //= 10
    return sum

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    Ret = AddInNumbers(no)
    print("Addition of digits in ",no," is : ",Ret)

if __name__ == "__main__":
    main()