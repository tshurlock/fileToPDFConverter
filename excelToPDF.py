'''not working'''
import pandas as pd
#from xlsx2pdf import convert

file_path = 'testToConvert\\2023 Budget.xlsx'
output_path = 'testToConvert\\shinynew.pdf'

df = pd.read_excel(file_path)
df.to_pdf(output_path)