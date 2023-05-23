'''single function to extract the content of a zip file'''

import zipfile
import os



def extraction():
    zip_file = 'C:\\Users\\Tim\\Downloads\\Output.zip'
    extract_to = 'C:\\Users\\Tim\\PycharmProjects\\pythonProject8\\testToConvert'

    # Make sure the extract directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Extract the zip file to the extract directory
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f'Successfully extracted {zip_file} to {extract_to}')

