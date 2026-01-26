import threading

sumResult = 0
productResult = 1

def Sum(list):
     global sumResult
     for no in list:
         sumResult += no

def Product(list):
    global productResult
    for no in list:
        productResult *= no
    

def main():
    data = [10,36,58,63,23,77,54,89,11,62,49]

    t1 = threading.Thread(target=Sum,args=(data,))
    t2 = threading.Thread(target=Product,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is : ",sumResult)
    print("Product of elements is : ",productResult)

if __name__ == "__main__":
    main()