def CheckNumber1(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    

def main():
    number = float(input("Enter a number: "))
    result = CheckNumber1(number)
    print(f"The number is {result}")

if __name__ == "__main__":
    main()