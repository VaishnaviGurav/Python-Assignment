def Numbers1toN(n):
    for i in range(1, n + 1):
        print(i, end=' ')

def main():
    num = int(input("Enter a number: "))
    Numbers1toN(num)

if __name__ == "__main__":
    main()