import os

folder_path= 'C:\\Users\\Tim\\Desktop\\ExtractedZips'
for subdir, dirs, files in os.walk(folder_path):
        for filename in files:
            print('dir ', dirs, ' subdir ', subdir, ' filename ', filename)
