def CheckPrime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
    
def main():
    number = int(input("Enter a number to check if it is prime: "))
    if CheckPrime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

if __name__ == "__main__":
    main()