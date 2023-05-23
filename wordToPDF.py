'''working for .docx, need to .dotx, .doc is converted to .docx prior to this function'''
import os
import glob
from docx2pdf import convert as docx_to_pdf
from win32com import client

# Define the input and output folders
input_folder = 'testToConvert'
output_folder = 'testToConvert'

# Iterate through all the files in the input folder
for file_path in glob.glob(os.path.join(input_folder, '*.*')):
    # Get the file extension
    file_ext = os.path.splitext(file_path)[1].lower()

    # Convert .docx and .doc files to PDF
    if file_ext in ['.docx', '.doc']:
        docx_to_pdf(file_path, os.path.join(output_folder, f'{os.path.basename(file_path)[:-5]}.pdf'))

