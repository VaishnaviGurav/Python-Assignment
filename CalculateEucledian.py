import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[25,20000],
                 [30,40000]])

# Distance before scaling
distance_before = np.linalg.norm(data[0] - data[1])

# Feature scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(data)

# Distance after scaling
distance_after = np.linalg.norm(scaled[0] - scaled[1])

print("Distance before scaling:", distance_before)
print("Distance after scaling:", distance_after)