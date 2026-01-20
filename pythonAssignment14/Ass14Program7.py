
check_divisible= lambda no1 : no1 % 5 == 0

def main():
    print("Enter the number : ")
    no1 = int(input())

    Ret = check_divisible(no1)
    
    if(Ret == True):
        print("Number is Divisible by 5 ")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()