import math

def AreaOfCircle(radius):
    Area = math.pi * radius * radius
    return Area

def main():
    radius = 0.0
    
    print("Enter the radius : ")
    radius = float(input())

    Ret = AreaOfCircle(radius)
    print("Area of Circle is : ", Ret)


if __name__ == "__main__":
    main()