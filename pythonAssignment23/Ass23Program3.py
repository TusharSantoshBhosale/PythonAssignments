class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        print("Is it prime number : ",end= " ")
        if(self.Value < 2):
            return False
        for no in range(2,self.Value):
            if(self.Value % no == 0):
                return False
        return True
        
        
    def ChkPerfect(self):
        print("Is it Perfect number : ",end= " ")
        #Helper Method
        if self.SumFactors() == self.Value:
            return True
        else:
            return False

        # sum = 0
        # for no in range(1,self.Value):
        #     if(self.Value % no == 0):
        #         sum += no
        # if sum == self.Value:
        #     return True
        # else:
        #     return False

    def Factors(self):
        print("Factors are : ",end= " ")
        for no in range(1,self.Value):
            if(self.Value % no == 0):
                print(no,end= " ")

    def SumFactors(self):
        sum = 0
        for no in range(1,self.Value):
            if(self.Value % no == 0):
                sum += no
        return sum


def main():
    obj1 = Numbers(6)
    obj2 = Numbers(7)
    obj3 = Numbers(28)

    print("For 6:")
    print(obj1.ChkPrime())
    print(obj1.ChkPerfect())
    print("Sum of Factors is : ",obj1.SumFactors())
    obj1.Factors()
    print("\n")

    print("For 7:")
    print(obj2.ChkPrime())
    print(obj2.ChkPerfect())
    print("Sum of Factors is : ",obj2.SumFactors())
    obj2.Factors()
    print("\n")

    print("For 28:")
    print(obj3.ChkPrime())
    print(obj3.ChkPerfect())
    print("Sum of Factors is : ",obj3.SumFactors())
    obj3.Factors()
if __name__ == "__main__":
    main()