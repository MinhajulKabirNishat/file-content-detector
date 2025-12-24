import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import extract_features

DATASET_DIR = "../dataset"

X = []
y = []

for label in os.listdir(DATASET_DIR):
    folder = os.path.join(DATASET_DIR, label)

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        features = extract_features(path)
        X.append(features)
        y.append(label)

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
