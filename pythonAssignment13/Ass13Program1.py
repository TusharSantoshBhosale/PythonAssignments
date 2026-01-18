def AreaOfRactangle(lenght,width):
    Area = 0.0
    Area = lenght * width
    return Area

def main():
    length = 0.0
    width = 0.0
    print("Enter the length : ")
    length = float(input())

    print("Enter the length : ")
    width = float(input())
    
    Ret = AreaOfRactangle(length,width)
    print("Area of Ractangle is : ", Ret)


if __name__ == "__main__":
    main()