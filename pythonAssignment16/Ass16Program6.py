
def ChkNum(value):
    if (value == 0):
        return "Zero"
    elif (value > 0):
        return "Positive"
    else:
        return "Negative"
    
    
def main():
    no = 0
    print("Enter the number : ")
    no = int(input())
    Ret=ChkNum(no)

    if(Ret=="Zero"):
        print("Zero")
    elif(Ret == "Positive"):
        print("Positive")
    else:
        print("Negative")

if __name__ == "__main__":
    main()