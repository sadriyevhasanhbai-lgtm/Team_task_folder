from pathlib import Path
import shutil


def create_folders(folder, plan):
    names = set()
    for src, dest_name in plan:
        names.add(dest_name)

    for name in names:
        (folder / name).mkdir(exist_ok=True)


def confirm():
    answer = input("Continue? (y/n): ").strip().lower()
    return answer == "y"


def move_files(folder, plan):
    moved = 0
    skipped = 0

    for src, dest_name in plan:
        target = folder / dest_name / src.name

        if target.exists():
            print(f"{src.name} skipped: already exists in {dest_name}")
            skipped += 1
        else:
            shutil.move(str(src), str(target))
            moved += 1

    return moved, skipped


def print_summary(moved, skipped):
    print(f"Done. Moved: {moved}, Skipped: {skipped}")


# Runs only when this file is executed directly (for testing)
if __name__ == "__main__":
    folder = Path("practice_folder")
    folder.mkdir(exist_ok=True)

   # Create sample files for testing
    (folder / "a.jpg").write_text("test")
    (folder / "b.pdf").write_text("test")
    (folder / "c.csv").write_text("test")

    # Write the plan by hand in place of Mentee 1's code
    plan = [
        (folder / "a.jpg", "Images"),
        (folder / "b.pdf", "Documents"),
        (folder / "c.csv", "Other"),
    ]

    if confirm():
        create_folders(folder, plan)
        moved, skipped = move_files(folder, plan)
        print_summary(moved, skipped)
    else:
        print("Cancelled. Nothing was changed.")