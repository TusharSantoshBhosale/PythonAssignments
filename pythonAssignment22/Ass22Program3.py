class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        print("Enter the first value : ")
        self.Value1 = int(input())
        print("Enter the second value : ")
        self.Value2 = int(input())
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if(self.Value2 == 0):
            return "Division by zero is not allowed"
        return self.Value1 / self.Value2
    
def main():
    obj1 = Arithmetic()
    obj1.Accept()
    print("Addition is : ",obj1.Addition())
    print("Substraction is : ",obj1.Substraction())
    print("Multiplication is : ",obj1.Multiplication())
    print("Division is : ",obj1.Division())

    obj2 = Arithmetic()
    obj2.Accept()
    print("Addition is : ",obj2.Addition())
    print("Substraction is : ",obj2.Substraction())
    print("Multiplication is : ",obj2.Multiplication())
    print("Division is : ",obj2.Division())

    obj3 = Arithmetic()
    obj3.Accept()
    print("Addition is : ",obj3.Addition())
    print("Substraction is : ",obj3.Substraction())
    print("Multiplication is : ",obj3.Multiplication())
    print("Division is : ",obj3.Division())

if __name__ == "__main__":
    main()
    