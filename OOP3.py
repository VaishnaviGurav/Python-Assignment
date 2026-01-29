class Arithmetic:
    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division with zero handling
    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return self.Value1 / self.Value2


# Create multiple objects
Obj1 = Arithmetic()
Obj2 = Arithmetic()

# For Obj1
Obj1.Accept()
print("Addition       :", Obj1.Addition())
print("Subtraction    :", Obj1.Subtraction())
print("Multiplication :", Obj1.Multiplication())
print("Division       :", Obj1.Division())
print("----------------------------")

# For Obj2
Obj2.Accept()
print("Addition       :", Obj2.Addition())
print("Subtraction    :", Obj2.Subtraction())
print("Multiplication :", Obj2.Multiplication())
print("Division       :", Obj2.Division())
