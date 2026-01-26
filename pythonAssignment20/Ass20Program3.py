import threading

def EvenList(list):
    sum = 0
    for no in list:
        if no % 2 == 0:
            print("Even number : ",no)
            sum += no 
    print("Even sum is : ",sum)
    print("Exit from Odd Method")

def OddList(list):
    total = 0
    for no in list:
        if no % 2 != 0:
            print("Odd is : ",no)
            total += no
    print("Odd sum is : ",total)
    print("Exit from Odd Method")

def main():
    data = []
    No = 0
    print("Enter how many elements you want : ")
    No = int(input())

    for i in range(No):
        value = 0
        print(f"Enter the {i+1} number : ")
        value = int(input())
        data.append(value)
    print(data)

    t1 = threading.Thread(target=EvenList,args=(data,))
    t2 = threading.Thread(target=OddList,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("Exit from main")

if __name__ == "__main__":
    main()