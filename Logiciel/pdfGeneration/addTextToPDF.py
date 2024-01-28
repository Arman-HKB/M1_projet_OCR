from PyPDF2 import PdfWriter, PdfReader
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from unidecode import unidecode                        

def addTextToPDF(teacher ,classes,loopN):
    teacher = teacher
    name = classes["name"]
    day = classes["day"]
    time = classes["time"]
    promo = classes["promo"]

    if classes["group"] == "":
        group = "CM"
    else:
        group = classes["group"]

    packet = io.BytesIO()

    can = canvas.Canvas(packet, pagesize=letter)
    #Change font and size

    can.setFont('Times-Bold',12)

    #write data
    day = day.replace("\n", " ").replace("\xa0", " ").replace("\t", " ")
    can.drawString(160, 653, teacher)
    can.drawString(160, 626, name)
    can.drawString(160, 597, day+time)
    can.save()

    pdfModel = group +"_"+promo
    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF
    try :
        existing_pdf = PdfReader(open(f"pdfGeneration./models/{promo}/{pdfModel}.pdf", "rb"))
    except:
        raise Exception("Le modèle de pdf n'existe pas")

    output = PdfWriter()

    # add the data on the existing page
    page = existing_pdf.pages[0]
    #merge edited page
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    #add unedited pages
    for i in range(1,len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        output.add_page(page)

    directory = f"./pdfGeneration/results/{teacher}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    #delete old pdf
    if loopN == 0 :
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                file_path = os.path.join(directory, filename)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

    day=day.strip()
    day = unidecode(day)
    #output the new PDF
    outputStream = open(f"./pdfGeneration/results/{teacher}/{promo + group}_{day}_{time}.pdf", "wb")
    output.write(outputStream)
    outputStream.close()