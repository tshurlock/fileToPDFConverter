'''working for .docx, need to .dotx, .doc is converted to .docx prior to this function'''
import os
import glob
from docx2pdf import convert as docx_to_pdf
from win32com import client


wordTypes = ('.docx')


def wordToPDFConvert(subdir, filename):
    input_path = os.path.join(subdir, filename)
    output_path = os.path.join(subdir, f"{os.path.splitext(filename)[0]}.pdf")
    docx_to_pdf(input_path, output_path)
    os.remove(input_path)


'''
def wordToPDFConvert(subdir, filename):
    input_path = os.path.join(subdir, filename)
    output_path = os.path.join(subdir, f"{os.path.splitext(filename)[0]}.pdf")

    file_ext = os.path.splitext(file_path)[1].lower()

    # Convert .docx and .doc files to PDF
    if file_ext in ['.docx', '.doc']:
        docx_to_pdf(file_path, os.path.join(output_folder, f'{os.path.basename(file_path)[:-5]}.pdf'))


'''