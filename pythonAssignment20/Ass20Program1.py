import threading

def Even(No):
    for i in range(2,No*2+1,2):
        if(i%2 == 0):
            print("Even : ",i)

def Odd(No):
    for i in range(1,No*2,2):
        if(i%2 != 0):
            print("Odd : ",i)

def main():
    t1 = threading.Thread(target=Even,args=(10,))
    t2 = threading.Thread(target=Odd,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()