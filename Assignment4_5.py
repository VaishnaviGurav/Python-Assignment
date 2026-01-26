from functools import reduce

# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Input list
data = [2, 70, 11, 10, 17, 23, 31, 77]
print("Input List =", data)

# Filter: only prime numbers
filtered = list(filter(is_prime, data))
print("List after filter =", filtered)

# Map: multiply each by 2
mapped = list(map(lambda x: x * 2, filtered))
print("List after map =", mapped)

# Reduce: find maximum
result = reduce(lambda a, b: a if a > b else b, mapped)
print("Output of reduce =", result)
