def ChkNumber(Number):
    if Number % 2 == 0:
        return True
    else:
        return False

def even(Num):
    return Num % 2 == 0

def odd(Num):
    return Num % 2 != 0

def main():
        Num = int(input("Enter a number: "))
        if even(Num):
            print(f"{Num} is Even")
        else:

            print(f"{Num} is Odd")
if __name__ == "__main__":
     main()