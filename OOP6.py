class Numbers:
    # Constructor accepts a number from the user
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    # Check if number is prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    # Display all factors of the number
    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Return sum of all factors
    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i
        return total

    # Check if number is perfect
    def ChkPerfect(self):
        # A perfect number = sum of its proper divisors (excluding itself)
        return self.SumFactors() - self.Value == self.Value


# Create multiple objects and call all methods
Obj1 = Numbers()
print("Is Prime   :", Obj1.ChkPrime())
print("Is Perfect :", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())
print("----------------------------")

Obj2 = Numbers()
print("Is Prime   :", Obj2.ChkPrime())
print("Is Perfect :", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors:", Obj2.SumFactors())
