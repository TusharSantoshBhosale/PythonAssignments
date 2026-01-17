def PrintNumbers(No1):
    for i in range(1,No1+1):
        print(i, end= " ")

def main():
    Value1 = 0

    print("Enter the first number : ")
    Value1 = int(input())
    PrintNumbers(Value1)

if __name__ == "__main__":
    main()