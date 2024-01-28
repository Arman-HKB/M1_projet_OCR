import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from QtInterface.app_ui import Ui_MainWindow
from ocr.ocr import detectAbsent
import json
import configparser
from ocr.toExcel import to_excel
from pdfGeneration.pdfGenerator import generate_pdf
from pdfGeneration.addTextToPDF import addTextToPDF
from pdfGeneration.sendMail import sendPDF
from datetime import datetime, timedelta
import darkdetect
import locale
import requests
import mysql.connector
import urllib.request
from ftplib import FTP

# Open Config file and get the current values
config = configparser.ConfigParser()
config.read_file(open(r'config.ini'))
confLow = config.get('Tolerance Signature', 'low')
confHigh = config.get('Tolerance Signature', 'high')
confPromoList = config.get('Generation PDF', 'promoList')
confGroupList = config.get('Generation PDF', 'groupList')
confTheme = config.get('Theme', 'color')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        locale.setlocale(locale.LC_ALL, 'fr_FR')
        now = datetime.now()
        day_of_week = now.weekday()
        # Check if it's Sunday
        if day_of_week == 6:
            # If it's Sunday, add one day to get the next Monday
            self.monday = (now + timedelta(days=1)).strftime("%A %d %B")
            self.saturday = (now + timedelta(days=6)).strftime("%A %d %B")
        else:
            # If it's not Sunday, subtract the number of days from Monday
            self.monday = (now - timedelta(days=day_of_week)).strftime("%A %d %B")
            self.saturday = (now - timedelta(days=day_of_week) + timedelta(days=5)).strftime("%A %d %B")
        self.fileName=""
        self.ui.main.setCurrentIndex(0)
        #self.ui.home_btn.setChecked(True)
        if(self.connect()):
            self.findChild(QFrame, "wifi_verticalFrame").hide()
        else: 
            self.findChild(QPushButton, "export_btn").hide()
        self.findChild(QPushButton, "saveScan_btn").hide()
        self.findChild(QPushButton, "saveToDB_btn").hide()
        self.findChild(QPushButton, "next_btn").hide()
        self.findChild(QPushButton, "previous_btn").hide()
        #self.findChild(QWidget, "widget_manualCheck").hide()
        self.tableStudents = self.findChild(QTableWidget, "tableWidget")
        self.tableStudents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.low = int(confLow)
        self.high = int(confHigh)
        self.dataAPI = []
        self.teachersToMail = []
        self.promoList = confPromoList.split(",")
        self.promoList.sort()
        self.groupList = confGroupList.split(",")
        self.groupList.sort()
        header = self.tableStudents.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.findChild(QLabel, "import_success_label").hide()
        self.tableStudents.hide()
        self.labelTitle1 = self.findChild(QLabel, "tableTitle_1")
        self.labelTitle1.hide()
        self.labelTitle2 = self.findChild(QLabel, "tableTitle_2")
        self.labelTitle2.hide()
        self.labelTitle3 = self.findChild(QLabel, "tableTitle_3")
        self.labelTitle3.hide()
        self.labelTitle4 = self.findChild(QLabel, "tableTitle_4")
        self.labelTitle4.hide()
        self.labelStat1 = self.findChild(QLabel, "Stat_label_1")
        self.labelStat1.hide()
        self.labelStat2 = self.findChild(QLabel, "Stat_label_2")
        self.labelStat2.hide()
        self.labelStat3 = self.findChild(QLabel, "Stat_label_3")
        self.labelStat3.hide()
        self.pageTitle = self.findChild(QLabel, "pageTitle")
        self.pageTitle.hide()
        self.infoLabel = self.findChild(QLabel, "info_label_2")
        self.loadingOcr = self.findChild(QLabel, "loading_label_2")
        self.generalStatus = self.findChild(QLabel, "general_status")
        self.apiStatus = self.findChild(QLabel, "api_status")
        self.pdfGenerationStatus = self.findChild(QLabel, "pdf_generation_status")
        self.mailSendingStatus = self.findChild(QLabel, "mail_sending_status")

        self.promotionsList = []
        with open('promotions.json', 'r') as file:
            self.promotionsList = json.loads(file.read())
        file.close()
        with open('teachers.json', 'r') as file:
            self.teacherListJson = json.loads(file.read())
        file.close()
        self.teacherList = []
        for teacher in self.teacherListJson:
            self.teacherList.append(teacher["fullname"].upper())
        self.teacherList.sort()
        
        # LISTENERS
        self.generateBtn = self.findChild(QPushButton, "generate_btn")
        self.generateBtn.clicked.connect(self.generatePDF)
        self.sendBtn = self.findChild(QPushButton, "send_btn")
        self.sendBtn.clicked.connect(self.sendPDFBtn)
        self.importBtn = self.findChild(QPushButton, "import_file")
        self.importBtn.clicked.connect(self.importPDF)
        self.returnCheckBtn = self.findChild(QPushButton, "check_btn_return")
        self.returnCheckBtn.clicked.connect(self.returnFromCheck)
        self.refuseCheckBtn = self.findChild(QPushButton, "check_btn_refuse")
        self.refuseCheckBtn.clicked.connect(self.refuseCheck)
        self.validateCheckBtn = self.findChild(QPushButton, "check_btn_ok")
        self.validateCheckBtn.clicked.connect(self.validateCheck)
        
        self.findChild(QPushButton, "saveScan_btn").clicked.connect(self.saveScan)
        self.findChild(QPushButton, "saveToDB_btn").clicked.connect(self.saveToDB)
        self.findChild(QPushButton, "next_btn").clicked.connect(self.next_btn)
        self.findChild(QPushButton, "previous_btn").clicked.connect(self.previous_btn)

        self.lowSlider = self.findChild(QSlider, "low_slider")
        self.lowSlider.valueChanged.connect(self.lowSliderChanged)
        self.highSlider = self.findChild(QSlider, "high_slider")
        self.highSlider.valueChanged.connect(self.highSliderChanged)

        self.lowSlider.setValue(self.low)
        self.highSlider.setValue(self.high)
        self.findChild(QLabel, "low_label").setText(str(self.low))
        self.findChild(QLabel, "high_label").setText(str(self.high))

        self.teacherComboBox = self.findChild(QComboBox, "teacher_comboBox")
        if(self.connect()): self.teacherComboBox.addItems(self.teacherList)

        self.promoComboBox = self.findChild(QComboBox, "promo_comboBox")
        self.promoComboBox.addItems(self.promoList) 
        self.groupeComboBox = self.findChild(QComboBox, "groupe_comboBox")
        self.groupeComboBox.addItems(self.groupList)

        self.teacherComboBox.currentTextChanged.connect(self.check_combobox)
        self.promoComboBox.currentTextChanged.connect(self.check_combobox)
        self.groupeComboBox.currentTextChanged.connect(self.check_combobox)

        self.findChild(QLabel, "date_label").setText("Les feuilles de présences du <b>" + self.monday + " au " + self.saturday + "</b>  vont être générées avec les paramètres suivants :")
        self.findChild(QPushButton, "generate_btn").setEnabled(True)

        self.themeComboBox = self.findChild(QComboBox, "theme_combobox")
        self.themeComboBox.activated.connect(self.check_theme)
        if(confTheme == "dark"):
            self.themeComboBox.setCurrentIndex(1)
        elif(confTheme == "light"):
            self.themeComboBox.setCurrentIndex(2)

        self.title = self.findChild(QFrame, "title")
        self.pressing = False

        if(confTheme == "dark" or darkdetect.isDark()):
            if(confTheme != "light"):
                #self.findChild(QLabel, "label_logo").setPixmap(QPixmap("./QtInterface/assets/logo_full_dark.png"))
                self.findChild(QLabel, "miage_label_2").setPixmap(QPixmap("./QtInterface/assets/uca_dark.png"))
                self.findChild(QLabel, "miage_label").setPixmap(QPixmap("./QtInterface/assets/miage_dark.png"))

    def connect(self, host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False

    def check_combobox(self):
        comboBoxChoice = ["Tous les enseignants","Toutes les promotions","Tous les groupes"]
        if(self.teacherComboBox.currentText()=="Enseignant..."):
            comboBoxChoice[0] = "Tous les enseignants"
        else:
            comboBoxChoice[0] = self.teacherComboBox.currentText()
        
        if(self.promoComboBox.currentText()=="Promotion..."):
            comboBoxChoice[1] = "Toutes les promotions"
        else:
            comboBoxChoice[1] = self.promoComboBox.currentText()
        
        if(self.groupeComboBox.currentText()=="Groupe de TD/TP..."):
            comboBoxChoice[2] = "Tous les groupes"
        else:
            comboBoxChoice[2] = self.groupeComboBox.currentText()
        self.findChild(QLabel, "teacher_label").setText("Enseignant : " + comboBoxChoice[0])
        self.findChild(QLabel, "promo_label").setText("Promotion : " + comboBoxChoice[1])
        self.findChild(QLabel, "group_label").setText("Groupe : " + comboBoxChoice[2])

        return 0

    def check_theme(self):
        if(self.themeComboBox.currentIndex() == 0):
            theme = "auto"
        elif(self.themeComboBox.currentIndex() == 1):
            theme = "dark"
        else:
            theme = "light"
        config.set('Theme', 'color', theme)
        config.write(open('config.ini', 'w'))

        with open("QtInterface/QSS/style.qss", "r") as stylesheet:
            style_str = stylesheet.read()
        if(theme == "dark" or darkdetect.isDark()):
            with open("QtInterface/QSS/dark.qss", "r") as stylesheet:
                style_str_2 = stylesheet.read()
            self.setStyleSheet(style_str+style_str_2)
            self.findChild(QLabel, "miage_label").setPixmap(QPixmap("./QtInterface/assets/miage_dark.png"))
            self.findChild(QLabel, "miage_label_2").setPixmap(QPixmap("./QtInterface/assets/uca_dark.png"))
        if(theme == "light" or darkdetect.isLight()):
            self.setStyleSheet(style_str)
            self.findChild(QLabel, "miage_label").setPixmap(QPixmap("./QtInterface/assets/miage.png"))
            self.findChild(QLabel, "miage_label_2").setPixmap(QPixmap("./QtInterface/assets/uca.png"))
        return 0

    def lowSliderChanged(self):
        if self.lowSlider.value() >= self.high:
            self.lowSlider.setValue(self.high-1)
        self.findChild(QLabel, "low_label").setText(str(self.lowSlider.value()))
        self.low = self.lowSlider.value()
        config.set('Tolerance Signature', 'low', str(self.lowSlider.value()))
        config.write(open('config.ini', 'w'))

    def highSliderChanged(self):
        if self.highSlider.value() <= self.low:
            self.highSlider.setValue(self.low+1)
        self.findChild(QLabel, "high_label").setText(str(self.highSlider.value()))
        self.high = self.highSlider.value()
        config.set('Tolerance Signature', 'high', str(self.highSlider.value()))
        config.write(open('config.ini', 'w'))

    def getApiData(self):
        teacher = self.teacherComboBox.currentText()
        group = self.groupeComboBox.currentText()
        promotion = self.promoComboBox.currentText()
        if teacher == "Enseignant..." :
            teacher = ",".join(self.teacherList)
        if promotion == "Promotion..." :
            promotion =""
        if group == "Groupe de TD/TP..." :
            group = ""
        url = "https://api-beige-seven.vercel.app/?teachers="+teacher.replace(" ", "%20")+"&group="+group.replace(" ", "%20")+"&promo="+promotion.replace(" ", "%20")
        self.generalStatus.setText("Etat d'avancement : ")
        self.apiStatus.setText("Récupération des données depuis l'API en cours...")
        self.apiStatus.setStyleSheet("color: #F07B07")
        self.generalStatus.update()
        self.apiStatus.update()
        self.generalStatus.repaint()
        self.apiStatus.repaint()
        #get the data from the API
        try :
            response = requests.get(url)
            data = response.json()
        #if the request failed
        except Exception as e:
            print(e)
            self.apiStatus.setText("La récupération des donnees depuis l'API a echouée ✘")
            self.pdfGenerationStatus.setText("Annulation de la generation du PDF ")
            self.apiStatus.setStyleSheet("color: #b74242")
            return 0
        total_classes = 0
        for teacher in data:
            try :
                total_classes += len(teacher["class"])
            except :
                pass
        self.apiStatus.setText("Récupération des données depuis l'API terminée ✔ ({} cours trouvés)".format(total_classes))
        self.apiStatus.setStyleSheet("color: #43c342")
        self.dataAPI = data

    def generatePDF(self):
        self.apiStatus.setText("")
        self.pdfGenerationStatus.setText("")
        self.mailSendingStatus.setText("")
        
        self.getApiData()
        data = self.dataAPI
        if len(data) == 0 :
            return 0

        #generate the PDF with adding the data
        self.pdfGenerationStatus.setText("Génération des PDF en cours...")
        self.pdfGenerationStatus.setStyleSheet("color: #F07B07")
        self.pdfGenerationStatus.update()
        self.pdfGenerationStatus.repaint()

    
        try :
            i=0
            imax = 0
            for d in data:
                imax += len(d["class"])

            for d in data:
                if d["class"] == []:
                    continue
                t = d["teacher"]
                self.teachersToMail.append(t)

                for c in d["class"]:
                    try :
                        addTextToPDF(t,c,i)
                        i+=1
                    except Exception as e:
                        print(e)
                        continue
                    self.pdfGenerationStatus.setText("Génération des PDF en cours... ({} PDF générés sur {})".format(i, imax))
                    self.pdfGenerationStatus.update()
                    self.pdfGenerationStatus.repaint()
        except Exception as e:
            print(e)
            self.pdfGenerationStatus.setText("La generation du PDF a echouée ✘")
            self.pdfGenerationStatus.setStyleSheet("color: #b74242")
            return 0

        self.pdfGenerationStatus.setText("Generation des PDF terminée ✔ ({} PDF générés sur {})".format(i, imax))
        self.pdfGenerationStatus.setStyleSheet("color: #43C342")

        self.findChild(QPushButton, "send_btn").setEnabled(True)
        self.findChild(QCheckBox, "checkBox").setEnabled(True)

    def sendPDFBtn(self):
        self.mailSendingStatus.setText("Envoi des PDF en cours...")
        self.mailSendingStatus.setStyleSheet("color: #F07B07")
        self.mailSendingStatus.update()
        self.mailSendingStatus.repaint()
        expiredLessons = self.findChild(QCheckBox, "checkBox").isChecked()
        
        for t in self.teacherListJson :
            if t["fullname"] in self.teachersToMail :
                if t["email"] != "" :
                    
                    sendPDF("pdfGeneration/results/"+t["fullname"], t["email"], expiredLessons)

                else :
                    self.mailSendingStatus.setText(f"L'enseignant {t['fullname']} n'a pas d'email enregistré.")
                    self.mailSendingStatus.setStyleSheet("color : red")
                    self.mailSendingStatus.update()
                    self.mailSendingStatus.repaint()
                    time.sleep(2.5)

        self.mailSendingStatus.setText("Envoi des PDF terminé ✔")
        self.mailSendingStatus.setStyleSheet("color: #43C342")
        return 0

    def filter_students(self,promoList, promotion, td='', tp=''):
        filtered_students = []
        result = list(filter(lambda x: x["promotion"] == promotion, promoList)) 
        filtered_students = [student for item in result for student in item['students'] if (not td or student['TD'] == td) and (not tp or student['TP'] == tp)]
     
        return filtered_students

    def addStudent(self, promotion=None, civility=None, lastname=None, firstname=None, td=None, tp=None):
        if not lastname:
            promotion = self.promoComboBox2.currentText()
            civility = self.findChild(QComboBox, "civility_combobox").currentText()
            lastname = self.findChild(QLineEdit, "student_lastname_input").text().lower()
            firstname = self.findChild(QLineEdit, "student_firstname_input").text().lower()
            td = self.findChild(QLineEdit, "TD_input").text()
            tp = self.findChild(QLineEdit, "TP_input").text()
            if civility == "Civilité..." or promotion == "Promotion..." or lastname == "" or firstname == "":
                missing_fields = []

                if civility == "Civilité...":
                    missing_fields.append("Civilité")
                if promotion == "Promotion...":
                    missing_fields.append("Promotion")
                if lastname == "":
                    missing_fields.append("Nom")
                if firstname == "":
                    missing_fields.append("Prénom")

                if len(missing_fields) > 0:
                    self.infoLabel.setText("Les champs suivants sont manquants : {} ".format(", ".join(missing_fields)))
                self.infoLabel.setStyleSheet("color: #b74242")
                QTimer.singleShot(2500, lambda : self.infoLabel.setText("") )
                
                return 0

        # Si plusieurs étudiants sont ajoutés en même temps separé par une virgule
        if "," in lastname :
            lastnameList = lastname.split(",")
            firstnameList = firstname.split(",")
            tdList = td.split(",")
            tpList = tp.split(",")
            if civility == "Civilité..." or promotion == "Promotion...":
                return 0
            for i in range(len(lastnameList)):
                self.addStudent(promotion, civility, lastnameList[i], firstnameList[i], tdList[i], tpList[i])
            return 0

        # Ajouter un étudiant à la liste d'une promo.
        for promo in self.promotionsList:
            if promo["promotion"] == promotion:
                promo["students"].append({"civility" : civility ,
                                "lastname": lastname, 
                                "firstname":firstname,
                                "TD":td,
                                "TP":tp})
                break

        
        with open('promotions.json', 'w') as outfile:
            json.dump(self.promotionsList, outfile)
        outfile.close()
        with open('promotions.json', 'r') as file:
            self.promotionsList = json.loads(file.read())
        file.close()

        newPromotions = []
        with open('promotions.json', 'r') as file:
            newPromotions = json.loads(file.read())
        file.close()
        
        filteredStudentsCM = sorted(self.filter_students(newPromotions, promotion), key=lambda d: d['lastname'])
        filteredStudents = sorted(self.filter_students(newPromotions, promotion ,td,tp), key=lambda d: d['lastname'])
        try:
            if td :
                generate_pdf(filteredStudents, promotion,"TD"+td)
            if tp :
                generate_pdf(filteredStudents,promotion,"TP"+tp)
            generate_pdf(filteredStudentsCM,promotion)  
            self.infoLabel.setText("L'étudiant {} {} a bien été ajouté à la promotion {} ".format( lastname, firstname, promotion))
        
        except Exception as e:
            print(e)
            self.infoLabel.setText("ERREUR L'étudiant {} {} n'a pas été ajouté à la promotion {} ".format(lastname, firstname, promotion))
            self.infoLabel.setStyleSheet("color: #b74242")

        self.infoLabel.setStyleSheet("color: #43C342")
        QTimer.singleShot(2500, lambda : self.infoLabel.setText("") )
                
        self.findChild(QLineEdit, "student_lastname_input").setText("")
        self.findChild(QLineEdit, "student_firstname_input").setText("")
        self.findChild(QLineEdit, "TD_input").setText("")
        self.findChild(QLineEdit, "TP_input").setText("")
        self.findChild(QComboBox, "civility_combobox").setCurrentIndex(0)
        self.promoComboBox2.setCurrentIndex(0)
        
        return 0
    
    def deleteStudent(self):
        # Supprimer un étudiant de liste d'une promo.
        promotionInput = self.promoComboBox2.currentText()
        lastname = self.findChild(QLineEdit, "student_lastname_input").text().lower()
        firstname = self.findChild(QLineEdit, "student_firstname_input").text().lower()

        tp=""
        td=""

        if lastname == "" or firstname == "" or promotionInput == "Promotion...":
            missing_fields = []

            if promotionInput == "Promotion...":
                missing_fields.append("Promotion")
            if lastname == "":
                missing_fields.append("Nom")
            if firstname == "":
                missing_fields.append("Prénom")

            if len(missing_fields) > 0:
                self.infoLabel.setText("Les champs suivants sont manquants : {} ".format(", ".join(missing_fields)))
            self.infoLabel.setStyleSheet("color: #b74242")
            QTimer.singleShot(2500, lambda : self.infoLabel.setText("") )


            return 0

        found = False 

        for promotion in self.promotionsList:
            if promotion["promotion"] == promotionInput:
                for student in promotion["students"]:
                    if student["lastname"].lower() == lastname and student["firstname"].lower() == firstname:
                        td = student["TD"]
                        tp = student["TP"]     
                        promotion["students"].remove(student)
                        found = True
                        break
                break

        with open('promotions.json', 'w') as outfile:
            json.dump(self.promotionsList, outfile)
        outfile.close()

        newPromotions = []
        with open('promotions.json', 'r') as file:
            newPromotions = json.loads(file.read())
        file.close()


        filteredStudentsCM = sorted(self.filter_students(newPromotions, promotionInput), key=lambda d: d['lastname'])
        filteredStudents = sorted(self.filter_students(newPromotions, promotionInput,td,tp), key=lambda d: d['lastname'])

        if not found:
            self.infoLabel.setText("L'étudiant {} {} n'a pas été trouvé dans la promotion {} ".format(lastname, firstname, promotionInput))
            self.infoLabel.setStyleSheet("color: #b74242")
            QTimer.singleShot(3000, lambda : self.infoLabel.setText("") )
            return 0

        try :
            if td :
                generate_pdf(filteredStudents, promotionInput,"TD"+td)
            if tp :
                generate_pdf(filteredStudents,promotionInput,"TP"+tp)

            generate_pdf(filteredStudentsCM,promotionInput)  
            self.infoLabel.setText("L'étudiant {} {} a bien été supprimé de la promotion {} ".format(lastname, firstname, promotionInput))
            self.infoLabel.setStyleSheet("color: green")
            QTimer.singleShot(2500, lambda : self.infoLabel.setText("") )
        except Exception as e:
            print(e)
            self.infoLabel.setText("ERREUR L'étudiant {} {} n'a pas été supprimé de la promotion {} ".format(lastname, firstname, promotionInput))
            self.infoLabel.setStyleSheet("color: #b74242")
        
        self.findChild(QLineEdit, "student_lastname_input").setText("")
        self.findChild(QLineEdit, "student_firstname_input").setText("")
        self.findChild(QLineEdit, "TD_input").setText("")
        self.findChild(QLineEdit, "TP_input").setText("")
        self.findChild(QComboBox, "civility_combobox").setCurrentIndex(0)
        self.promoComboBox2.setCurrentIndex(0)
        
        return 0

    def convertDate(self, date):
        date = date.replace("lundi", "")
        date = date.replace("mardi", "")
        date = date.replace("mercredi", "")
        date = date.replace("jeudi", "")
        date = date.replace("vendredi", "")
        
        date = date.replace("janvier", "january ")
        date = date.replace("février", "february ")
        date = date.replace("mars", "march ")
        date = date.replace("avril", "april ")
        date = date.replace("mai", "may ")
        date = date.replace("juin", "june ")
        date = date.replace("juillet", "july ")
        date = date.replace("aout", "august ")
        date = date.replace("septembre", "september ")
        date = date.replace("octobre", "october ")
        date = date.replace("novembre", "november ")
        date = date.replace("décembre", "december ")
        return date

    def importPDF(self):
        self.fileName = QFileDialog.getOpenFileName(self, "Importer le PDF", "", "Fichier PDF (*.pdf)")
        self.findChild(QLabel, "import_success_label").show()
        if self.fileName != ("",""):
            self.findChild(QLabel, "import_success_label").setStyleSheet("color: #2c7e2b")
            if(confTheme == "dark" or darkdetect.isDark()):
                self.findChild(QLabel, "import_success_label").setStyleSheet("color: #43c342")
            self.findChild(QLabel, "import_success_label").setText("Import réussi")
            self.checkPDF()
        else:
            self.findChild(QLabel, "import_success_label").setStyleSheet("color: #7e2b2b")
            if(confTheme == "dark" or darkdetect.isDark()):
                self.findChild(QLabel, "import_success_label").setStyleSheet("color: #bd4141")
            self.findChild(QLabel, "import_success_label").setText("Import échoué/annulé")

    def checkPDF(self):
        time.sleep(0.3)
        self.tableStudents.setRowCount(0)
        self.loadingOcr.setText("Détection en cours...") 
        self.loadingOcr.setStyleSheet("color: #429cb7")
        self.loadingOcr.update()
        self.loadingOcr.repaint()
        try : 
            self.data = detectAbsent(self.fileName[0],self.low,self.high)
        except Exception as e:
            print(e)
            self.loadingOcr.setText("Erreur lors de la détection.")
            self.loadingOcr.setStyleSheet("color: #b74242")
            return 0
        self.loadingOcr.hide()

        """self.loadingOcr.setText("Détection terminé")
        self.loadingOcr.setStyleSheet("color: #2c7e2b")
        if(confTheme == "dark" or darkdetect.isDark()):
            self.loadingOcr.setStyleSheet("color: #43c342")
        QTimer.singleShot(3000, lambda : self.loadingOcr.hide())"""

        self.currentPage = 0
        self.fillQTableStudent("first")
        self.findChild(QLabel, "import_success_label").hide()
        self.labelTitle1.show()
        self.labelTitle2.show()
        self.labelTitle3.show()
        self.labelTitle4.show()
        self.labelStat1.show()
        self.labelStat2.show()
        self.labelStat3.show()
        if(len(self.data)-1 > 0):
            self.findChild(QPushButton, "next_btn").show()
            self.findChild(QPushButton, "previous_btn").show()
            self.pageTitle.setText("Feuille N° 1")
            self.pageTitle.show()
        self.tableStudents.show()
        self.findChild(QPushButton, "saveScan_btn").show()
        if(self.connect()):
            self.findChild(QPushButton, "saveToDB_btn").show()
        self.importBtn.setText("IMPORTER UN AUTRE PDF")
        return 0

    def fillQTableStudent(self,index):
        self.aSigne = 0
        self.nonSigne = 0
        self.aVerifie = 0
        #iterate over the different lessons        
        if(index == "next"):
            if(self.currentPage < len(self.data)-1):
                self.currentPage += 1
                self.pageTitle.setText("Feuille N° "+str(self.currentPage+1))
            else:
                lesson = self.data[self.currentPage]
                self.pageTitle.setText("Feuille N° "+str(self.currentPage+1))
            lesson = self.data[self.currentPage]
        elif(index == "previous"):
            if(self.currentPage > 0):
                self.currentPage -= 1
                self.pageTitle.setText("Feuille N° "+str(self.currentPage-1))
            else:
                lesson = self.data[self.currentPage]
                self.pageTitle.setText("Feuille N° "+str(self.currentPage-1))
        else:
            lesson = self.data[0]
            self.pageTitle.setText("Feuille N° 1")
        self.lessInfo=lesson["lessonInfo"]
        self.studInfo=lesson["studentsInfo"]

        #iterate over the different students of the lesson
        for d in self.studInfo:
            rowPosition = self.tableStudents.rowCount()
            self.tableStudents.insertRow(rowPosition)
            item = QTableWidgetItem(d["student"].rstrip())
            item2 = QTableWidgetItem(str(round(d["probaOfSignature"],2))+"%")
            color = "#f07b07"
            if(d["hasSigned"]) :
                item3= QTableWidgetItem("Oui")
            else :
                item3=QTableWidgetItem("Non")
            if(d["probaOfSignature"] < self.high and d["probaOfSignature"] > self.low): #Orange color for unsure signature
                item.setForeground(QColor(color))
                item2.setForeground(QColor(color))
                item3.setForeground(QColor(color))

                #add a check button if signature is suspicous
                if(d["verifie"] == False):
                    btnVerif = QPushButton()
                    btnVerif.button_text = "Vérifier!"
                    btnVerif.data = [self.studInfo.index(d),d["student"].rstrip(),d["hasSigned"],d["probaOfSignature"],d["proof"]]
                    btnVerif.setIcon(QIcon("./QtInterface/assets/icons/search.png"))
                    btnVerif.setIconSize(QSize(25,25))
                    btnVerif.clicked.connect(self.on_btnVerif_clicked)
                    self.tableStudents.setCellWidget(rowPosition, 3, btnVerif)
                    self.aVerifie += 1
            elif(d["probaOfSignature"] < self.high): #Red color for students who have not signed
                color = "#7e2b2b"
                if(confTheme == "dark" or darkdetect.isDark()):
                    color = "#bd4141"
                if(d["verifie"]):
                    self.nonSigne += 1
                else:
                    self.nonSigne += 1
            else: #Green color for students who have signed
                color = "#2c7e2b"
                if(confTheme == "dark" or darkdetect.isDark()):
                    color = "#43c342"
                if(d["verifie"]):
                    self.aSigne += 1
                else:
                    self.aSigne += 1
            
            #set the color for the items
            item.setForeground(QColor(color))
            item2.setForeground(QColor(color))
            item3.setForeground(QColor(color))
            
            #display items
            self.tableStudents.setItem(rowPosition, 0, item)
            self.tableStudents.setItem(rowPosition, 1, item3)
            self.tableStudents.setItem(rowPosition, 2, item2)
            self.labelStat1.setStyleSheet("color: #2c7e2b")
            if(confTheme == "dark" or darkdetect.isDark()):
                self.labelStat1.setStyleSheet("color: #43c342")
            self.labelStat1.setText(str(self.aSigne)+" ÉTUDIANTS ONT SIGNÉ.")
            self.labelStat2.setStyleSheet("color: #7e2b2b")
            if(confTheme == "dark" or darkdetect.isDark()):
                self.labelStat2.setStyleSheet("color: #bd4141")
            self.labelStat2.setText(str(self.nonSigne)+" N'ONT PAS SIGNÉ.")
            self.labelStat3.setStyleSheet("color: #f07b07")
            self.labelStat3.setText(str(self.aVerifie)+" À VÉRIFIER.")

            enseignant = self.lessInfo['enseignant'].strip()
            ue = self.lessInfo['ue']
            self.lessInfo['promo'] = self.lessInfo['promo'].replace(",", "")
            promo = self.lessInfo['promo']
            self.lessInfo['date'] = self.lessInfo['date'].replace(" -", "-")
            locale.setlocale(locale.LC_ALL, 'en_US')
            date = self.lessInfo['date']    
            hours = date[-11:]   
            date = date[:-12]
            date = self.convertDate(date)
            date = date[1:]
            date_obj = datetime.strptime(date, "%d %B %Y")
            date = date_obj.strftime("%d/%m/%Y")
            date += " "+hours
            locale.setlocale(locale.LC_ALL, 'fr_FR')
            #date = self.lessInfo['date']
            self.labelTitle1.setText(enseignant)
            self.labelTitle2.setText(ue)
            self.labelTitle3.setText(date)
            self.labelTitle4.setText(promo)
        return 0

    def clearQTableStudent(self):
        self.tableStudents.setRowCount(0)
        return 0

    def next_btn(self):
        self.clearQTableStudent()
        self.fillQTableStudent('next')
        return 0

    def previous_btn(self):
        self.clearQTableStudent()
        self.fillQTableStudent('prev')
        return 0
    
    def saveScan(self):
        self.fileName = QFileDialog.getSaveFileName(self, "Exporter vers", "", "Fichier XLSX (*.xlsx)")
        if self.fileName != ("",""):
            to_excel(self.data, self.fileName)
        return 0

    def saveToDB(self):
        db = mysql.connector.connect(host="45.13.252.103", user="u252758484_d84LF", passwd="EOg=eiRZ*5v", db="u252758484_2ZPML")
        #db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", db="signchecker")
        cursor = db.cursor()
        # Insertion des Etudiants n'étant pas encore dans la base de données
        
        self.lessInfo['promo'] = self.lessInfo['promo'][6:]
        if(self.lessInfo['promo'][:2]== "Ml"):
            self.lessInfo['promo'] = "M1"+self.lessInfo['promo'][2:]
        
        for d in self.studInfo:
            req = "INSERT INTO `etudiant` (`nomEtu`, `promo`) SELECT '"+d["student"].rstrip()+"', '"+self.lessInfo['promo']+"' WHERE NOT EXISTS (SELECT * FROM etudiant WHERE nomEtu = '"+d["student"].rstrip()+"' AND promo = '"+self.lessInfo['promo']+"');"
            cursor.execute(req)
        db.commit()
        
        # Insertion de l'Enseignant n'étant pas encore dans la base de données
        req = "INSERT INTO `enseignant` (`nomEns`) SELECT '"+self.lessInfo['enseignant']+"' WHERE NOT EXISTS (SELECT * FROM enseignant WHERE nomEns = '"+self.lessInfo['enseignant']+"');"
        cursor.execute(req)
        db.commit()

        # Insertion de la Matiere n'étant pas encore dans la base de données
        eu = self.lessInfo['ue'].replace("'", " ")
        req = "INSERT INTO `matiere` (`nomMat`) SELECT '"+eu+"' WHERE NOT EXISTS (SELECT * FROM matiere WHERE nomMat = '"+eu+"');"
        cursor.execute(req)
        db.commit()

        # Insertion du lien entre un Enseignant et une Matiere dans la base de données (si pas encore existant)
        req = "SELECT idEns FROM enseignant WHERE nomEns = '"+self.lessInfo['enseignant']+"';" # last inserted id
        cursor.execute(req)
        idEns = cursor.fetchone()[0]
        req = "SELECT idMat FROM matiere WHERE nomMat = '"+eu+"';" # last inserted id
        cursor.execute(req)
        idMat = cursor.fetchone()[0]
        req = "INSERT INTO `enseigner` (`idEnsEnsr`, `idMatEnsr`) SELECT "+str(idEns)+","+str(idMat)+" WHERE NOT EXISTS (SELECT * FROM enseigner WHERE idEnsEnsr = "+str(idEns)+" AND idMatEnsr = "+str(idMat)+");"
        cursor.execute(req)
        db.commit()
        
        # Insertion des absences dans la base de données
        locale.setlocale(locale.LC_ALL, 'en_US')
        date = self.lessInfo['date']        
        date = date[:-12]
        date = self.convertDate(date)
        date = date[1:]
        date_obj = datetime.strptime(date, "%d %B %Y")
        date = date_obj.strftime("%Y-%m-%d")
        seance = "td" # A changer en fonction du type de séance
        duree = 120 # A changer en fonction de la durée de la séance
        locale.setlocale(locale.LC_ALL, 'fr_FR')
        for d in self.studInfo:
            try :
                if(d["hasSigned"]==False):
                    req = "SELECT idEtu FROM etudiant WHERE nomEtu = '"+d['student']+"';"
                    cursor.execute(req)
                    idEtu = cursor.fetchone()[0]
                    req = "INSERT INTO `absence` (`etuAbs`, `matAbs`, `dateAbs`, `seance`, `duree`) SELECT "+str(idEtu)+", "+str(idMat)+", '"+date+"', '"+seance+"', "+str(duree)+" WHERE NOT EXISTS (SELECT * FROM absence WHERE idAbs = "+str(idEtu)+" AND idAbs = "+str(idMat)+" AND dateAbs = "+date+" AND seance = '"+seance+"' AND duree = "+str(duree)+");"
                    cursor.execute(req)
            except Exception as e:
                 print(e)
                 pass
        db.commit()
        
        # Fin des insetions
        db.close()
        cursor.close()

    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            btn.setAutoExclusive(True)

    def on_home_btn_clicked(self):
        self.ui.main.setCurrentIndex(0)
    def on_export_btn_clicked(self):
        self.ui.main.setCurrentIndex(1)
    def on_import_btn_clicked(self):
        self.ui.main.setCurrentIndex(2)
    def on_config_btn_clicked(self):
        self.ui.main.setCurrentIndex(4)

    def on_btnVerif_clicked(self):
        self.ui.main.setCurrentIndex(3)
        #self.findChild(QWidget, "widget_manualCheck").show()
        self.findChild(QLabel, "proofImage_label").setPixmap(QPixmap(self.sender().data[4]))
        self.findChild(QLabel, "proofStudent_label").setText("Étudiant : "+self.sender().data[1])
        if(self.sender().data[2]) :
            self.findChild(QLabel, "proofSign_label").setText("A signé : Oui")
        else :
            self.findChild(QLabel, "proofSign_label").setText("A signé : Non")
        self.findChild(QLabel, "proofSure_label").setText("Fiabilité : "+str(round(self.sender().data[3],2))+"%")
        self.studentIndex = self.sender().data[0]

    def returnFromCheck(self):
        self.ui.main.setCurrentIndex(2)
        #self.findChild(QWidget, "widget_manualCheck").hide()

    def refuseCheck(self):
        item = QTableWidgetItem("Non")
        item.setForeground(QColor("#7e2b2b"))
        if(confTheme == "dark" or darkdetect.isDark()):
            item.setForeground(QColor("#bd4141"))
        self.tableStudents.setItem(self.studentIndex, 1, item)
        self.tableStudents.removeCellWidget(self.studentIndex, 3)
        self.studInfo[self.studentIndex]["hasSigned"] = False
        self.studInfo[self.studentIndex]["verifie"] = True
        self.nonSigne += 1
        self.aVerifie -= 1
        self.labelStat2.setText(str(self.nonSigne)+" N'ONT PAS SIGNÉ.")
        self.labelStat3.setText(str(self.aVerifie)+" À VÉRIFIER.")
        self.returnFromCheck()

    def validateCheck(self):
        item = QTableWidgetItem("Oui")
        item.setForeground(QColor("#2c7e2b"))
        if(confTheme == "dark" or darkdetect.isDark()):
            item.setForeground(QColor("#43c342"))
        self.tableStudents.setItem(self.studentIndex, 1, item)
        self.tableStudents.removeCellWidget(self.studentIndex, 3)
        self.studInfo[self.studentIndex]["hasSigned"] = True
        self.studInfo[self.studentIndex]["verifie"] = True
        self.aSigne += 1
        self.aVerifie -= 1
        self.labelStat1.setText(str(self.aSigne)+" ÉTUDIANTS ONT SIGNÉ.")
        self.labelStat3.setText(str(self.aVerifie)+" À VÉRIFIER.")
        self.returnFromCheck()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Import QSS
    with open("QtInterface/QSS/style.qss", "r") as stylesheet:
        style_str = stylesheet.read()
    #if(darkdetect.isDark()):
    if(confTheme == "dark" or darkdetect.isDark()):
        with open("QtInterface/QSS/dark.qss", "r") as stylesheet:
            style_str_2 = stylesheet.read()
        app.setStyleSheet(style_str+style_str_2)
    if(confTheme == "light" or darkdetect.isLight()):
        app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())