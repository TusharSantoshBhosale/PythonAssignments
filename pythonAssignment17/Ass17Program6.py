def DisplayPattern(no):
    for i in range(no,0,-1):
        for j in range(i):
            print(" * " , end= " ")
        print()

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    DisplayPattern(no)

if __name__ == "__main__":
    main()