from fastapi import FastAPI, UploadFile, File
from core.utils import detect_file

app = FastAPI(title="AI File Type Detector")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI File Type Detector API"}

@app.post("/detect")
async def detect(upload_file: UploadFile = File(...)):
    # Save uploaded file temporarily
    file_location = f"temp_{upload_file.filename}"
    with open(file_location, "wb") as f:
        f.write(await upload_file.read())
    
    # Detect file type
    result = detect_file(file_location)
    
    return {"filename": upload_file.filename, "file_type": result}
