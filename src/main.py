import PyPDF2
import re
import customutils

DEBUG_MODE = True

pdfFileObj = open('timer1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
if pageObj == "" or pageObj is None:
    print ("ERROR:EMPTY PAGE")
else:    
    test = pageObj.extractText()
    test += "\n ENDOFPAGE"

        #UnFiltered Data
    if DEBUG_MODE:
        text_file_unfiltered = open("Output_unfiltered.txt","w")
        text_file_unfiltered.write(test)
        text_file_unfiltered.close()
        # Close Unfiltered Data

    text_file = open("Output.txt", "w")
    
    
    text_array = re.split("\n",test)
    text_array = customutils.cleanup(text_array)
    
    customutils.PageCreation(text_array)
    for i in text_array:
        text_file.write(i + "\n")
    #Writing to text
    text_file.close()
