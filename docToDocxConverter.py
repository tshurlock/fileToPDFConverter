import os
from doc2docx import convert

def docToDocx(folder_path):
    for subdir, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith('.doc'):
                    doc_path = os.path.join(subdir, filename)
                    docx_path = os.path.join(subdir, filename + 'x')
                    convert(doc_path, docx_path)
                    os.remove(doc_path)

