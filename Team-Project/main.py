from pathlib import Path
from team_project import get_file_category
from analyzer import create_folders, confirm, move_files, print_summary

def main():
    # Papka manzilini to'g'ridan-to'g'ri shu yerga yozib qo'yamiz (input yo'q)
    folder = Path("practice_folder") # Kerakli papka nomini shu yerga yozasiz

    if not folder.exists() or not folder.is_dir():
        print(f"Xato: '{folder}' papkasi mavjud emas!")
        return

    # Fayllarni tahlil qilib reja tuzamiz
    plan = []
    for file_path in folder.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            category = get_file_category(extension)
            plan.append((file_path, category))

    if not plan:
        print("Diqqat: Tanlangan papka bo'sh!")
        return

    print(f"Topildi: {len(plan)} ta fayl saralashga tayyor.")

    # Tasdiqlatib va xavfsiz ko'chiramiz
    if confirm():
        create_folders(folder, plan)
        moved, skipped = move_files(folder, plan)
        print_summary(moved, skipped)
    else:
        print("Cancelled. Nothing was changed.")

if __name__ == "__main__":
    main()