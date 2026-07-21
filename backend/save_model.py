import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import pickle


# Load dataset

data = pd.read_csv("disaster_dataset.csv")


# Input features

X = data[
[
"temperature",
"humidity",
"rainfall",
"wind_speed",
"pressure"
]
]


# Output

y = data["flood_risk"]


# Train model

model = RandomForestClassifier()

model.fit(X, y)


# Save model

with open("flood_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model saved successfully!")