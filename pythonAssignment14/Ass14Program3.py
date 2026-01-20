
MaxNumber = lambda no1,no2 : no1 if no1 > no2 else no2

def main():
    print("Enter the number : ")
    no1 = int(input())

    print("Enter the number : ")
    no2 = int(input())

    Ret = MaxNumber(no1,no2)
    print(Ret," is Maximum")

if __name__ == "__main__":
    main()