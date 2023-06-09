'''single function to extract the content of a zip file'''

import zipfile
import os



def extraction(file_path):
    zip_file = file_path
    extract_to = 'C:\\Users\\Tim\\Desktop\\ExtractedZips'

    # Make sure the extract directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Extract the zip file to the extract directory
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f'Successfully extracted {zip_file} to {extract_to}')

