import sys

def detect_file_type(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)

    # PDF
    if header.startswith(b"%PDF"):
        return "PDF Document"

    # PNG
    elif header.startswith(b"\x89PNG"):
        return "PNG Image"

    # JPG
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "JPG Image"

    # TXT (basic check)
    try:
        header.decode("utf-8")
        return "Text File"
    except:
        pass

    return "Unknown File Type"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python detector.py <file_path>")
    else:
        file_path = sys.argv[1]
        result = detect_file_type(file_path)
        print("Detected File Type:", result)
