if __name__ == '__main__':
    print('run')
    '''extractor module contains single function extractor that unzips contents of zip file and saves in new location'''
    '''extractor module is currently relying on hardcoded filepaths, in final version file path should be provided here
    as arguaments to extraction function'''

    '''GUI opens file extractor GUi to select a file to enable Zip file to be selected'''
    import GUI
    file_path= GUI.open_file_explorer()

    import extractor
    folder_path= extractor.extraction(file_path)

    print()
    print('The zip file {} was extracted, its contents have been saved at {}'.format(file_path, folder_path))

    '''docToDocxConverter contains single function docToDocx which iterates through directory, for any .doc file, it 
    converts to .docx and deletes the original file'''
    '''
    import docToDocxConverter
    docToDocxConverter.docToDocx()
'''


