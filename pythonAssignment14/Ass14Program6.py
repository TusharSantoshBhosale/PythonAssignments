
CheckOdd = lambda no1 : no1 % 2 != 0

def main():
    print("Enter the number : ")
    no1 = int(input())

    Ret = CheckOdd(no1)
    print(Ret)

if __name__ == "__main__":
    main()