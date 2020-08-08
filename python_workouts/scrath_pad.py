
# # Content
# filename = 'Report.pdf'
# documentTitle = 'OSCP Report'
# title = 'Lab Report of OSCP Exam'
# subTitle = 'Lab 1-5'

# textLines = ['Test','TEST']




# from reportlab.pdfgen import canvas

# pdf = canvas.Canvas(filename)
# pdf.setTitle(documentTitle)
# pdf.setFont('Times-Roman', 36)
# pdf.drawCentredString(300,770, title)

# pdf.setFillColorRGB(0,0,255)
# pdf.setFont('Times-Roman', 24)
# pdf.drawCentredString(300, 720, subTitle)

# pdf.line(30,710,550,710)

# pdf.save()
url_in = 'https://www.google.com/active;ls'
url_out = ''

for letter in url_in:
    if letter in '^&; \$':
        url_out += f"%{str(ord(letter))}"
    else:
        url_out += letter
    
print(url_out)


print(ord('/'))