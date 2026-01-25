def DigitCount(no):
    count = 0 
    while(no > 0):
        no = no // 10
        count +=1
    return count

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    Ret = DigitCount(no)
    print("Count of digits in ",no," is : ",Ret)

if __name__ == "__main__":
    main()