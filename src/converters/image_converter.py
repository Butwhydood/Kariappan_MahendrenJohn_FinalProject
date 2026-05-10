import os
from PIL import Image


"""
Module for image file conversions.

This module provides functions to convert images between various formats.
"""

def convert_image(input_file, output_file):
    """
    Convert an image file to another format.

    Args:
        input_file (str): Path to the input image file.
        output_file (str): Path to the output image file.
    """
    with Image.open(input_file) as img:
        if img.mode not in ("RGB", "LA"):
            img = img.convert("RGB")
        img.save(output_file)

# Usage example for convert_image:
# convert_image('input.jpg', 'output.png')
# Converts the input image file (JPG) to another format (PNG) and saves it as output.png.