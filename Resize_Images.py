import os
from PIL import Image

# Define the path for the new directory
new_folder = 'resized_images'

# Create the new directory if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through all files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.png') or filename.endswith('.PNG'):
        # Open an image file
        with Image.open(filename) as img:
            # Get the original dimensions
            original_width, original_height = img.size
            
            # Calculate the new dimensions (half the size)
            new_width = original_width // 2
            new_height = original_height // 2
            
            # Resize the image
            resized_img = img.resize((new_width, new_height))
            
            # Save the resized image in the new directory with the same name
            resized_img.save(os.path.join(new_folder, filename))

print("Resizing completed. All images are saved in the 'resized_images' folder.")
