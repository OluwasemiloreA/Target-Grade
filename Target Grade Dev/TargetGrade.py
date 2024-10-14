import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from pathlib import Path
import numpy as np
import os
from matplotlib.figure import Figure

#asigns each label a value 
DICT_VALUES = {
"U (0 points)" : 0, "E (16 points)" : 16, "D (24 points)" : 24, "C (32 points)" : 32, "B (40 points)" : 40, "A (48 points)" : 48, "A* (56 points)" : 56
}

#predicted ucas points 
POINTS_PREDICT = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">%s</span></p></body></html>"
#predicted Grades
GRADE_PREDICT = "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">%s</span></p></body></html>"


class Ui_TGWindow(object):
    def __init__(self):
       self.filenames = ['','','','']
       if not os.path.exists('./TGD/Subjects'):
          self.subject_file = os.mkdir('./TGD/Subjects')
       else:
          self.subject_file = Path('./TGD/Subjects')


    def SetUpUi(self, TGWindow):
        TGWindow.setObjectName("TGWindow")
        TGWindow.resize(997, 551)
        TGWindow.setMinimumSize(QtCore.QSize(705, 395))
        TGWindow.setMaximumSize(QtCore.QSize(12345678, 16777215))
        TGWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        TGWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(TGWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-10, 0, 1101, 581))
        self.graphicsView.setMinimumSize(QtCore.QSize(741, 421))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView.setPalette(palette)
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setInteractive(False)
        self.graphicsView.setObjectName("graphicsView")
        self.FrameA = QtWidgets.QGraphicsView(self.centralwidget)
        self.FrameA.setGeometry(QtCore.QRect(30, 20, 451, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.FrameA.setPalette(palette)
        self.FrameA.setAutoFillBackground(False)
        self.FrameA.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.FrameA.setObjectName("FrameA")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(510, 20, 461, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setMidLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        #creating horizontal layout
        #creates canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        #add canvas
        self.predict_points_label = QtWidgets.QLabel(self.centralwidget)
        self.predict_points_label.setGeometry(QtCore.QRect(590, 460, 301, 45))
        self.predict_points_label.setObjectName("predict_points_label")
        self.FrameD = QtWidgets.QGraphicsView(self.centralwidget)
        self.FrameD.setGeometry(QtCore.QRect(510, 284, 461, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.FrameD.setPalette(palette)
        self.FrameD.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.FrameD.setObjectName("FrameD")
        self.predict_label = QtWidgets.QLabel(self.centralwidget)
        self.predict_label.setGeometry(QtCore.QRect(590, 330, 301, 100))
        self.predict_label.setObjectName("predict_label")
        self.current_predict_label = QtWidgets.QLabel(self.centralwidget)
        self.current_predict_label.setGeometry(QtCore.QRect(565, 300, 351, 51))
        self.current_predict_label.setObjectName("current_predict_label")
        self.Ucas_pred_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Ucas_pred_label_2.setGeometry(QtCore.QRect(550, 420, 380, 41))
        self.Ucas_pred_label_2.setObjectName("Ucas_pred_label_2")
        self.Grade_Box_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Grade_Box_1.setGeometry(QtCore.QRect(260, 310, 171, 31))
        self.Grade_Box_1.setObjectName("Grade_Box_1")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_1.addItem("")
        self.Grade_Box_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Grade_Box_2.setGeometry(QtCore.QRect(260, 350, 171, 31))
        self.Grade_Box_2.setObjectName("Grade_Box_2")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Grade_Box_2.addItem("")
        self.Subject_Box_3 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject_Box_3.setGeometry(QtCore.QRect(70, 390, 161, 31))
        self.Subject_Box_3.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.Subject_Box_3.setObjectName("Subject_Box_3")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_3.addItem("")
        self.Subject_Box_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject_Box_2.setGeometry(QtCore.QRect(70, 350, 161, 31))
        self.Subject_Box_2.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.Subject_Box_2.setObjectName("Subject_Box_2")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_2.addItem("")
        self.Subject_Box_4 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject_Box_4.setGeometry(QtCore.QRect(70, 430, 161, 31))
        self.Subject_Box_4.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.Subject_Box_4.setObjectName("Subject_Box_4")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.Subject_Box_4.addItem("")
        self.FrameC = QtWidgets.QGraphicsView(self.centralwidget)
        self.FrameC.setGeometry(QtCore.QRect(30, 284, 451, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.FrameC.setPalette(palette)
        self.FrameC.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.FrameC.setObjectName("FrameC")
        self.Grade_Box_4 = QtWidgets.QComboBox(self.centralwidget)
        self.Grade_Box_4.setGeometry(QtCore.QRect(260, 430, 171, 31))
        self.Grade_Box_4.setObjectName("Grade_Box_4")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_4.addItem("")
        self.Grade_Box_3 = QtWidgets.QComboBox(self.centralwidget)
        self.Grade_Box_3.setGeometry(QtCore.QRect(260, 390, 171, 31))
        self.Grade_Box_3.setObjectName("Grade_Box_3")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.Grade_Box_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.WriteToFile)
        self.pushButton.setGeometry(QtCore.QRect(200, 480, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 233, 121))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 233, 121))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 235, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.Subject_Box_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject_Box_1.setGeometry(QtCore.QRect(70, 310, 161, 31))
        self.Subject_Box_1.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.Subject_Box_1.setObjectName("Subject_Box_1")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.Subject_Box_1.addItem("")
        self.graphicsView.raise_()
        self.FrameC.raise_()
        self.FrameD.raise_()
        self.FrameA.raise_()
        self.textEdit.raise_()
        self.predict_points_label.raise_()
        self.predict_label.raise_()
        self.current_predict_label.raise_()
        self.Ucas_pred_label_2.raise_()
        self.Grade_Box_1.raise_()
        self.Grade_Box_2.raise_()
        self.Subject_Box_3.raise_()
        self.Subject_Box_2.raise_()
        self.Subject_Box_4.raise_()
        self.Grade_Box_4.raise_()
        self.Grade_Box_3.raise_()
        self.pushButton.raise_()
        self.Subject_Box_1.raise_()
        TGWindow.setCentralWidget(self.centralwidget)
        self.actionasd = QtWidgets.QAction(TGWindow)
        self.actionasd.setObjectName("actionasd")
        self.actionsad = QtWidgets.QAction(TGWindow)
        self.actionsad.setObjectName("actionsad")
        self.actionasd_2 = QtWidgets.QAction(TGWindow)
        self.actionasd_2.setObjectName("actionasd_2")
        self.actionasd_3 = QtWidgets.QAction(TGWindow)
        self.actionasd_3.setObjectName("actionasd_3")
        self.actionasd_4 = QtWidgets.QAction(TGWindow)
        self.actionasd_4.setObjectName("actionasd_4")
        self.actionasd_5 = QtWidgets.QAction(TGWindow)
        self.actionasd_5.setObjectName("actionasd_5")
        self.actionasdd = QtWidgets.QAction(TGWindow)
        self.actionasdd.setObjectName("actionasdd")
        self.actionasd_6 = QtWidgets.QAction(TGWindow)
        self.actionasd_6.setObjectName("actionasd_6")
        self.actionas = QtWidgets.QAction(TGWindow)
        self.actionas.setObjectName("actionas")
        self.actionGrade_input = QtWidgets.QAction(TGWindow)
        self.actionGrade_input.setEnabled(True)
        self.actionGrade_input.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionGrade_input.setObjectName("actionGrade_input")
        self.actionPoints_calculator = QtWidgets.QAction(TGWindow)
        self.actionPoints_calculator.setObjectName("actionPoints_calculator")
        self.actionGrade_Projections = QtWidgets.QAction(TGWindow)
        self.actionGrade_Projections.setObjectName("actionGrade_Projections")

        self.RetranslateUi(TGWindow)
        QtCore.QMetaObject.connectSlotsByName(TGWindow)

    def RetranslateUi(self, TGWindow):
        _translate = QtCore.QCoreApplication.translate
        TGWindow.setWindowTitle(_translate("TGWindow", "Target Grade"))
        self.textEdit.setHtml(_translate("TGWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift SemiBold\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Target Grade</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">Welcome to Target Grade; a grade tracking software for A levels made for students by students.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:400;\">Instructions:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">Choose subject names and grades using the drop down menu in the bottom left. Press the record button when finished and the graph of your current results and predicted results will be displayed. \nThese grades and your current and predicted UCAS points score will be displayed in the bottom right.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">Come back after every test to track your preperation for your A Levels in May.</span></p></body></html>"))
        ############################################################################################################
        self.predict_points_label.setText(_translate("TGWindow", POINTS_PREDICT%'XXX'))
        self.predict_label.setText(_translate("TGWindow", GRADE_PREDICT%'XXX'))
        self.current_predict_label.setText(_translate("TGWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:13pt; font-weight:600;\">Your Current Predicted Grades:</span></p></body></html>"))
        self.Ucas_pred_label_2.setText(_translate("TGWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Your Current Predicted UCAS Points:</span></p></body></html>"))
        self.Grade_Box_1.setItemText(0, _translate("TGWindow", "Select a Grade"))
        self.Grade_Box_1.setItemText(1, _translate("TGWindow", "A* (56 points)"))
        self.Grade_Box_1.setItemText(2, _translate("TGWindow", "A (48 points)"))
        self.Grade_Box_1.setItemText(3, _translate("TGWindow", "B (40 points)"))
        self.Grade_Box_1.setItemText(4, _translate("TGWindow", "C (32 points)"))
        self.Grade_Box_1.setItemText(5, _translate("TGWindow", "D (24 points)"))
        self.Grade_Box_1.setItemText(6, _translate("TGWindow", "E (16 points)"))
        self.Grade_Box_1.setItemText(7, _translate("TGWindow", "U (0 points)"))
        self.Grade_Box_2.setItemText(0, _translate("TGWindow", "Select a Grade"))
        self.Grade_Box_2.setItemText(1, _translate("TGWindow", "A* (56 points)"))
        self.Grade_Box_2.setItemText(2, _translate("TGWindow", "A (48 points)"))
        self.Grade_Box_2.setItemText(3, _translate("TGWindow", "B (40 points)"))
        self.Grade_Box_2.setItemText(4, _translate("TGWindow", "C (32 points)"))
        self.Grade_Box_2.setItemText(5, _translate("TGWindow", "D (24 points)"))
        self.Grade_Box_2.setItemText(6, _translate("TGWindow", "E (16 points)"))
        self.Grade_Box_2.setItemText(7, _translate("TGWindow", "U (0 points)"))
        self.Subject_Box_3.setItemText(0, _translate("TGWindow", "Select a subject"))
        self.Subject_Box_3.setItemText(1, _translate("TGWindow", "Art"))
        self.Subject_Box_3.setItemText(2, _translate("TGWindow", "Biology"))
        self.Subject_Box_3.setItemText(3, _translate("TGWindow", "Business"))
        self.Subject_Box_3.setItemText(4, _translate("TGWindow", "Chemistry"))
        self.Subject_Box_3.setItemText(5, _translate("TGWindow", "Computer Science"))
        self.Subject_Box_3.setItemText(6, _translate("TGWindow", "D&T"))
        self.Subject_Box_3.setItemText(7, _translate("TGWindow", "Economics"))
        self.Subject_Box_3.setItemText(8, _translate("TGWindow", "English Language"))
        self.Subject_Box_3.setItemText(9, _translate("TGWindow", "English Literature"))
        self.Subject_Box_3.setItemText(10, _translate("TGWindow", "Further Maths"))
        self.Subject_Box_3.setItemText(11, _translate("TGWindow", "Geography"))
        self.Subject_Box_3.setItemText(12, _translate("TGWindow", "History"))
        self.Subject_Box_3.setItemText(13, _translate("TGWindow", "Languages"))
        self.Subject_Box_3.setItemText(14, _translate("TGWindow", "Maths"))
        self.Subject_Box_3.setItemText(15, _translate("TGWindow", "Music"))
        self.Subject_Box_3.setItemText(16, _translate("TGWindow", "P.E."))
        self.Subject_Box_3.setItemText(17, _translate("TGWindow", "Physics"))
        self.Subject_Box_3.setItemText(18, _translate("TGWindow", "Politics"))
        self.Subject_Box_3.setItemText(19, _translate("TGWindow", "Psychology"))
        self.Subject_Box_3.setItemText(20, _translate("TGWindow", "Religious Studies"))
        self.Subject_Box_2.setItemText(0, _translate("TGWindow", "Select a subject"))
        self.Subject_Box_2.setItemText(1, _translate("TGWindow", "Art"))
        self.Subject_Box_2.setItemText(2, _translate("TGWindow", "Biology"))
        self.Subject_Box_2.setItemText(3, _translate("TGWindow", "Business"))
        self.Subject_Box_2.setItemText(4, _translate("TGWindow", "Chemistry"))
        self.Subject_Box_2.setItemText(5, _translate("TGWindow", "Computer Science"))
        self.Subject_Box_2.setItemText(6, _translate("TGWindow", "D&T"))
        self.Subject_Box_2.setItemText(7, _translate("TGWindow", "Economics"))
        self.Subject_Box_2.setItemText(8, _translate("TGWindow", "English Language"))
        self.Subject_Box_2.setItemText(9, _translate("TGWindow", "English Literature"))
        self.Subject_Box_2.setItemText(10, _translate("TGWindow", "Further Maths"))
        self.Subject_Box_2.setItemText(11, _translate("TGWindow", "Geography"))
        self.Subject_Box_2.setItemText(12, _translate("TGWindow", "History"))
        self.Subject_Box_2.setItemText(13, _translate("TGWindow", "Languages"))
        self.Subject_Box_2.setItemText(14, _translate("TGWindow", "Maths"))
        self.Subject_Box_2.setItemText(15, _translate("TGWindow", "Music"))
        self.Subject_Box_2.setItemText(16, _translate("TGWindow", "P.E."))
        self.Subject_Box_2.setItemText(17, _translate("TGWindow", "Physics"))
        self.Subject_Box_2.setItemText(18, _translate("TGWindow", "Politics"))
        self.Subject_Box_2.setItemText(19, _translate("TGWindow", "Psychology"))
        self.Subject_Box_2.setItemText(20, _translate("TGWindow", "Religious Studies"))
        self.Subject_Box_4.setItemText(0, _translate("TGWindow", "Select a subject"))
        self.Subject_Box_4.setItemText(1, _translate("TGWindow", "Art"))
        self.Subject_Box_4.setItemText(2, _translate("TGWindow", "Biology"))
        self.Subject_Box_4.setItemText(3, _translate("TGWindow", "Business"))
        self.Subject_Box_4.setItemText(4, _translate("TGWindow", "Chemistry"))
        self.Subject_Box_4.setItemText(5, _translate("TGWindow", "Computer Science"))
        self.Subject_Box_4.setItemText(6, _translate("TGWindow", "D&T"))
        self.Subject_Box_4.setItemText(7, _translate("TGWindow", "Economics"))
        self.Subject_Box_4.setItemText(8, _translate("TGWindow", "English Language"))
        self.Subject_Box_4.setItemText(9, _translate("TGWindow", "English Literature"))
        self.Subject_Box_4.setItemText(10, _translate("TGWindow", "Further Maths"))
        self.Subject_Box_4.setItemText(11, _translate("TGWindow", "Geography"))
        self.Subject_Box_4.setItemText(12, _translate("TGWindow", "History"))
        self.Subject_Box_4.setItemText(13, _translate("TGWindow", "Languages"))
        self.Subject_Box_4.setItemText(14, _translate("TGWindow", "Maths"))
        self.Subject_Box_4.setItemText(15, _translate("TGWindow", "Music"))
        self.Subject_Box_4.setItemText(16, _translate("TGWindow", "P.E."))
        self.Subject_Box_4.setItemText(17, _translate("TGWindow", "Physics"))
        self.Subject_Box_4.setItemText(18, _translate("TGWindow", "Politics"))
        self.Subject_Box_4.setItemText(19, _translate("TGWindow", "Psychology"))
        self.Subject_Box_4.setItemText(20, _translate("TGWindow", "Religious Studies"))
        self.Grade_Box_4.setItemText(0, _translate("TGWindow", "Select a Grade"))
        self.Grade_Box_4.setItemText(1, _translate("TGWindow", "A* (56 points)"))
        self.Grade_Box_4.setItemText(2, _translate("TGWindow", "A (48 points)"))
        self.Grade_Box_4.setItemText(3, _translate("TGWindow", "B (40 points)"))
        self.Grade_Box_4.setItemText(4, _translate("TGWindow", "C (32 points)"))
        self.Grade_Box_4.setItemText(5, _translate("TGWindow", "D (24 points)"))
        self.Grade_Box_4.setItemText(6, _translate("TGWindow", "E (16 points)"))
        self.Grade_Box_4.setItemText(7, _translate("TGWindow", "U (0 points)"))
        self.Grade_Box_3.setItemText(0, _translate("TGWindow", "Select a Grade"))
        self.Grade_Box_3.setItemText(1, _translate("TGWindow", "A* (56 points)"))
        self.Grade_Box_3.setItemText(2, _translate("TGWindow", "A (48 points)"))
        self.Grade_Box_3.setItemText(3, _translate("TGWindow", "B (40 points)"))
        self.Grade_Box_3.setItemText(4, _translate("TGWindow", "C (32 points)"))
        self.Grade_Box_3.setItemText(5, _translate("TGWindow", "D (24 points)"))
        self.Grade_Box_3.setItemText(6, _translate("TGWindow", "E (16 points)"))
        self.Grade_Box_3.setItemText(7, _translate("TGWindow", "U (0 points)"))
        self.pushButton.setText(_translate("TGWindow", "Record"))
        self.Subject_Box_1.setItemText(0, _translate("TGWindow", "Select a subject"))
        self.Subject_Box_1.setItemText(1, _translate("TGWindow", "Art"))
        self.Subject_Box_1.setItemText(2, _translate("TGWindow", "Biology"))
        self.Subject_Box_1.setItemText(3, _translate("TGWindow", "Business"))
        self.Subject_Box_1.setItemText(4, _translate("TGWindow", "Chemistry"))
        self.Subject_Box_1.setItemText(5, _translate("TGWindow", "Computer Science"))
        self.Subject_Box_1.setItemText(6, _translate("TGWindow", "D&T"))
        self.Subject_Box_1.setItemText(7, _translate("TGWindow", "Economics"))
        self.Subject_Box_1.setItemText(8, _translate("TGWindow", "English Language"))
        self.Subject_Box_1.setItemText(9, _translate("TGWindow", "English Literature"))
        self.Subject_Box_1.setItemText(10, _translate("TGWindow", "Further Maths"))
        self.Subject_Box_1.setItemText(11, _translate("TGWindow", "Geography"))
        self.Subject_Box_1.setItemText(12, _translate("TGWindow", "History"))
        self.Subject_Box_1.setItemText(13, _translate("TGWindow", "Languages"))
        self.Subject_Box_1.setItemText(14, _translate("TGWindow", "Maths"))
        self.Subject_Box_1.setItemText(15, _translate("TGWindow", "Music"))
        self.Subject_Box_1.setItemText(16, _translate("TGWindow", "P.E."))
        self.Subject_Box_1.setItemText(17, _translate("TGWindow", "Physics"))
        self.Subject_Box_1.setItemText(18, _translate("TGWindow", "Politics"))
        self.Subject_Box_1.setItemText(19, _translate("TGWindow", "Psychology"))
        self.Subject_Box_1.setItemText(20, _translate("TGWindow", "Religious Studies"))
        self.actionasd.setText(_translate("TGWindow", "asd"))
        self.actionsad.setText(_translate("TGWindow", "sad"))
        self.actionasd_2.setText(_translate("TGWindow", "asd"))
        self.actionasd_3.setText(_translate("TGWindow", "asd"))
        self.actionasd_4.setText(_translate("TGWindow", "asd"))
        self.actionasd_5.setText(_translate("TGWindow", "asd"))
        self.actionasdd.setText(_translate("TGWindow", "asdd"))
        self.actionasd_6.setText(_translate("TGWindow", "asd"))
        self.actionas.setText(_translate("TGWindow", "as"))
        self.actionGrade_input.setText(_translate("TGWindow", "Grade input"))
        self.actionPoints_calculator.setText(_translate("TGWindow", "Points calculator"))
        self.actionGrade_Projections.setText(_translate("TGWindow", "Grade Projections"))

    
    def WriteToFile(self):
        #removes redundant data such as empty Grade fields and/or subject fields. stops this from being plotted on thre graph
        def Sanitize(x):
            return '' if x == "Select a Grade" else x   
        def SanitizeSubjects(x):
            return '' if x == "Select a subject" else self.subject_file/x
        
        # Get the selected Grade from the QComboBox
        selected_items = [self.Grade_Box_1.currentText(),self.Grade_Box_2.currentText(),self.Grade_Box_3.currentText(),self.Grade_Box_4.currentText()]  
        selected_items = [Sanitize(x) for x in selected_items]
        filenames = [SanitizeSubjects(self.Subject_Box_1.currentText()),SanitizeSubjects(self.Subject_Box_2.currentText()),SanitizeSubjects(self.Subject_Box_3.currentText()),SanitizeSubjects(self.Subject_Box_4.currentText())]
        
        #adds the subject name and assigned grade to seperate arrays. They are in the same position so will be acssesed together
        Grades = []
        self.filenames = []
        for i in range(4):
            if selected_items[i] != '' and filenames[i] != '':
                Grades.append(selected_items[i])
                self.filenames.append(Path(filenames[i]))



        def LogData(path, data):
            #if the input is redundant then quit
            if path == '':
                return
             
            if os.path.exists(path): 
                # Write the selected item to the file
                with open(path, 'a') as file:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    file.write(','+ data)
            else:
                #Create the new file then write the data in
                directory = os.path.dirname(self.subject_file)
                if not os.path.exists(directory):
                    os.makedirs(directory)

                with open(path, 'x') as f:
                    f.write(data)

        for i in range(len(self.filenames)):
            LogData(self.filenames[i],Grades[i])
        
        self.LaunchGraph()
        self.MakePrediction()
    
    def GetResults(self):
        #Converts the grades into number form
        global DICT_VALUES
        results_arrays = []
        for f in self.filenames:
            with open(f, 'r') as file:
                raw_results = file.read().split(',')
                results_arrays.append([DICT_VALUES[i] for i in raw_results])
        return results_arrays


   
    #graph function
    def LaunchGraph(self):
        global DICT_VALUES
        if len(self.filenames) == 0:
            return
        results_arrays = self.GetResults()  
        total_length = max([len(r) for r in results_arrays])

        #Extrapolates lines for the subjects that have less data than the others
        def DataExtend(nparr):
            last = nparr[-1]
            for i in range(total_length-len(nparr)):
                nparr.append(last)
                

        # continues the line if there is one array that is longer than the others. keeps them all the same length by just repeating the most recent 
        for r in results_arrays:
            DataExtend(r)
 
    
        x = np.arange(1,total_length+1,1)
        ylabels = ['U','E','D','C','B','A','A*']

        #Graph properties
        fig = Figure((4.2,2.2))
        axis = fig.gca()
        for i in range(len(self.filenames)):
            axis.plot(x,results_arrays[i],label = self.filenames[i].name)
        axis.set_yticks(list(DICT_VALUES.values()), ylabels)
        axis.set_xlabel("Number of Scores")
        axis.legend()
        canvas = FigureCanvas(fig)
        scene = QtWidgets.QGraphicsScene()
        self.FrameA.setScene(scene)
        scene.addWidget(canvas)
        self.FrameA.resize(452, 252)
        self.FrameA.show()

    def MakePrediction(self):
        global DICT_VALUES
        if len(self.filenames) == 0:
            return
        all_results = self.GetResults()
        results = [ar[-3:]for ar in all_results]
        raw_predictions = {}
        for i in range(len(results)):
            raw_predictions[self.filenames[i].name] = sum(results[i])//len(results[i])
        #round to nearest grade
        inverted = {v:k for k,v in DICT_VALUES.items()}
        predictions = {}
        for subject,raw_score in raw_predictions.items():
            last = -1
            last_grade = ''
            for score,grade in inverted.items():
                if score < raw_score:
                    last = score
                    last_grade = grade
                    continue
                last_dif = raw_score - last
                next_dif = score - raw_score
                pgrade = grade if next_dif <= last_dif else last_grade 
                predictions[subject] = pgrade
                break
        
        subject_predictions = '<br/>'.join([s+': '+g for s,g in predictions.items()])
        _translate = QtCore.QCoreApplication.translate
        self.predict_label.setText(_translate("TGWindow", GRADE_PREDICT%subject_predictions))

        ucas_points = sum([DICT_VALUES[g] for g in predictions.values()])
        self.predict_points_label.setText(_translate("TGWindow", GRADE_PREDICT%ucas_points))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TGWindow = QtWidgets.QMainWindow()
    ui = Ui_TGWindow()
    ui.SetUpUi(TGWindow)
    TGWindow.show()
    sys.exit(app.exec_())