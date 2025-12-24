# file-content-detector
AI-Powered File Content Type Detection

# Project Overview

This project detects the real content type of a file by analyzing its actual data, not just the file extension.
It helps identify whether a file is a PDF, image, text, audio, video, or other type — even if the file name is misleading.

🟢 BEGINNER LEVEL

Detect file types using file content (magic numbers / headers) instead of file extensions.

# How it Works (Simple)

-Read the first few bytes of a file

-Match known file signatures (magic numbers)

-Return the detected file type

🛠 Technologies Used

-Python

-Built-in file handling

📂 Project Structure
file-type-detector/
│
├── detector.py
├── samples/
│   ├── sample.pdf
│   ├── image.png
│   └── text.txt
└── README.md

▶ How to Run
python detector.py samples/sample.pdf

# Features

-Fast detection

-Beginner-friendly

-No AI / ML required

-Accurate for common file types

📌 Example Output
Detected File Type: PDF Document

🟡 INTERMEDIATE LEVEL 

Improve detection using machine learning when rule-based detection fails.

# How it Works

-Try rule-based detection (magic numbers)

-If unknown:

-Extract features from file

-Use ML model to predict type

🛠 Technologies Used

-Python

-scikit-learn

-NumPy

-Pandas

📂 Project Structure
file-type-detector/
│
├── rules/
│   └── magic_detector.py
├── ml/
│   ├── feature_extractor.py
│   ├── train_model.py
│   └── model.pkl
├── dataset/
│   ├── pdf/
│   ├── png/
│   ├── jpg/
│   └── txt/
├── main.py
└── README.md

🧪 Features Used for ML

-Byte frequency

-File size

-Entropy

-Text patterns

▶ How to Run
python main.py samples/unknown_file

# Features

-Rule-based + ML hybrid system

-Higher accuracy

-Handles unknown or corrupted files

🔴 ADVANCED LEVEL (Coming Soon)

Build a high-performance, production-ready file type detection system.

