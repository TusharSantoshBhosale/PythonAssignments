import threading

counter = 0
lObj = threading.Lock()

def Counter():
    global counter
    with lObj:
        counter += 1
        print("updated counter value is : ",counter)

def main():
    
    t1 = threading.Thread(target=Counter)
    t2 = threading.Thread(target=Counter)
    t3 = threading.Thread(target=Counter)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()