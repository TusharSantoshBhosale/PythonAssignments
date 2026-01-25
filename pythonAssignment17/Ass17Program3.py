def ChkFact(no):
    result = 1
    for i in range(no,0,-1):
        result *= i
    return result

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    Ret = ChkFact(no)
    print("Factorail of ",no," is : ",Ret)

if __name__ == "__main__":
    main()