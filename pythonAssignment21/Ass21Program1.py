import threading

def Prime(list):
    for no in list:
        if(no < 2):
            continue
        iRet = True
        for i in range(2,no):
            if (no % i) == 0:
                iRet = False
                break  
        if(iRet):
            print("prime number : ",no)  

def NonPrime(list):
    for no in list:
        if(no < 2):
            continue
        iRet = True
        for i in range(2,no):
            if (no % i) == 0:
                iRet = False
                break  
        if(iRet == False):
            print("nonPrime number : ",no)  

def main():
    data = [10,36,58,63,23,77,54,89,11,62,49]

    t1 = threading.Thread(target=Prime,args=(data,))
    t2 = threading.Thread(target=NonPrime,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()