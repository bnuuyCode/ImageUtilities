import pandas as pd
from pathlib import Path
import shutil
import sys

# === INITIAL CONFIGURATION ===
images_folder = Path("webp_400x400")
excel_file = Path("product_list.xlsx")
destination_folder = Path("matched_images")

# Create required folders if they don't exist
images_folder.mkdir(parents=True, exist_ok=True)
destination_folder.mkdir(parents=True, exist_ok=True)

# === CHECK FILE AND FOLDER EXISTENCE ===
if not excel_file.exists():
    print(f"[ERROR] Excel file not found: {excel_file.resolve()}")
    sys.exit(1)

if not any(images_folder.iterdir()):
    print(f"[WARNING] No images found in folder: {images_folder.resolve()}")

# === READ EXCEL FILE ===
try:
    df = pd.read_excel(excel_file)
    expected_images = set(df['fotoWebp'].dropna().astype(str))
except Exception as e:
    print(f"[ERROR] Failed to read the Excel file: {e}")
    sys.exit(1)

# === PROCESS IMAGES ===
moved_images = 0
for image_path in images_folder.iterdir():
    if image_path.is_file():
        if image_path.name in expected_images:
            try:
                shutil.move(str(image_path), str(destination_folder / image_path.name))
                moved_images += 1
                print(f"Moved: {image_path.name}")
            except Exception as e:
                print(f"Error moving {image_path.name}: {e}")

print(f"\nTotal images moved: {moved_images}")