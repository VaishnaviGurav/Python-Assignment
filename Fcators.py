def Fcators(n):

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
            

def main():
    num = int(input("Enter a number: "))
    Fcators(num)

if __name__ == "__main__":
    main()