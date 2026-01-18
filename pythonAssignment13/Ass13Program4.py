
def is_perfect_numner(number):
    if number <= 1:
        return False
    
    divisor_sum = 0

    for i in range (1,number):
        if (number % i == 0) :
            divisor_sum += i
    print(divisor_sum)
    return divisor_sum

def main():
    no = 0
    
    print("Enter the number : ")
    no = int(input())

    Ret = is_perfect_numner(no)
    if(Ret == no):
        print("Given Number is Perfect")
    else:
        print("Given Number is Not Perfect")

if __name__ == "__main__":
    main()