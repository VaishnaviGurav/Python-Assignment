def AreaCircle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

def main():
    r = float(input("Enter radius of circle: "))
    area = AreaCircle(r)
    print("Area of circle is:", area)

if __name__ == "__main__":
    main()