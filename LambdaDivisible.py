Divisible = lambda x: True if x % 5 == 0 else False

def CheckDivisible(No):
    return Divisible(No)

def main():
    Number = int(input("Enter number: "))
    if CheckDivisible(Number):
        print(f"{Number} is Divisible by 5")
    else:
        print(f"{Number} is Not Divisible by 5")

if __name__ == "__main__":
    main()