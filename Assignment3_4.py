def FrequencyList(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count

def main():
    lst = []
    n = int(input("Enter number of elements in the list: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)
    value = int(input("Enter the value to find its frequency: "))
    frequency = FrequencyList(lst, value)
    print(f"Frequency of {value} in the list is:", frequency)

if __name__ == "__main__":
    main()