is_Odd = lambda x: True if x % 2 != 0 else False

def CheckOdd(No):
    return is_Odd(No)

def main():

    Number = int(input("Enter number: "))
    if CheckOdd(Number):
        print(f"{Number} is Odd")
    else:
        print(f"{Number} is Even")

if __name__ == "__main__":
    main()