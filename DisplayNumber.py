def Number(Num):
    
    for i in range(10,0,-1):
        print(i, end=" ")

def main():
    Value = int(input("Enter a number: "))
    Number(Value)

if __name__ == "__main__":
    main()