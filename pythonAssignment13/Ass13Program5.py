
def number_into_binary(number):
    if number == 0:
        return 0

    binary = ""
    while(number > 0 ):
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    
    return binary

def main():
    no = 0
    
    print("Enter the number : ")
    no = int(input())

    Ret = number_into_binary(no)
    print("binary number of ",no,"is : ",Ret)

if __name__ == "__main__":
    main()