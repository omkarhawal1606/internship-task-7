import os
from PIL import Image

# Input and output folders
input_folder = "images"          # Folder with original images
output_folder = "resized_images" # Folder to save resized images

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired resize dimensions (width, height)
new_size = (800, 600)

# Loop through all image files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # Open image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        resized_img = img.resize(new_size)

        # Save to output folder (optional: convert format)
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        print(f"Resized and saved: {output_path}")

print("✅ All images resized successfully!")
