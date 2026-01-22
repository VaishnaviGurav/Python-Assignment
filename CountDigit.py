def CountDigit(number):
    if number == 0:
        return 1
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count

def main():
    num = int(input("Enter a number: "))
    result = CountDigit(num)
    print("Number of digits:", result)

if __name__ == "__main__":
    main()