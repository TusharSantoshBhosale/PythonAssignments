class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("-"*40)
        print("Account holder name is : ",self.Name)
        print("Account Current Balance is : ",self.Amount)
        print("-"*40)

    def Deposite(self):
        print("-"*40)
        iAmount = 0
        print("Enter Amount to deposite : ")
        iAmount = float(input())
        self.Amount += iAmount
        print("Amount Deposite Successfully. Current Balance is : ",self.Amount)
        print("-"*40)
    
    def Withdraw(self):
        print("-"*40)
        iAmount = 0
        print("Enter Amount to withdraw : ")
        iAmount = float(input())
        if iAmount <= self.Amount:
            self.Amount -= iAmount
            print("Amount Withdraw Successfully. Current Balance is : ",self.Amount)
        else:
            print("Insufficient balance. withdraw not allowed.")
        print("-"*40)

    def CalculateInterest(self):
        print("-"*40)
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("-"*40)
        return Interest
        

def main():
    obj1 = BankAccount("TUSHAR SANTOSH BHOSALE" , 2000000)
    obj1.Display()
    obj1.Deposite()
    obj1.Withdraw()
    print("Interest is :  ",obj1.CalculateInterest())

    obj2 = BankAccount("AJINKYA KUMAR MORE" , 1250000)
    obj2.Display()
    obj2.Deposite()
    obj2.Withdraw()
    print("Interest is :  ",obj2.CalculateInterest())

    obj3 = BankAccount("SUNIL SAMBHAJI BORKAR" , 1590000)
    obj3.Display()
    obj3.Deposite()
    obj3.Withdraw()
    print("Interest is :  ",obj3.CalculateInterest())

if __name__ == "__main__":
    main()