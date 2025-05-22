
# 🖼️ Image Resizer Script

A simple Python script to resize images based on maximum dimensions or file size, while preserving aspect ratio.

## 📌 Features

- Automatically resizes an image if:
  - It exceeds a specified width or height.
  - It exceeds a specified file size (in bytes).
- Maintains the original image's aspect ratio.
- Optional logging to the console for feedback.
- Easy to integrate into other Python projects.

## 🧰 Requirements

- Python 3.7 or higher
- Pillow (PIL fork)

Install dependencies using pip:

```bash
pip install pillow
```

## 🚀 Usage

```python
from PIL import Image
from resize_image import resize_image_if_needed

image_path = "path/to/image.jpg"
max_width = 800
max_height = 600
max_byte_size = 500_000  # 500 KB

# Open the image
with Image.open(image_path) as img:
    resized_image = resize_image_if_needed(
        image=img,
        image_path=image_path,
        max_width=max_width,
        max_height=max_height,
        max_byte_size=max_byte_size,
        verbose=True
    )
```

## 📝 Function Documentation

```python
def resize_image_if_needed(
    image: Image.Image,
    image_path: str,
    max_width: int,
    max_height: int,
    max_byte_size: int,
    verbose: Optional[bool] = True
) -> Image.Image:
    """
    Resize an image if it exceeds the specified dimensions or file size.

    Args:
        image (Image.Image): The image object.
        image_path (str): Path to the original image file.
        max_width (int): Maximum allowed width in pixels.
        max_height (int): Maximum allowed height in pixels.
        max_byte_size (int): Maximum allowed file size in bytes.
        verbose (bool, optional): If True, prints log messages. Defaults to True.

    Returns:
        Image.Image: The resized image (or the original if no resizing was necessary).
    """
```

## 📂 Project Structure

```
your_project/
│
├── resize_image.py       # Contains the resize_image_if_needed function
├── example_script.py     # (Optional) Script demonstrating usage
└── README.md             # This file
```
✧ made by bnnuy 🐇 in bnnuy code style ૮꒰ ˶• ༝ •˶꒱ა ♡