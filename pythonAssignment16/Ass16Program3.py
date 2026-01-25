
def Add(value1,value2):
    return value1 + value2
    
def main():
    no1 = 0
    no2 = 0

    print("Enter the number : ")
    no1 = int(input())

    print("Enter the number : ")
    no2 = int(input())

    Ret=Add(no1,no2)
    print("Addition of two numbers is : ",Ret)

if __name__ == "__main__":
    main()