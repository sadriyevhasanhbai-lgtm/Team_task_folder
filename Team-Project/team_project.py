import os
import shutil

CATEGORIES = {
    # Images (Rasmlar)
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", 
    ".gif": "Images", ".svg": "Images", ".webp": "Images",

    # Documents (Hujjatlar)
    ".pdf": "Documents", ".docx": "Documents", ".doc": "Documents",
    ".txt": "Documents", ".xlsx": "Documents", ".xls": "Documents",
    ".pptx": "Documents", ".csv": "Documents",

    # Archives (Arxivlar)
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",

    # Media (Musiqa va Videolar)
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio",
    ".mp4": "Video", ".mkv": "Video", ".avi": "Video", ".mov": "Video",

    # Code & Development (Dasturlash)
    ".py": "Code", ".js": "Code", ".html": "Code", ".css": "Code",
    ".json": "Code", ".sql": "Code", ".cpp": "Code", ".java": "Code",

    # Executables & Programs (Dasturlar)
    ".exe": "Executables", ".msi": "Executables", ".dmg": "Executables"
}


def organize_file():
    path = input("Enter path: ")

    if not os.path.exists(path) or not os.path.isdir(path):
        print("Xato: Ko'rsatilgan yo'l mavjud emas yoki bu papka emas!")
        return  
    
    files = os.listdir(path)

    if not files:
        print("Diqqat: Tanlangan papka bo'sh!")
        return

    for file in files:
        file_path = os.path.join(path, file)

        # Agar bu papkaning o'zi bo'lsa, tashlab o'tamiz
        if os.path.isdir(file_path):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        # XATOLIK TO'G'RILANDI: CATEGORIES o'rniga category o'zgaruvchisi ishlatildi
        category = get_file_category(extension)

        # --- SHU YERDAN PASTGA QOLGAN QISMNI QO'SHISH KERAK EDI ---

        # 1. Kategoriya papkasi yo'lini hosil qilamiz (masalan: path/Images)
        category_dir = os.path.join(path, category)

        # 2. Agar bunday papka yo'q bo'lsa, uni yaratamiz
        os.makedirs(category_dir, exist_ok=True)

        # 3. Faylning yangi boradigan manzili
        target_path = os.path.join(category_dir, file)

        # 4. Xavfsizlik qoidasi: Agar o'sha papkada bunday fayl allaqachon bo'lsa
        if os.path.exists(target_path):
            print(f"O'tkazilmadi: '{file}' allaqachon '{category}' papkasida mavjud.")
            continue

        # 5. Faylni o'z papkasiga ko'chiramiz
        shutil.move(file_path, target_path)
        print(f"Ko'chirildi: {file} ---> {category} papkasiga")



def get_file_category(extension):
    # Rasmlar uchun shartlar
    if extension in [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"]:
        return "Images"

    # Hujjatlar uchun shartlar
    elif extension in [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv"]:
        return "Documents"

    # Arxivlar uchun shartlar
    elif extension in [".zip", ".rar", ".7z", ".tar", ".gz"]:
        return "Archives"
    
    # Musiqa va videolar uchun shartlar
    elif extension in [".mp3", ".wav", ".flac", ".mp4", ".mkv", ".avi", ".mov"]:
        return "Media"
    
    # Dasturlash kodlari uchun shartlar
    elif extension in [".py", ".js", ".html", ".css", ".json", ".sql", ".cpp", ".java"]:
        return "Code"

    # Dasturlar uchun shartlar
    elif extension in [".exe", ".msi", ".dmg"]:
        return "Executables"

    else:
        return "Other"


if __name__ == "__main__":
    organize_file()