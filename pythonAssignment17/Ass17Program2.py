def DisplayPattern(no):
    for i in range(no):
        for j in range(no):
            print(" * " , end= " ")
        print()

def main():
    no = 0

    print("Enter the first number : ")
    no = int(input())

    DisplayPattern(no)

if __name__ == "__main__":
    main()