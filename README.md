# file-content-detector
AI-Powered File Content Type Detection

# Project Overview

This project detects the real content type of a file by analyzing its actual data, not just the file extension.
It helps identify whether a file is a PDF, image, text, audio, video, or other type — even if the file name is misleading.

# LEVEL 1(Completed)
Detect file types using file content (magic numbers / headers) instead of file extensions.

<b>How it Works (Simple)</b><br>
-Read the first few bytes of a file<br>
-Match known file signatures (magic numbers)<br>
-Return the detected file type

<b>Technologies Used-Python</b><br>
-Built-in file handling

<b>Features</b><br>
-Fast detection<br>
-Beginner-friendly<br>
-No AI / ML required<br>
-Accurate for common file types

# LEVEL 2(Completed)
Improve detection using machine learning when rule-based detection fails.

<b>How it Works</b><br>
-Try rule-based detection (magic numbers)<br>
-If unknown:<br>
-Extract features from file<br>
-Use ML model to predict type<br>

<b>Technologies Used</b><br>
-Python<br>
-scikit-learn<br>
-NumPy<br>
-Pandas

<b>Features Used for ML</b><br>
-Byte frequency<br>
-File size<br>
-Entropy<br>
-Text patterns

 <b>Features</b><br>
-Rule-based + ML hybrid system<br>
-Higher accuracy<br>
-Handles unknown or corrupted files<br>
<br>

  
# LEVEL 3(Completed)
Build a high-performance, production-ready file type detection system.

<b>How it Works</b><br>
The system operates on a Fail-Fast, Deep-Inspect hierarchy. Every file uploaded to the API passes through three distinct layers of analysis:<br>
Layer 1: Rule-Based (The Sprint)<br>
Layer 2: Statistical Verification (The Check)<br>
Layer 3: ML/Deep Learning Fallback (The Brain)

<b>Tech Stack</b><br>
-API Framework: FastAPI<br>
-Rule Engine: python-magic<br>
-Machine Learning: PyTorch (Inference) & scikit-learn (Feature extraction)<br>
-Containerization: Docker + Multi-stage builds<br>
-Performance: Uvicorn with uvloop for lightning-fast event loops.<br>

<b>Key Features</b><br>
<b>Performance & Scale</b><br>
-Async I/O: Fully non-blocking architecture allows the API to handle thousands of concurrent requests.<br>
-Batch Processing: Dedicated endpoint to process multiple files in a single multipart request.<br>
-Memory Optimized: Streams files instead of loading them entirely into RAM, allowing for the analysis of GB-sized files on low-resource containers.


 

