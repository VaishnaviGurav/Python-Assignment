def AdditionList(lst):
    result = 0
    for num in lst:
        result += num
    return result

def main():
    lst = []
    n = int(input("Enter number of elements in the list: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)
    print("Sum of the list is:", AdditionList(lst))

if __name__ == "__main__":
    main()