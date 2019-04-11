#import PyPDF2 module
import PyPDF2

#open file we want to read and copy from
pdfFile = open('meetingminutes.pdf', 'rb')

#open file we want to write to
pdfOFile = open('meetingminutes1.pdf', 'wb')

#open the file we want to read at the end
pdfORFile = open('meetingminutes1.pdf', 'rb')

#create object to read pdfFile
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#create object to write
pdfWriter = PyPDF2.PdfFileWriter()

#the string we want to cross examine to the pdf pages
st = input('Please enter the string \'student\' -')

#loop through pdfFile
for page in range(pdfReader.numPages):

    #create page object
    p = pdfReader.getPage(page)

    #store the page object text into a string so we can cross examine it
    ext = p.extractText()

    #test purposes making sure the loop is working properly
    print('test -1-' + str(page))

    #loop to see if string st is in the stored string ext which is a page of the pdf document
    if st in ext:

        #add the page @ p to the writer... Think about this like storing objects in memory its temporary
        pdfWriter.addPage(p)

        # test purposes making sure the loop is working properly
        print('test -2-' + str(page))
    else:

        # test purposes making sure the loop is working properly
        print('test -3-' + str(page))

#visual effects for seperation
print('\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')

#write pages we added above to pdfOFile
pdfWriter.write(pdfOFile)

#close file since we arent using it
pdfOFile.close()

#close file since we arent using it
pdfFile.close()

#new reader instance to read the final copy and make sure it copied properly
pdfReaderO = PyPDF2.PdfFileReader(pdfORFile)

#loop through pdfORFile
for pages in range(pdfReaderO.numPages):

    #create page object pO
    pO = pdfReaderO.getPage(pages)

    #print pO
    print(pO.extractText())

    #visual effects for seperation of pages
    print('\n-----------------------------------------------------------------------------------------------------\n')

#close file since we arent using it
pdfORFile.close()
