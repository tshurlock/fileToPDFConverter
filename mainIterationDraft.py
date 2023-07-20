import os

import imageConverter
import wordToPDF

folder_path= 'C:\\Users\\Tim\\Desktop\\ExtractedZips'

# add in time stamp that is added to report file name so that a unique file is generated each time
# add path so report file is in situ
'''Correctly working for image and word file types. add txt and msg'''

# single OS walk here that will call relevent file converter
with open('report.txt','w') as f:
    for subdir, dirs, files in os.walk(folder_path):
        for filename in files:
            # image file types
            if filename.endswith(imageConverter.imageTypes):
                imageConverter.imageConvert(subdir, filename)
                print('converted to pdf ', filename)
                f.write(f'{filename} was converted to a pdf\n')
            elif filename.endswith(wordToPDF.wordTypes):
                wordToPDF.wordToPDFConvert(subdir, filename)
                print('converted to pdf ', filename)
                f.write(f'{filename} was converted to a pdf\n')
            else:
                print('not an image file, no conversion', filename)
                f.write(f'{filename} is not an image file\n')


''' write to file each time is working, just need to add in convert logic and converstion here'''