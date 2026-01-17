def Multiplicationtable(Value):
    table = []
    for i in range(1,11):
        table.append(Value * i)
    return table

def main():
    No1 = 0
    print("Enter number which you want multiplication table : ")
    No1 = int(input())
    Result = Multiplicationtable(No1)
    print(Result)

if __name__ == "__main__":
    main()