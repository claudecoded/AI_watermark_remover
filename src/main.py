import cv2
import numpy as np
import os

def remove_watermark(image_path, output_path, low_threshold=150, high_threshold=255):
    """
    Removes watermarks from images using OpenCV's Inpainting technique.
    
    :param image_path: Path to the original image.
    :param output_path: Path where the processed image will be saved.
    :param low_threshold: Lower threshold for detecting bright/white watermark pixels.
    :param high_threshold: Upper threshold for the binary mask.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} was not found.")
        return

    # 1. Load the original image
    img = cv2.imread(image_path)

    # 2. Convert to grayscale to easily detect shapes/text
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Create a binary mask (detects bright pixels which usually form watermarks)
    # Adjust thresholds if the watermark is dark or colored
    _, mask = cv2.threshold(gray, low_threshold, high_threshold, cv2.THRESH_BINARY)

    # 4. Apply Inpainting algorithm to fill the masked area
    # cv2.INPAINT_TELEA is ideal for fast restoration and textual noise removal
    result = cv2.inpaint(img, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # 5. Save the final result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, result)
    print(f"Success! Watermark-free image saved to: {output_path}")

if __name__ == "__main__":
    # Local usage example
    # Make sure to create an 'input' folder with an image inside to test
    INPUT_IMAGE = "input/watermarked_image.jpg"
    OUTPUT_IMAGE = "output/cleaned_image.jpg"
    
    print("Starting watermark removal process...")
    remove_watermark(INPUT_IMAGE, OUTPUT_IMAGE)
