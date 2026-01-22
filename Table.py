def Table(Number):
    for i in range(1, 11):
        print(Number * i, end=' ')

def main():
        No = int(input("Enter number: "))
        Table(No)

if __name__ == "__main__":
     main()