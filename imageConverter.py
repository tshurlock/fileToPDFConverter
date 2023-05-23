'''this is working to iterate and change files if image type, currently original, eventually will merge all filetype
converters to single filehandler'''

import os
from PIL import Image

imageTypes= ('.tif', '.tiff', '.jpg', '.jpeg', '.png', '.gif', '.eps', '.ai', '.psd', '.indd', '.raw')

# Set the path to the folder containing the files to convert
#place holder path, this will need to be the path of extracted PDF
folder_path = "testToConvert"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a JPEG image
    print(filename)
    if filename.endswith(imageTypes):
        # Set the input and output file paths

        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.pdf")

        # Use Pillow to open the image and save it as a PDF
        with Image.open(input_path) as img:
            img.save(output_path, "PDF", resolution=100.0)

        print(f"Converted {input_path} to {output_path}")