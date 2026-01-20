
chk_largest = lambda no1,no2,no3 : no1 if no1>=no2 and no1>=no3 else no2 if no2 > no3 else no3

def main():
    print("Enter the number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    print("Enter third number : ")
    no3 = int(input())

    Ret = chk_largest(no1,no2,no3)
    print("Largest element is : ",Ret)

if __name__ == "__main__":
    main()