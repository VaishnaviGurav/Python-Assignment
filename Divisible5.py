def Divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False
    

def main():
    number = int(input("Enter a number: "))
    if Divisible(number):
        print("numberis divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()