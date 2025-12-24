import sys
import pickle
from rules.magic_detector import detect_by_magic
from ml.feature_extractor import extract_features

with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)


def detect_file(file_path):
    result = detect_by_magic(file_path)

    if result != "unknown":
        return f"Detected by rules: {result.upper()}"

    features = extract_features(file_path)
    prediction = model.predict([features])[0]
    return f"Detected by ML: {prediction.upper()}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
    else:
        print(detect_file(sys.argv[1]))
