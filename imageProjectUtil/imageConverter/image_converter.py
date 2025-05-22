from PIL import Image
from datetime import date
from pathlib import Path

# Configuration
INPUT_DIR = Path("C:/Programs/your_folder/your_subfolder/your_images")
OUTPUT_BASE_DIR = Path("./converted_images")
SUPPORTED_FORMATS = {"jpg", "jpeg", "png", "webp", "bmp", "tiff", "gif"}

INPUT_FORMAT = "jpg"   # Change as needed
OUTPUT_FORMAT = "webp" # Change as needed

# Format today's date
today = date.today()
formatted_date = today.strftime("%d_%m_%Y")
process_dir = OUTPUT_BASE_DIR / formatted_date

# Create folders
temp_dir = process_dir / "temp"
final_dir = process_dir / f"converted_to_{OUTPUT_FORMAT}"
temp_dir.mkdir(parents=True, exist_ok=True)
final_dir.mkdir(parents=True, exist_ok=True)

print(f"[INFO] Starting image conversion on {formatted_date}")
print(f"[INFO] Input directory: {INPUT_DIR}")
print(f"[INFO] Output format: {OUTPUT_FORMAT.upper()}")

# Get all image files
image_files = [file for file in INPUT_DIR.iterdir() if file.suffix[1:].lower() == INPUT_FORMAT.lower()]

if not image_files:
    print("[WARNING] No files found with the specified input format.")
else:
    for image_file in image_files:
        try:
            print(f"\n[PROCESSING] {image_file.name}")
            with Image.open(image_file) as img:
                print(f"  - Original format: {img.format}")
                print(f"  - Mode: {img.mode}")
                print(f"  - Size: {img.size}")

                # Convert image mode if needed
                if img.mode not in ("RGB", "RGBA"):
                    print("  - Converting to RGBA")
                    img = img.convert("RGBA")

                # Save as intermediate format (optional)
                temp_image_path = temp_dir / (image_file.stem + ".png")
                img.save(temp_image_path, format="PNG")
                print(f"  - Saved temp PNG: {temp_image_path.name}")

                # Save in final format
                output_file = final_dir / f"{image_file.stem}.{OUTPUT_FORMAT.lower()}"
                img.save(output_file, format=OUTPUT_FORMAT.upper())
                print(f"  - Converted and saved as {OUTPUT_FORMAT.upper()}: {output_file.name}")

        except Exception as e:
            print(f"[ERROR] Failed to process {image_file.name}: {e}")