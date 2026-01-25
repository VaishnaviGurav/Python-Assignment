is_Even = lambda x: True if x % 2 == 0 else False
def CheckEven(No):
    return is_Even(No)
def main():

    Number = int(input("Enter number: "))
    if CheckEven(Number):
        print(f"{Number} is Even")
    else:
        print(f"{Number} is Odd")

if __name__ == "__main__":
    main()