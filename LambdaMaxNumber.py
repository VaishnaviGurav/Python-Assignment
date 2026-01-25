MaxNumber = lambda a, b: a if a > b else b

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Result = MaxNumber(Num1, Num2)
    print("Maximum number is:", Result)

if __name__ == "__main__":
    main()