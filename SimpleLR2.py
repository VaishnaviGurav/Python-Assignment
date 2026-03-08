X = [1,2,3,4,5]
Y = [3,4,2,4,5]

m = 0.4
c = 2.4

Y_pred = []

# Predict values
for x in X:
    y = m*x + c
    Y_pred.append(y)

print("Predicted values:",Y_pred)

# MSE
n = len(Y)
error = 0

for i in range(n):
    error += (Y[i] - Y_pred[i])**2

MSE = error/n
print("MSE =",round(MSE,2))


# R2 Score
mean_y = sum(Y)/n

ss_total = 0
ss_res = 0

for i in range(n):
    ss_total += (Y[i] - mean_y)**2
    ss_res += (Y[i] - Y_pred[i])**2

r2 = 1 - (ss_res/ss_total)

print("R2 Score =",round(r2,2))