# -*- coding: utf-8 -*-
import os
import sqlite3
from fixed_file import folder_data
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from fpdf import FPDF

class Ui_MainWindow(object):
    data_users = os.path.join(folder_data, "users.bd")
    
    def window_add_user(self):
        self.stackedWidget.setCurrentWidget(self.add_user)
        
    def window_list_user(self):
        self.stackedWidget.setCurrentWidget(self.display_user)
        self.display_user_list()
        
    def creation_data_base(self):
        conn = sqlite3.connect(Ui_MainWindow.data_users)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            last_name TEXT,
            first_name TEXT,
            age INTERGER)""")
        conn.commit()
        conn.close()

    def recording_user(self):
        last_name = self.enter_last_name.text()
        first_name = self.enter_first_name.text()
        age = self.enter_age.text()
        ENTERS = [self.enter_last_name, self.enter_first_name, self.enter_age]
        
        d = {
            "last_name": last_name,
            "first_name": first_name,
            "age": age
        }
        
        if (last_name and first_name and age and 
            not last_name.isspace() and not first_name.isspace() and not age.isspace()) :
            conn = sqlite3.connect(Ui_MainWindow.data_users)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users VALUES (:last_name, :first_name, :age)", d)
            conn.commit()
            conn.close()
            for enter in ENTERS: enter.clear()
            self.msgQuestion = QMessageBox()
            self.msgQuestion.setWindowTitle("Vous fevez d'enregistrer un utilisateur")
            self.msgQuestion.setText("L'utilateur vient d'être enregistré")
            self.msgQuestion.setStandardButtons(QMessageBox.Ok)
            self.msgQuestion.show()         
        else:
            self.msgQuestion = QMessageBox()
            self.msgQuestion.setWindowTitle("Erreur d'enregistrement")
            self.msgQuestion.setText("Impossble d'enregistrer l'utilisateur. Veuillez vérifier les informations")
            self.msgQuestion.setStandardButtons(QMessageBox.Ok)
            self.msgQuestion.show() 
    
    def get_data(self):
        conn = sqlite3.connect(Ui_MainWindow.data_users)
        cursor = conn.cursor()
        data = cursor.execute("SELECT * FROM users").fetchall()
        conn.commit()
        conn.close()
        
        return data
        
    def display_user_list(self):
        users = self.get_data()
        
        pdf = FPDF("P", "cm", "LETTER")
        pdf.add_page()
        pdf.set_font("helvetica", "", 14)

        pdf.cell(4.5, 1, "N°")
        pdf.cell(4.5, 1, "Nom")
        pdf.cell(4.5, 1, "Prénom")
        pdf.cell(4.5, 1, "Age", ln=1)

        for i in range(100):
            #last
            pdf.cell(4.5, 1, "1", border=True,)
            pdf.cell(4.5, 1, "Afri", border=True,)
            pdf.cell(4.5, 1, "Kréto", border=True,)
            pdf.cell(4.5, 1, "19", border=True, ln=1)

            pdf.output("test.pdf")
    
    def create_pdf(self):
        print("oui")
        # users = self.get_data()
        # users = [list(user) for user in users]
        # users = [user.append("Abidjan") for user in users]
        
        # print(users)
        
        data = [
            ["First name", "Last name", "Age", "City",], # 'testing','size'],
            ["Jules", "Smith", "34", "San Juan",], # 'testing','size'],
            ["Mary", "Ramos", "45", "Orlando",], # 'testing','size'],
            ["Carlson", "Banks", "19", "Los Angeles",], # 'testing','size'],
            ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire",], # 'testing','size'],
        ]
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Times", size=10)

        pdf.create_table(table_data = data,title='I\'m the first title', cell_width='even')
        pdf.ln()
        print("FIn")
        
        
        
        


    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 891, 421))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.add_user = QtWidgets.QWidget()
        self.add_user.setObjectName("add_user")
        self.label = QtWidgets.QLabel(self.add_user)
        self.label.setGeometry(QtCore.QRect(340, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.enter_last_name = QtWidgets.QLineEdit(self.add_user)
        self.enter_last_name.setGeometry(QtCore.QRect(350, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.enter_last_name.setFont(font)
        self.enter_last_name.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"padding: 10;")
        self.enter_last_name.setObjectName("enter_last_name")
        self.enter_first_name = QtWidgets.QLineEdit(self.add_user)
        self.enter_first_name.setGeometry(QtCore.QRect(350, 160, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.enter_first_name.setFont(font)
        self.enter_first_name.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"padding: 10;")
        self.enter_first_name.setObjectName("enter_first_name")
        self.enter_age = QtWidgets.QLineEdit(self.add_user)
        self.enter_age.setGeometry(QtCore.QRect(350, 220, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.enter_age.setFont(font)
        self.enter_age.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"padding: 10;")
        self.enter_age.setObjectName("enter_age")
        self.button_add = QtWidgets.QPushButton(self.add_user)
        self.button_add.clicked.connect(self.recording_user)
        self.button_add.setGeometry(QtCore.QRect(350, 300, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton#button_add {\n"
"border: 2px solid white;\n"
"background-color: rgb(0, 251, 22);\n"
"color: white;\n"
"border-radius: 3px; \n"
"}\n"
"\n"
"")
        self.button_add.setObjectName("button_add")
        self.stackedWidget.addWidget(self.add_user)
        self.display_user = QtWidgets.QWidget()
        self.display_user.setObjectName("display_user")
        self.list_users = QtWidgets.QTableWidget(self.display_user)
        self.list_users.move(70, 80)
        self.list_users.setFixedSize(500, 150)
        self.list_users.setObjectName("list_users")
        self.list_users.setStyleSheet("""
            QtWidgets#list_users{
                border: 1px solid black;
            }
        """)
        self.label_2 = QtWidgets.QLabel(self.display_user)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.display_user)
        self.add_user_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_2.clicked.connect(self.window_add_user)
        self.add_user_2.setGeometry(QtCore.QRect(60, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.add_user_2.setFont(font)
        self.add_user_2.setObjectName("add_user_2")
        self.display_users_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.display_users_pdf.clicked.connect(self.window_list_user)
        self.display_users_pdf.setGeometry(QtCore.QRect(320, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.display_users_pdf.setFont(font)
        self.display_users_pdf.setObjectName("display_users_pdf")
        self.add_user_4 = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_4.setGeometry(QtCore.QRect(620, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.add_user_4.setFont(font)
        self.add_user_4.setObjectName("add_user_4")
        self.add_user_4.clicked.connect(self.create_pdf)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ajouter un utilisateur"))
        self.enter_last_name.setPlaceholderText(_translate("MainWindow", "Entrer le nom"))
        self.enter_first_name.setPlaceholderText(_translate("MainWindow", "Entrer le prénom"))
        self.enter_age.setPlaceholderText(_translate("MainWindow", "Entrer l\'age"))
        self.button_add.setText(_translate("MainWindow", "Ajouter l\'utilisateur"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.add_user_2.setText(_translate("MainWindow", "Ajouter un utilisateur"))
        self.display_users_pdf.setText(_translate("MainWindow", "Voir la liste des utilisateurs"))
        self.add_user_4.setText(_translate("MainWindow", "Voir le pdf"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.creation_data_base()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
