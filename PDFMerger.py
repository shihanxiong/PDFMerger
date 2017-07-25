# Loading the pyPdf Library
from PyPDF2 import PdfFileMerger

pdfs = ['WPI_Transcript_1.pdf', 'WPI_Transcript_2.pdf', 'WPI_Transcript_3.pdf', 'WPI_Transcript_4.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('WPI_Transcript_Hanxiong_Shi.pdf', 'wb') as fout:
    merger.write(fout)