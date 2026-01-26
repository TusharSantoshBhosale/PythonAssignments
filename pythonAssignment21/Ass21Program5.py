import threading

value = 10
lObj = threading.Lock()

def add():
    global value
    with lObj:
        value += 10
        print("After adding 10 : ",value)

def sub():
    global value
    with lObj:
        value -= 5
        print("After subtracting 5 : ",value)

def mult():
    global value
    with lObj:
        value *= 2
        print("After multiply by 2 : ",value)
         

def main():
    
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)
    t3 = threading.Thread(target=mult)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()