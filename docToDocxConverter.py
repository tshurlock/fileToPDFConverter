import os
from doc2docx import convert

def docToDocx():
    directory = 'testToConvert'

    for filename in os.listdir(directory):
        if filename.endswith('.doc'):
            doc_path = os.path.join(directory, filename)
            docx_path = os.path.join(directory, filename + 'x')
            convert(doc_path, docx_path)
            os.remove(doc_path)