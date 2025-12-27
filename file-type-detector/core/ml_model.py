import pickle
from ml.feature_extractor import extract_features

# Load trained ML model
with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_file_type(file_path):
    features = extract_features(file_path)
    prediction = model.predict([features])[0]
    return prediction
