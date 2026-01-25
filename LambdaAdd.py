Add = lambda x, y: x + y

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Result = Add(Num1, Num2)
    print("Addition is:", Result)

if __name__ == "__main__":
    main()