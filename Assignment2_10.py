def Sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

def main():
    num = int(input("Enter a number to sum its digits: "))
    print("Sum of digits in", num, "is", Sum_digits(num))

if __name__ == "__main__":
    main()