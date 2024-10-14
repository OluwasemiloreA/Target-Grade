from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os
from TargetGrade import Ui_TGWindow

class Ui_loginWindow(object):
    ## __init__ is the constructor
    ## It is called when you call Ui_loginWindow() in __main__ below
    def __init__(self):
        # Define the directory path where you want to store the files
        self.user_file = os.path.abspath('./TGD/details')

        ## Check if user file exists, if it does store the username and password
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as f:
                # Read lines from the details file
                # Take all characters except the last one because the lines end in
                # the new line character '\n'
                self.username = f.readline()[:-1]
                self.password = f.readline()[:-1]
        else:
            message = QMessageBox()
            message.setText("Create a username and password then click 'Submit'. Be careful though as this will be your username and password permanently so make sure you write it down!")
            message.exec()

    def SetUpUi(self, loginWindow):
        #Sets window characteristics
        self.loginwindow = loginWindow
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(451, 453)
        loginWindow.setMinimumSize(QtCore.QSize(451, 363))
        loginWindow.setMaximumSize(QtCore.QSize(11123456, 1234567))
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.CheckPasskey())
        self.submit_button.setGeometry(QtCore.QRect(150, 350, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.submit_button.setPalette(palette)
        self.submit_button.setStyleSheet("")
        self.submit_button.setObjectName("submit_button")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 130, 491, 181))
        self.frame.setStyleSheet("background-color: rgb(243, 235, 122);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pword = QtWidgets.QLabel(self.frame)
        self.pword.setGeometry(QtCore.QRect(80, 100, 131, 41))
        self.pword.setObjectName("pword")
        self.pword_inp = QtWidgets.QLineEdit(self.frame)
        self.pword_inp.setGeometry(QtCore.QRect(240, 100, 141, 41))
        self.pword_inp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pword_inp.setText("")
        self.pword_inp.setObjectName("pword_inp")
        self.uname = QtWidgets.QLabel(self.frame)
        self.uname.setGeometry(QtCore.QRect(80, 40, 131, 41))
        self.uname.setObjectName("uname")
        self.uname_inp = QtWidgets.QLineEdit(self.frame)
        self.uname_inp.setGeometry(QtCore.QRect(240, 40, 141, 41))
        self.uname_inp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.uname_inp.setText("")
        self.uname_inp.setObjectName("uname_inp")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-21, -1, 491, 461))
        self.frame_2.setStyleSheet("background-color: rgb(0, 150, 200);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setGeometry(QtCore.QRect(100, 30, 281, 61))
        self.title.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.title.setObjectName("title")
        self.frame_2.raise_()
        self.frame.raise_()
        self.submit_button.raise_()
        loginWindow.setCentralWidget(self.centralwidget)

        self.RetranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def RetranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Target Grade"))
        self.submit_button.setText(_translate("loginWindow", "Submit"))
        self.pword.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Password:</span></p></body></html>"))
        self.pword_inp.setPlaceholderText(_translate("loginWindow", "Enter Password"))
        self.uname.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Username:</<span></span></p></body></html>"))
        self.uname_inp.setPlaceholderText(_translate("loginWindow", "Enter Username"))
        self.title.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Log In</span></p></body></html>"))

    #function to Check for and/or Validate username and password
    def CheckPasskey(self):
        message = QMessageBox()
        passValue = self.pword_inp.text()
        usernameValue = self.uname_inp.text()

        if usernameValue == '' and passValue == '':
            message.setText("Empty username and password")
            message.exec()
            return
        if usernameValue == '':
            message.setText("Empty username")
            message.exec()
            return
        if passValue == '':
            message.setText("Empty password")
            message.exec()
            return

        if os.path.exists(self.user_file):
            # Check if the input username and password match those of the details file
            if self.username != usernameValue and self.password != passValue:
                message.setText("Invalid username and password")
                message.exec()
                return
            if self.username != usernameValue:
                message.setText("Invalid username")
                message.exec()
                return
            if self.password != passValue:
                message.setText("Invalid password")
                message.exec()
                return
        else:
            # Otherwise make the details file
            directory = os.path.dirname(self.user_file)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(self.user_file, 'x') as f:
                # Add a trailing new line for easier processing
                f.write(usernameValue +'\n' + passValue + '\n')

        self.OpenMain()


    def OpenMain(self):
        #Creates Main Window 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TGWindow()
        self.loginwindow.hide()
        self.ui.SetUpUi(self.window)
        self.window.show()


if __name__ == "__main__":
    #Launch procedure
    import sys
    app = QtWidgets.QApplication(sys.argv)
    message = QMessageBox()
    Loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.SetUpUi(Loginwindow)
    Loginwindow.show()
    sys.exit(app.exec_())

