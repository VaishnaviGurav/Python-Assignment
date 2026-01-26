def DisplayStar(no):
    for i in range(no):
        print("*", end=" ")

def main():
    n = int(input("Enter number: "))
    DisplayStar(n)

if __name__ == "__main__":
    main()
