import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Dummy data
X = np.array([[1000, 2, 2], [1500, 3, 3], [2000, 4, 4]])
y = np.array([5000000, 7500000, 10000000])

# Train a simple model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
