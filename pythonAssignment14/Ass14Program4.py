
MinNumber = lambda no1,no2 : no1 if no1 < no2 else no2

def main():
    print("Enter the number : ")
    no1 = int(input())

    print("Enter the number : ")
    no2 = int(input())

    Ret = MinNumber(no1,no2)
    print(Ret," is Minimum")

if __name__ == "__main__":
    main()