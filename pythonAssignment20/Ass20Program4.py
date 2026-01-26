import threading

def Small(str):
    count = 0
    for ch in str:
        if (ch >= "a") and (ch <= "z"):
            count += 1
    print("Number of Lowercase characters is : ",count)
    print("Thread Id is : ",threading.get_ident())
    print("Thread Name is : ",threading.current_thread().name)

def Capital(str):
    count = 0
    for ch in str:
        if (ch >= "A") and (ch <= "Z"):
            count += 1
    print("Number of UpperCase characters is : ",count)
    print("Thread Id is : ",threading.get_ident())
    print("Thread Name is : ",threading.current_thread().name)

def Digit(str):
    count = 0
    for ch in str:
        if (ch >= "0") and (ch <= "9"):
            count += 1
    print("Number of numeric digit is : ",count)
    print("Thread Id is : ",threading.get_ident())
    print("Thread Name is : ",threading.current_thread().name)


def main():
    str = ""
    print("Enter the text : ")
    str = input()

    t1 = threading.Thread(target=Small,args=(str,))
    t2 = threading.Thread(target=Capital,args=(str,))
    t3 = threading.Thread(target=Digit,args=(str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


    print("Exit from main")

if __name__ == "__main__":
    main()