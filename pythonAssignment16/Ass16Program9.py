
def ChkEven(value):
    for i in range(2,value * 2 +1,2):
        print(i, end= " ")
 
def main():
    No = 10
    Ret=ChkEven(No)

if __name__ == "__main__":
    main()