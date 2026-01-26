def MinList(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

def main():
    lst = []
    n = int(input("Enter number of elements in the list: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)
    print("Minimum value in the list is:", MinList(lst))

if __name__ == "__main__":
    main()