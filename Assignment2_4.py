def Sum_factors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter a number: "))
    print("Sum of factors of", num, "is", Sum_factors(num))

if __name__ == "__main__":
    main()