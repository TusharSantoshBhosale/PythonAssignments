
def FrequencyCount(list,digit):
    count = 0
    for no in list:
        if(digit == no):
            count+=1
    return count


def main():
    value = 0
    print("enter how many elements you want : ")
    value = int(input()) 
    no = 0
    list = []
    for i in range(value):
        print(f"Enter the {i+1} Element : ")
        no = int(input())
        list.append(no)
    
    print("Enter element to search : ")
    value1 = int(input()) 
    
    Ret = FrequencyCount(list,value1)
    print("Frequeny of ",value1," in list is : ",Ret)

if __name__ == "__main__":
    main()