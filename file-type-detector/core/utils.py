from core.rules import detect_by_magic
from core.ml_model import predict_file_type

def detect_file(file_path):
    result = detect_by_magic(file_path)
    if result != "unknown":
        return f"Detected by rules: {result.upper()}"
    else:
        prediction = predict_file_type(file_path)
        return f"Detected by ML: {prediction.upper()}"
