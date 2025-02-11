import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = np.array([
    [25, 1, 0], [30, 0, 2], [40, 1, 1], [20, 0, 0], [35, 1, 2], 
    [50, 0, 1], [23, 1, 0], [27, 0, 2], [29, 1, 1], [33, 0, 0]
])

# 1 = Likes Coffee, 0 = Likes Tea
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
