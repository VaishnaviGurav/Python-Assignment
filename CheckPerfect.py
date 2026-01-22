def CheckPerfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def main():
    number = int(input("Enter a number: "))
    if CheckPerfect(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")