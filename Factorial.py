def Factorial(No):
    if No == 0:
        return 1
    else:
        return No * Factorial(No - 1)
    
def main():
    Value = int(input("Enter number: "))
    Result = Factorial(Value)
    print("Factorial is:", Result)

if __name__ == "__main__":
    main()