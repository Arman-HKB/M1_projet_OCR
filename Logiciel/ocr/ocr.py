
from PIL import Image
import numpy as np
import pdfplumber
import time
import os


def detectAbsent(filename,low,high) : 

    directory = f"./ocr/proof"
    if not os.path.exists(directory):
        os.makedirs(directory)
    #open the pdf file
    pdf = pdfplumber.open(filename)
    data = []
    i=0
    for page in pdf.pages :

        #extract text from pdf pages
        text = page.extract_words()
        text2 = page.extract_text()
        save=False
        for t in text:
            if t["text"].upper() == "PRESENCE":
                presence = t
            if t["text"].lower() == "date" :
                dateCoords = t

        if ("FEUILLE DE PRESENCE" in text2) :
            save=True
            header = page.crop((0,presence["bottom"]+5 ,500,dateCoords["bottom"]))               
            headerText = header.extract_text()
            headerTextLower = headerText.lower()

            start_enseignant = headerTextLower.find("enseignant") + len("enseignant") + 2
            start_ue_ecue = headerTextLower.find("ue ou ecue") + len("UE ou ECUE") + 2
            start_date = headerTextLower.find("date") + len("Date") + 1

            enseignant = headerText[start_enseignant:start_ue_ecue - 12].strip().replace(":","")
            ue_ecue = headerText[start_ue_ecue:start_date - 5].strip().replace(":","")
            date = headerText[start_date:].strip().replace(":","")
            headerList=headerText.split("\n")
            lessonInfoList = list(filter(lambda x: x != ' ' and len(x)>1, headerList))
            lessonInfo={
                "promo": lessonInfoList[0] if len(lessonInfoList)>1 else "manquant",
                "enseignant": enseignant if enseignant else "manquant",
                "ue" : ue_ecue if ue_ecue else "manquant",
                "date" : date if date else "manquant"
            }
            studentsInfo = []
        #iterate over the extracted text list
        for word in range(len(text)) :
            start_time = time.perf_counter()
            #get coordinates of the text when text is equal to "M." or "Mme"
            if text[word]['text'] == "M." or text[word]['text'] == "Mme" or text[word]['text'] == "M-" or text[word]['text'] == "M" or text[word]['text'] == "M " or  text[word]['text'] == "Mme " :           
                #Once we're here, we know that word is "M." or "Mme" so the next word is the name
                if len(text[word]['text'])==2:
                    civility = "M"
                else :
                    civility = "Mme"
                nextWord=word+1
                name = ""
                #need a while loop because the name can be composed of several words
                while  text[nextWord]['text'].isalpha() and text[nextWord]['text'] != "M." and text[nextWord]['text'] != "Mme":
                    name += text[nextWord]['text'] + " "
                    nextWord+=1
                    try:
                        text[nextWord]
                    except:
                        break


                #coords of the text
                top = text[word]['top']-6
                left = text[word]['x0']
                right = left + 490
                bottom = text[word]['bottom']+6

                #crop the pdf to get the row of the table that we are interested in AND the next row AND the previous row
                croppedPDFWithTopAndBottom = page.crop((left,top-24,right,bottom+24))
                #crop the pdf to only get one row of the table (gender, name, surname and his signature)
                croppedPDF = page.crop((left,top,right,bottom))

                #convert the cropped pdf to png (beacause we need to count number of black pixels)
                croppedPNG = croppedPDF.to_image()
                croppedPNGWithTopAndBottom = croppedPDFWithTopAndBottom.to_image()
                #save the cropped image
                croppedPNG.save("./ocr/scanned/crop.png")
                #open the cropped image
                cropped = Image.open("./ocr/scanned/crop.png")
                
                #get dimensions of the cropped image
                width, height = cropped.size
                #crop again the image to only get the signature
                signature = cropped.crop((315,5,width-15,height-6))

                #get the number of not-white pixels (pixel's brightness <= 220) in the signature
                numberOfBlackPixel = np.sum(np.array(signature) <= 220)
                


                #if the number of not-white pixels is greater than 380, it means that the person signed
                #380 is the minimum of pixels required for a signature to be 100% sure
                #change this value allows to adjust the precision of the detection (not recommended)
                probaOfSignature = ((numberOfBlackPixel*100)/320)
                if probaOfSignature > 100 :
                    probaOfSignature = 100
                hasSigned = probaOfSignature >= high

                #save a sreenshot of the signatures that are suspicious
                if probaOfSignature > low and probaOfSignature < high :
                    i=i+1
                    croppedPNGWithTopAndBottom.save(f"./ocr/proof/cropWithTopAndBottom{i}.png")

                #formatted display
                student = name
                if len(name)>0:
                    studentsInfo.append({
                        "civility": civility,
                        "student": student,
                        "hasSigned": hasSigned,
                        "probaOfSignature": probaOfSignature,
                        "proof" : f"./ocr/proof/cropWithTopAndBottom{i}.png",
                        "verifie": False
                    })
                end_time = time.perf_counter()
                execution_time = end_time - start_time
        if save : 
            data.append({
                "lessonInfo": lessonInfo,
                "studentsInfo": studentsInfo
            })
        
    #clean the cropped image if it exists
    try:
        os.remove("./ocr/scanned/crop.png") 
    except :
        pass
    
    return data