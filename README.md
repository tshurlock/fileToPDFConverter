**DRAFT and NOTES**

**09/05/2023**

main now uses file explorer to select zip file and select destination file 
and holds they values, next step is to run OS walk in main which
will point the file the relevent converter so single walk is needed, not one
for each py file


**23/05/2023**

Throughout programme hard coded file paths used, will use PATH objects from pathlib in future and ideally end user
to use file explorer to select source zipfile for conversion and destination for converted files.
Currently able to convert .txt, .doc, .docx, image files and .msg which covers 99.2% of files in docSearch

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





**NOTES**

Front end considerations and deployment ?Tkinter ?Webapp
Need os walk

need exception handling if file is not valid type.

**TODO**

Completion report
Copy file structure including where unable to convert to PDF



**File Type**

.txt _ complete
.doc _ complete
.pdf _ not required
.docx_ complete
.tif _ complete
.msg _ complete
.jpg _ complete
.xlsx
.rtf
.xls
.png _ complete
.htm
.gif _ complete
.zip _ n/a
.jpeg _ complete
.wav
.xps
.tiff _ complete
.xlsm
.html
.pptx
.ppt
.mht
.xltx
.csv
.bmp
.eml
.dotx