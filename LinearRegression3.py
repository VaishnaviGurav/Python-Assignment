import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([1,2,3,4,5])
Y = np.array([20000,25000,30000,35000,40000])

# Mean
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Calculate slope (m)
num = sum((X - mean_x) * (Y - mean_y))
den = sum((X - mean_x) ** 2)

m = num / den

# Intercept (c)
c = mean_y - m * mean_x

print("Slope:", m)
print("Intercept:", c)

# Prediction for 6 years experience
x = 6
pred_salary = m*x + c

print("Predicted Salary for 6 Years Experience =", pred_salary)

# Plot graph
plt.scatter(X, Y, color='blue')
plt.plot(X, m*X + c, color='red')

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction using Linear Regression")

plt.show()