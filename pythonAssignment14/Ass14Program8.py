
chk_addition = lambda no1,no2 : no1 + no2

def main():
    print("Enter the number : ")
    no1 = int(input())

    print("Enter the number : ")
    no2 = int(input())

    Ret = chk_addition(no1,no2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()