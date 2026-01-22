def SumNatural(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter number: "))
    Result = SumNatural(Value)
    print("Sum of natural numbers is:", Result)

if __name__ == "__main__":
    main()