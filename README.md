
# Image Processing Scripts

This repository contains three standalone Python scripts to simplify common image processing tasks, especially useful for batch operations and automating workflows.

---

## 1. Image Resizer Script

Resizes images based on maximum width/height or target file size, preserving the aspect ratio.

### Features
- Resize by max dimensions (width or height).
- Resize by max file size (KB or MB).
- Preserves image aspect ratio.

### Usage Example

```bash
python image_resizer.py --input_folder ./images --output_folder ./resized --max_width 800 --max_height 600
```

Or resize by file size:

```bash
python image_resizer.py --input_folder ./images --output_folder ./resized --max_size_kb 200
```

---

## 2. Image Converter Script

Converts images between supported formats (JPG, PNG, WEBP, etc.) using the Pillow library. Automatically organizes converted images into folders by conversion date.

### Features
- Supports multiple source and target formats.
- Auto-organizes outputs into date-based folders (YYYY-MM-DD).

### Usage Example

```bash
python image_converter.py --input_folder ./images --output_folder ./converted --target_format png
```

---

## 3. Validate Product Images

Checks whether image files in a folder match product image names listed in an Excel spreadsheet. Matching images are moved to a specified destination folder.

### Features
- Reads product image names from an Excel file.
- Moves matched images to a destination folder for easy organization.

### Usage Example

```bash
python validate_product_images.py --images_folder ./product_images --excel_file ./products.xlsx --destination_folder ./validated_images
```

---

## Requirements

- Python 3.x
- Pillow
- pandas
- openpyxl

Install dependencies:

```bash
pip install Pillow pandas openpyxl
```

---

## Notes

- Adjust paths and parameters as needed for your environment.
- Each script is independent; run them separately as needed.
- Scripts can be extended with additional command-line options if desired.

---
✧ made by bnnuy 🐇 in bnnuy code style ૮꒰ ˶• ༝ •˶꒱ა ♡
