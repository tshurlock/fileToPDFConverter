import os

import imageConverter

folder_path= 'C:\\Users\\Tim\\Desktop\\ExtractedZips'

# add in time stamp that is added to report file name so that a unique file is generated each time
# add path so report file is in situ
'''Currently importing image converter, working correctly but writing to root directory, want to do in situ, make 
changes to imageCoverter file'''

# single OS walk here that will call relevent file converter
with open('report.txt','w') as f:
    for subdir, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(imageConverter.imageTypes):
                imageConverter.imageConvert(folder_path, filename)
                print(filename)
                f.write(f'{filename} was converted to a pdf\n')
            else:
                print('x', filename)
                f.write(f'{filename} is not an image file\n')


''' write to file each time is working, just need to add in convert logic and converstion here'''