from functools import reduce

data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter: >=70 and <=90
filtered = list(filter(lambda x: 70 <= x <= 90, data))
print("List after filter =", filtered)

# Map: +10
mapped = list(map(lambda x: x + 10, filtered))
print("List after map =", mapped)

# Reduce: product
result = reduce(lambda a, b: a * b, mapped)
print("Output of reduce =", result)
