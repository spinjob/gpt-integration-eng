import argparse
from PIL import Image
import os

def resize_image(image_path, width, height):
    """Resizes an image to the specified width and height."""
    with Image.open(image_path) as img:
        resized_img = img.resize((width, height))
        resized_img.save(f'resized_{os.path.basename(image_path)}')

def main():
    """Main function to parse arguments and call the resize function."""
    parser = argparse.ArgumentParser(description='Resize an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file.')
    parser.add_argument('width', type=int, help='Desired width of the image.')
    parser.add_argument('height', type=int, help='Desired height of the image.')

    args = parser.parse_args()

    resize_image(args.image_path, args.width, args.height)

if __name__ == "__main__":
    main()
