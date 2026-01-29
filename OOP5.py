class BankAccount:
    # Class variable
    ROI = 10.5   # Rate of Interest

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance     :", self.Amount)

    # Deposit money
    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        if amt > 0:
            self.Amount += amt
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw money
    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= 0:
            print("Invalid withdrawal amount.")
        elif amt > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= amt
            print("Amount withdrawn successfully.")

    # Calculate interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Create multiple objects
Obj1 = BankAccount("Vaishnavi", 10000)
Obj2 = BankAccount("Amit", 5000)

# Demonstrate all methods for Obj1
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest on balance:", Obj1.CalculateInterest())
print("----------------------------")

# Demonstrate all methods for Obj2
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest on balance:", Obj2.CalculateInterest())
