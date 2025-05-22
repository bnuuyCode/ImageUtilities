import os
from PIL import Image
from typing import Optional


def resize_image_if_needed(
    image: Image.Image,
    image_path: str,
    max_width: int,
    max_height: int,
    max_byte_size: int,
    verbose: Optional[bool] = True
) -> Image.Image:

    original_width, original_height = image.size
    image_name = os.path.basename(image_path)
    file_size = os.path.getsize(image_path)

    if verbose:
        print(f"Image '{image_name}' has dimensions {original_width}x{original_height} and size {file_size} bytes.")

    # Check if resizing is necessary
    if original_width > max_width or original_height > max_height or file_size > max_byte_size:
        # Calculate new size maintaining aspect ratio
        aspect_ratio = original_width / original_height
        if aspect_ratio > 1:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)

        image = image.copy()  # Avoid modifying original image
        image.thumbnail((new_width, new_height))

        if verbose:
            print(f"Image '{image_name}' resized to {new_width}x{new_height}.")
    else:
        if verbose:
            print(f"Image '{image_name}' does not need resizing.")

    return image