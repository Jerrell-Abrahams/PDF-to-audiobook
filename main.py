import PyPDF2
import pyttsx3

def pdf_open(filename):
    """
    Function that parses through a pdf file and returns the text that is passed to the speech engine
    """
    with open(filename, "rb") as pdf:
        output = ""
        pdf_file = PyPDF2.PdfFileReader(pdf)
        for page in range(0, pdf_file.getNumPages()):
            all_pages = pdf_file.getPage(page).extractText()
            output += all_pages
    return output
        
def text_to_speech(text):
    """
    Engine that allows the text to be converted to speech
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



if __name__ == '__main__':
    """
    Add pdf to project folder then 
    Enter filename in pdf_open function
    """
    text = pdf_open("Praxis FA2.pdf")
    print(text)
    text_to_speech(text)