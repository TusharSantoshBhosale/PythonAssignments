
def ChkDivisible(value):
    if (value % 5 == 0):
        return True
    else:
        return False
    
def main():
    no = 0
    print("Enter the number : ")
    no = int(input())
    Ret=ChkDivisible(no)
    print(Ret)

if __name__ == "__main__":
    main()