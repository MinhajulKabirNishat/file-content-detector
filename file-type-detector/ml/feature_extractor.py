import os
import math
from collections import Counter

def calculate_entropy(data):
    counter = Counter(data)
    total = len(data)
    entropy = 0

    for count in counter.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


def extract_features(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    features = []

    # 1. File size
    features.append(len(data))

    # 2. Entropy
    features.append(calculate_entropy(data))

    # 3. Byte frequency (first 256 bytes)
    freq = Counter(data[:256])
    for i in range(256):
        features.append(freq.get(i, 0))

    return features
