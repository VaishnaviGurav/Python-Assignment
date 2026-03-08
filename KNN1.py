import math

# Dataset
dataset = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# Accept input
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

distances = []

# Compute Euclidean distance
for point in dataset:
    name, x1, y1, label = point
    distance = math.sqrt((x - x1)**2 + (y - y1)**2)
    distances.append((name, distance, label))

# Sort distances
distances.sort(key=lambda d: d[1])

print("\nNearest Neighbors:")
for i in range(3):
    print(distances[i][0], "- Distance:", round(distances[i][1], 2))

# Select K=3 nearest neighbors
k_neighbors = distances[:3]

# Count labels
label_count = {}
for neighbor in k_neighbors:
    label = neighbor[2]
    if label in label_count:
        label_count[label] += 1
    else:
        label_count[label] = 1

# Predict label
predicted_label = max(label_count, key=label_count.get)

print("\nPredicted Class:", predicted_label)