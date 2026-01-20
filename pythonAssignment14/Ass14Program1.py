
CheckSquare = lambda no : (no **2)

def main():
    print("Enter the number : ")
    no = int(input())
    Ret = CheckSquare(no)
    print("square of ",no, " is : ",Ret)

if __name__ == "__main__":
    main()