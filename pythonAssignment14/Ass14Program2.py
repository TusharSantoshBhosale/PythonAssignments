
CheckCube = lambda no : (no **3)

def main():
    print("Enter the number : ")
    no = int(input())
    Ret = CheckCube(no)
    print("Cube of ",no, " is : ",Ret)

if __name__ == "__main__":
    main()