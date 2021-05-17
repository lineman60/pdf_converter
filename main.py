# importing required modules
import PyPDF2
import glob

def read_pdf(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    total_pages = int(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(0)
    for pagenumb in range(0,total_pages ):
        # extracting text from page
        print(pageObj.extractText())
    pdfFileObj.close()

# creating a pdf file object
file_to_read = glob.glob('*.pdf')
for x in file_to_read:
    read_pdf(x)

