def detect_by_magic(file_path):
    with open(file_path, "rb") as f:
        header = f.read(8)

    if header.startswith(b"%PDF"):
        return "pdf"
    elif header.startswith(b"\x89PNG"):
        return "png"
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "jpg"
    try:
        header.decode("utf-8")
        return "txt"
    except:
        pass
    return "unknown"
    