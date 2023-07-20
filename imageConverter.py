'''this is working to iterate and change files if image type, currently original, eventually will merge all filetype
converters to single filehandler'''

import os
from PIL import Image

imageTypes= ('.tif', '.tiff', '.jpg', '.jpeg', '.png', '.GIF', '.eps', '.ai', '.psd', '.indd', '.raw')

# Set the path to the folder containing the files to convert
#place holder path, this will need to be the path of extracted PDF


def imageConvert(subdir, filename):
    input_path = os.path.join(subdir, filename)
    output_path = os.path.join(subdir, f"{os.path.splitext(filename)[0]}.pdf")

    # Use Pillow to open the image and save it as a PDF
    with Image.open(input_path) as img:
        img.save(output_path, "PDF", resolution=100.0)

    os.remove(input_path)