def CountNumberOfDigits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

def main():
    number = int(input("Enter a number to count its digits: "))
    digits = CountNumberOfDigits(number)
    print("Number of digits in", number, "is", digits)

if __name__ == "__main__":
    main()