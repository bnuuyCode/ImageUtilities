# Validate Product Images

This Python script checks whether image files in a folder match a list of product image names provided in an Excel spreadsheet. If a match is found, the image is moved to a destination folder.

## 📌 Use Case

Imagine you have a folder full of product images (e.g., `.webp` files) and an Excel file listing valid product image filenames. This script helps you filter out the correct images by moving only the matching files to a target folder.

## ✅ Features

- Reads a list of valid image names from an Excel spreadsheet.
- Moves matching images to a specific folder.
- Skips non-matching files.
- Handles errors gracefully (e.g., missing files or permission issues).
- Uses modern Python features (`pathlib`, `pandas`, `shutil`).

## 🧩 Requirements

- Python 3.7+
- pandas
- openpyxl

Install dependencies using:

```bash
pip install pandas openpyxl
```

## 📁 Folder Structure Example

```
product_image_validator/
│
├── validate_product_images.py
├── product_list.xlsx              # Excel with a 'fotoWebp' column
├── /webp_400x400/                 # Source folder with image files
└── /matched_images/              # Destination folder for matched files
```

## 📄 Excel File Format

The Excel file should contain a column named `fotoWebp` with the exact filenames (e.g., `image123.webp`) you expect to match in the image folder.

| fotoWebp         |
|------------------|
| product1.webp    |
| product2.webp    |
| product3.webp    |

## 📷 Supported Image Formats
This script works with any image file format, such as:

- .webp

- .jpg

- .jpeg

- .png

- .gif

- ...and any other format

However, there's one important detail:

>The filenames listed in the `fotoWebp` column of the Excel file must exactly match the actual image filenames in the folder — including the file extension (e.g., `product1.webp`, `product2.jpg`, etc.).

## 🚀 How to Use

1. Open the script and make sure the folders are in place as shown above.
2. Run the script:

```bash
python validate_product_images.py
```

3. The script will print the names of moved files and a total count at the end.

## 🔐 Notes

- The script only moves files that exactly match the names in the Excel sheet.
- Filenames are case-sensitive. Ensure consistent formatting.
- Existing files in the destination folder will be overwritten if names match.

## 🛠️ Optional Improvements

- Add logging to track processed files.
- Build a user-friendly GUI.
- Add CLI support to pass paths as arguments.

---
✧ made by bnnuy 🐇 in bnnuy code style 
            ૮꒰ ˶• ༝ •˶꒱ა ♡