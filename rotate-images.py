import os
import sys
from PIL import Image

def rotate_images(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Process each file in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'webp')):
            file_path = os.path.join(directory, filename)
            try:
                with Image.open(file_path) as img:
                    # Rotate the image by 180 degrees
                    rotated_img = img.rotate(180)
                    # Save the rotated image back to the filesystem
                    rotated_img.save(file_path)
                    print(f"Rotated {filename} by 180 degrees.")
            except Exception as e:
                print(f"Could not process file '{filename}': {e}")

if __name__ == "__main__":
    # Check if the directory was passed as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python rotate_images.py <directory>")
        sys.exit(1)

    # Get the directory from the command line arguments
    directory = sys.argv[1]
    rotate_images(directory)
