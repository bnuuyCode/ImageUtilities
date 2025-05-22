# Image Converter Script

This Python script allows you to convert image files from **any supported format to any other**, such as `JPG → PNG`, `PNG → WEBP`, etc.  
It uses the [Pillow](https://python-pillow.org) library and automatically organizes the converted images into folders by date.

---

## 🧰 Features

- Converts between multiple image formats (e.g., JPG, PNG, WEBP, BMP, TIFF, GIF).
- Automatically creates output folders based on the current date.
- Logs image details (format, size, mode).
- Handles image mode conversion (e.g., to RGBA) when necessary.
- Skips unsupported or incompatible files.
- Modern and readable codebase using `pathlib` and best practices.

---

## 📦 Requirements

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)

Install the required package:

```bash
pip install pillow
```

---

## 🚀 How to Use

1. **Set your input directory** in the script:
   ```python
   INPUT_DIR = Path("C:/Programs/your_folder/your_subfolder/your_images")
   ```

2. **Choose input and output formats**:
   ```python
   INPUT_FORMAT = "jpg"      # or "png", "webp", etc.
   OUTPUT_FORMAT = "webp"    # target format
   ```

3. **Run the script**:
   ```bash
   python image_converter.py
   ```

4. **Find your converted images** inside:
   ```
   ./converted_images/<dd_mm_yyyy>/converted_to_<format>/
   ```

---

## 📂 Folder Structure

```
converted_images/
└── 22_05_2025/
    ├── temp/
    │   └── image1.png
    └── converted_to_webp/
        └── image1.webp
```

---

## 📝 Notes

- Only files matching the input format are processed.
- Intermediate PNGs are saved to a temporary folder (optional for further processing).
- Errors during image conversion are logged but do not interrupt the process.

---

## 🧠 Tip

You can easily modify the script to support bulk conversion from **multiple input formats** if needed.

---

✧ made by bnnuy 🐇 in bnnuy code style ૮꒰ ˶• ༝ •˶꒱ა ♡