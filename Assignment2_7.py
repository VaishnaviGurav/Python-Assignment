def NumberPattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def main():
    n = int(input("Enter number : "))
    NumberPattern(n)

if __name__ == "__main__":
    main()