import xlsxwriter
import os

def present(bool):
    if bool:
        return 'Présent'
    else:
        return 'Absent' 

# Save the changes to the Excel file
def to_excel(data, name):
    path = name[0]
    wb = xlsxwriter.Workbook(path)
    for i in data:
        lessonInfo=i['lessonInfo']
        filiere=lessonInfo["promo"]
        enseignant=lessonInfo["enseignant"]
        ue=lessonInfo["ue"]
        date=lessonInfo["date"]
        ws = wb.add_worksheet(filiere)
        listeStudents=list(map(lambda x: [x['civility']]+[x['student']]+[x['hasSigned']],i['studentsInfo']))
        df=list(map(lambda x : x[:2]+[present(x[2])],listeStudents))
        ws.write(0,0,filiere)
        ws.write(1,0,enseignant + " " +  ue)
        ws.write(2,0,date)
        ws.add_table("A4:C"+str(len(i['studentsInfo'])+4),{'data':df,'columns':[
    {'header': 'Civilité'},
    {'header': 'Nom Complet'},
    {'header': 'Présence'}]})
    wb.close()
