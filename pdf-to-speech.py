# importing library
import glob
import PyPDF2
import pyttsx3

# convert pdf to speech function
def pdf_speak(filename: str):

    # read pdf 
    read_pdf = PyPDF2.PdfFileReader(open(filename, 'rb'))
    pages = read_pdf.numPages

    # initiate text to speach engine
    engine = pyttsx3.init()

    # extract the content on page
    for i in range(pages):
        page = read_pdf.getPage(i)
        text_content = page.extractText()

        # convert text into speech
        engine.say(text_content)   
        engine.runAndWait()

# opening file in directory
for allfile in glob.glob('*.pdf'):
    pdf_file = allfile
    
# converting file    
pdf_speak(pdf_file)
