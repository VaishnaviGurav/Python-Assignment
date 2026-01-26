Mul = lambda A, B: A * B

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Multiplication of", num1, "and", num2, "is", Mul(num1, num2))

if __name__ == "__main__":
    main()