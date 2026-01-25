Largest = lambda x, y, z: x if x > y and x > z else (y if y > z else z)

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Num3 = int(input("Enter third number: "))
    Result = Largest(Num1, Num2, Num3)
    print("Largest number is:", Result)

if __name__ == "__main__":
    main()