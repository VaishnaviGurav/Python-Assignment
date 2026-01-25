MinNumber = lambda a, b: a if a < b else b

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Result = MinNumber(Num1, Num2)
    print("Minimum number is:", Result)

if __name__ == "__main__":
    main()