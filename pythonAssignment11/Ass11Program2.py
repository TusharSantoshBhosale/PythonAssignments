def IsCount(Value):
    Count = 0
    while(Value > 0):
        Value = Value // 10
        Count += 1
    return Count


def main():
    No = 0
    Result = False
    print("Enter the number : ")
    No = int(input())
    Result = IsCount(No)
    print("Count of Number in ",No, " is : ",Result)

if __name__ == "__main__":
    main()