''' now intergrated to main no longer needed'''

import os
import imageConverter
import txtAndMsgToPdfConverter
import wordToPDF
import datetime

folder_path= 'C:\\Users\\Tim\\Desktop\\ExtractedZips'



# add in time stamp that is added to report file name so that a unique file is generated each time
# add path so report file is in situ
'''Correctly working for image and word file types. add txt and msg'''

'''access current time/date as object and convert to string'''
now = datetime.datetime.now()
nowStr = now.strftime("%Y-%m-%d %H:%M:%S")



# single OS walk here that will call relevent file converter
with open('conversion_to_PDF_report.txt','w') as f:
    f.write(f'Conversion to PDF report for files in {folder_path}\n')
    f.write(f'Completed {nowStr}\n\n')
    for subdir, dirs, files in os.walk(folder_path):
        for filename in files:
            # image file types
            if filename.endswith(imageConverter.imageTypes):
                imageConverter.imageConvert(subdir, filename)
                print('converted to pdf ', filename)
                f.write(f'{filename} was converted to a pdf\n')
            # word docx files
            elif filename.endswith(wordToPDF.wordTypes):
                wordToPDF.wordToPDFConvert(subdir, filename)
                print('converted to pdf ', filename)
                f.write(f'{filename} was converted to a pdf\n')
            # txt and msg files
            elif filename.endswith(txtAndMsgToPdfConverter.txtTypes):
                txtAndMsgToPdfConverter.convertTxtOrMsgToPdf(subdir, filename)
                print('converted to pdf ', filename)
                f.write(f'{filename} was converted to a pdf\n')
            # pdf files
            elif filename.endswith('.pdf'):
                f.write(f'{filename} is already a pdf file\n')
            else:
                print('not an image file, no conversion', filename)
                f.write(f'{filename} is not a supported file type, unable to convert to pdf\n')


