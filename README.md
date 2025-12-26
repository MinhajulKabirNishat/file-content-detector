# file-content-detector
AI-Powered File Content Type Detection

# Project Overview

This project detects the real content type of a file by analyzing its actual data, not just the file extension.
It helps identify whether a file is a PDF, image, text, audio, video, or other type — even if the file name is misleading.

# LEVEL 1(Completed)
Detect file types using file content (magic numbers / headers) instead of file extensions.

# How it Works (Simple)
-Read the first few bytes of a file
-Match known file signatures (magic numbers)
-Return the detected file type

# Technologies Used-Python
-Built-in file handling

# Features
-Fast detection
-Beginner-friendly
-No AI / ML required
-Accurate for common file types

# LEVEL 2(Completed)
Improve detection using machine learning when rule-based detection fails.

# How it Works
-Try rule-based detection (magic numbers)
-If unknown:
-Extract features from file
-Use ML model to predict type

# Technologies Used
-Python
-scikit-learn
-NumPy
-Pandas

# Features Used for ML
-Byte frequency
-File size
-Entropy
-Text patterns

# Features
-Rule-based + ML hybrid system
-Higher accuracy
-Handles unknown or corrupted files


# LEVEL 3(Completed)
Build a high-performance, production-ready file type detection system.

# How it Works
The system operates on a Fail-Fast, Deep-Inspect hierarchy. Every file uploaded to the API passes through three distinct layers of analysis:
Layer 1: Rule-Based (The Sprint)
Layer 2: Statistical Verification (The Check)
Layer 3: ML/Deep Learning Fallback (The Brain)

# Tech Stack
-API Framework: FastAPI
-Rule Engine: python-magic
-Machine Learning: PyTorch (Inference) & scikit-learn (Feature extraction)
-Containerization: Docker + Multi-stage builds
-Performance: Uvicorn with uvloop for lightning-fast event loops.

# Key Features
# Performance & Scale
-Async I/O: Fully non-blocking architecture allows the API to handle thousands of concurrent requests.
-Batch Processing: Dedicated endpoint to process multiple files in a single multipart request.
-Memory Optimized: Streams files instead of loading them entirely into RAM, allowing for the analysis of GB-sized files on low-resource containers.


 

