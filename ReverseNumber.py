def ReverseNumber(number):
    reversed_num = 0
    while number != 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    return reversed_num

def main():
    num = int(input("Enter a number: "))
    result = ReverseNumber(num)
    print("Reversed Number:", result)

if __name__ == "__main__":
    main()