Power = lambda X : X * X

def main():
    num = int(input("Enter a number to find its square: "))
    print("Square of", num, "is", Power(num))

if __name__ == "__main__":
    main()