**File to PDF converter**

**20/07/2023**

**Purpose**

This programme takes a zipfile, extracts the contents. It then iterates
through all files in dir and any subdir. 

-If the file is a supported type it is
converted to a PDF (in situ) and the original file format is deleted.
-If the file is already a PDF file it is left in situ
-If the file is an unsuported format it is left in situ

The end result is that all of the files in the location chosen to extract 
the zip file will end up as PDFs (unless unsupported format)

**Operation**

1) run main.py
2) User is provided with file explorer window in order to select a zipfile
3) User is immediately provided with a second file explorer window to select
a location to extract zip file
4) A first pass OS walk checks for .doc format files and converts to .docx
   (in preparation for PDF conversion)
5) A second OS walk through the location where zip was extracted checks each
file type.
6) if file type is a supported image, txt, msg or word file it is converted
to PDF (in situ) and original file format is deleted.
7) If file type is already PDF or is an unsupported format then it is left
in situ
8) A report 'conversion_to_PDF_report.txt' is produced detailing, date/time
and the action taken for each file

**WARNING**

zipfile should be extracted to a new/empty directory. Main will attempt to
convert all files at location of extraction, therefore if extracted to 
e.g. desktop, documents can result in long run time and uninteded loss of
documents in their original format.

main now uses file explorer to select zip file and select destination file 
and holds they values, next step is to run OS walk in main which
will point the file the relevent converter so single walk is needed, not one
for each py file


**Action of individual modules**


Currently able to convert .txt, .doc, .docx, image files and .msg.

-main; imports extractor.py which contains extraction function to extract a zipfile, and imports doToDocxConverter,
which contains docToDocx function that converts doc to docx and deletes the original (in preparation for docxtopdf).
In future main will import all the other file type converters so that a single iteration through directory will id
filetype and then apply relevant converter.

-extractor; see above

-docToDocxConverter; see above

-imageConverter; converts ('.tif', '.tiff', '.jpg', '.jpeg', '.png', '.gif', '.eps', '.ai', '.psd', '.indd', '.raw')
files to pdf

-txtAndMsgToPdfConverter; converts .msg or .txt to pdf, currently hard coded to single file

-wordToPDF; .docx to PDF

**Supported File Types**

**Supported:**
.txt, .doc, .docx, .tif, .msg, .jpg, .png, .gif, .jpeg, .tiff

**Not applicable:**
.pdf (conversion not required, PDF is desired file format)
.zip (content will be extracted and individual files converted)

**Currenlty not supported:**
.xlsx, .rtf, .xls, .htm, .wav, .xps, .xlsm, .html, .pptx, .ppt, .mht, .xltx, .csv, .bmp, .eml, .dotx
