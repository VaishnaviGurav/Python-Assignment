def Cube(Number):
    return Number * Number * Number

def main():
    No = int(input("Enter number: "))
    Result = Cube(No)
    print("Cube is: ",Result)

if __name__ == "main":
    main()