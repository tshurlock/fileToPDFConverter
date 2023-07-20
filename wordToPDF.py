'''working for .docx, need to .dotx, .doc is converted to .docx prior to this function'''
import os
from docx2pdf import convert as docx_to_pdf


wordTypes = ('.docx')


def wordToPDFConvert(subdir, filename):
    input_path = os.path.join(subdir, filename)
    output_path = os.path.join(subdir, f"{os.path.splitext(filename)[0]}.pdf")
    docx_to_pdf(input_path, output_path)
    os.remove(input_path)


