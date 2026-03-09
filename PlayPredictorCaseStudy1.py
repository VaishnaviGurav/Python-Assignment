import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load Dataset
data = pd.read_csv("PlayPredictor.csv")

print("Dataset:")
print(data)

# Step 2: Data Preprocessing
le = LabelEncoder()

data['Weather'] = le.fit_transform(data['Weather'])
data['Temperature'] = le.fit_transform(data['Temperature'])
data['Play'] = le.fit_transform(data['Play'])

print("\nEncoded Dataset:")
print(data)

# Step 3: Separate Input and Output
X = data[['Weather','Temperature']]
Y = data['Play']

# Step 4: Split Dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

# Step 5: Train Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

# Step 6: Prediction
prediction = model.predict(X_test)

# Step 7: Accuracy
accuracy = accuracy_score(Y_test, prediction)

print("\nPredicted Output:", prediction)
print("Accuracy:", accuracy * 100)