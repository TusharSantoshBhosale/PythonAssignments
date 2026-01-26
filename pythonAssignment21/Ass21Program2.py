import threading

def Maximum(list):
    max_no = list[0]
    for no in list:
        if no > max_no:
            max_no = no
    print("Minimum number is : ",max_no)

def Minimum(list):
    min_no = list[0]
    for no in list:
        if no < min_no:
            min_no = no
    print("Minimum number is : ",min_no)
         

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

    t1 = threading.Thread(target=Maximum,args=(data,))
    t2 = threading.Thread(target=Minimum,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()