#!/usr/bin/env python3


import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw

def ensure_image_source_exists(image_source):
    if not Path(image_source).is_file():
        print(f"Error: The file '{image_source}' does not exist.")
        sys.exit(1)

def resize_and_save(image, output_path, size):
    resized_image = image.resize((size, size), Image.LANCZOS)
    resized_image.save(output_path, "PNG")

def generate_images(image_source, spec_list, suffix):
    with Image.open(image_source) as img:
        for size in spec_list:
            size = int(size)
            output_path = Path(f"icon-{suffix}-{size}.png")
            print(f"### Generating image: {suffix} {size}x{size}, file: {output_path}")

            if suffix == "round":
                mask = Image.new("L", (size, size), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, size, size), fill=255)

                resized_image = img.resize((size, size), Image.LANCZOS).convert("RGBA")
                output = Image.new("RGBA", (size, size))
                output.paste(resized_image, (0, 0), mask)
                output.save(output_path, "PNG")
            else:
                resize_and_save(img, output_path, size)

def main():
    # Ask the user for the image source
    image_source = input("Please provide the path to the image file (JPG, PNG, etc.): ").strip()

    ensure_image_source_exists(image_source)

    android_spec_list = [48, 72, 96, 144, 192, 320, 480, 640, 960, 1280]
    adaptive_spec_list = [108, 162, 216, 324, 432]

    # Generate square images
    generate_images(image_source, android_spec_list, "square")

    # Generate round images
    generate_images(image_source, android_spec_list, "round")

    # Generate adaptive images
    generate_images(image_source, adaptive_spec_list, "adaptive")

    print("Icon generation complete!")

if __name__ == "__main__":
    main()
