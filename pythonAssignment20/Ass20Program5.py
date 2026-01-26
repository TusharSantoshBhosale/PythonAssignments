import threading

lobj = threading.Lock()

def Thread1():
    with lobj:
        for i in range(1,50+1):
            print(i, end=" ")
    
def Thread2():
    with lobj:
        for i in range(50,0,-1):
            print(i, end=" ")

def main():
    
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()