class Demo:
    # Class variable
    Value = 0

    # Constructor
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    # Instance method Fun
    def Fun(self):
        print("Inside Fun()")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

    # Instance method Gun
    def Gun(self):
        print("Inside Gun()")
        print("no1 =", self.no1)
        print("no2 =", self.no2)


# Create two objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Call methods in given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
