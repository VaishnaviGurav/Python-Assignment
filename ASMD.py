def Addition(a, b):
    return a + b
def Subtraction(a, b):
    return a - b
def Multiplication(a, b):
    return a * b
def Division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Addition:", Addition(num1, num2))
    print("Subtraction:", Subtraction(num1, num2))
    print("Multiplication:", Multiplication(num1, num2))
    print("Division:", Division(num1, num2))

if __name__ == "__main__":
    main()