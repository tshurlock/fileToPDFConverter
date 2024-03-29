'''this functions correctly, .txt and .msg file is converted to pdf with appropriate margins/text wrapping, one file
with special characters was not working and had to add encoding=latin-1 to work, so far it works for all but will
need some test cases.
 Currenlty only accepting single hard coded file path, need to change to iterate for txt/msg files'''
'''contains function that converts a .txt file to .pdf, includes hardcoded margin and page size as well as text
wrapping'''

'''cant handle chars in Ed report, encoding issue try with RTF'''
from fpdf import FPDF
import os

txtTypes = ('.txt', '.msg')

def convertTxtOrMsgToPdf(subdir, filename):
    # Create a new PDF instance
    input_path = os.path.join(subdir, filename)
    output_path = os.path.join(subdir, f"{os.path.splitext(filename)[0]}.pdf")

    pdf = FPDF()

    # Set the margins (change as needed)
    left_margin = 10
    top_margin = 10
    right_margin = 10

    # Set the page dimensions (change as needed)
    page_width = 210  # A4 width in mm
    page_height = 297  # A4 height in mm

    # Calculate the usable width and height
    usable_width = page_width - left_margin - right_margin
    usable_height = page_height - top_margin

    # Open the .txt file and read its content
    '''ed reports file has special characters, required encoding argument to work and values is latin-1, may need to 
    provide this as if argument to determine encoding'''
    with open(input_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Add a new page
    pdf.add_page()

    # Set the font and font size (change as needed)
    font_size = 12
    pdf.set_font("Arial", size=font_size)

    # Split the content into lines and wrap text
    lines = pdf.multi_cell(usable_width, font_size, content)

    # Output the PDF file
    pdf.output(output_path)
    os.remove(input_path)

