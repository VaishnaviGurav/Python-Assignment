def AreaRectangle(length, breadth):
    return length * breadth

def main():
    l = float(input("Enter length of rectangle: "))
    b = float(input("Enter breadth of rectangle: "))
    area = AreaRectangle(l, b)
    print("Area of rectangle is:", area)

if __name__ == "__main__":
    main()