import threading

def EvenFactor(No):
    total = 0
    for i in range(1,No+1):
        if (No % i == 0) and (i % 2 == 0):
            print("Even Factor is : ",i)
            total += i 
    print("Even Factors sum is : ",total)
    print("Exit from EvenFactor Method")

def OddFactor(No):
    total = 0
    for i in range(1,No+1):
        if (No % i == 0) and (i % 2 != 0):
            print("Odd Factor is : ",i)
            total += i 
    print("Odd Factors sum is : ",total)
    print("Exit from OddFactor Method")

def main():
    No1 = 0
    print("Enter the number : ")
    No1 = int(input())
    t1 = threading.Thread(target=EvenFactor,args=(No1,))
    t2 = threading.Thread(target=OddFactor,args=(No1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()