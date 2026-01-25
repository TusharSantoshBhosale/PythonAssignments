import Arithmetic

def main():
    no1 = 0
    no2 = 0

    print("Enter the first number : ")
    no1 = int(input())

    print("Enter the second number : ")
    no2 = int(input())

    Add = Arithmetic.Add(no1,no2)
    print("Addition is : ",Add)

    Sub = Arithmetic.Sub(no1,no2)
    print("Substratcion is : ",Sub)

    Mult = Arithmetic.Mult(no1,no2)
    print("Multiplication is : ",Mult)

    Div = Arithmetic.Div(no1,no2)
    print("Division is : ",Div)

if __name__ == "__main__":
    main()