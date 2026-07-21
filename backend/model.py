import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


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


# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)


# Create model

model = RandomForestClassifier()


# Train

model.fit(
    X_train,
    y_train
)


# Test

prediction = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    prediction
)


print("Accuracy:", accuracy)