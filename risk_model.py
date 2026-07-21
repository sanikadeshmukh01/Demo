import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier


# Load dataset

data = pd.read_csv("disaster_dataset.csv")


# Input

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

y = data["risk_level"]


# Create model

model = RandomForestClassifier()


# Train

model.fit(X,y)


# Save model

with open("risk_model.pkl","wb") as file:
    pickle.dump(model,file)


print("Risk model trained successfully!")