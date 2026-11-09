from pathlib import Path
from team_project import get_file_category
from analyzer import create_folders, confirm, move_files, print_summary


def main():
    # Papka yo'lini foydalanuvchidan so'raymiz
    folder = Path(input("Papka yo'lini kiriting: ").strip().strip('"'))

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

    # Oldindan ko'rish (preview)
    print(f"Topildi: {len(plan)} ta fayl saralashga tayyor.")
    for file_path, category in plan:
        print(f"{file_path.name} -> {category}/")

    # Tasdiqlatib va xavfsiz ko'chiramiz
    if confirm():
        create_folders(folder, plan)
        moved, skipped = move_files(folder, plan)
        print_summary(moved, skipped)
    else:
        print("Cancelled. Nothing was changed.")


if __name__ == "__main__":
    main()