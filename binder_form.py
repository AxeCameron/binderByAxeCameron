# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 520)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\Vasiliy\\Desktop\\Модели\\vid\\img")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(".QMainWindow{\n"
"background-color: #3C4049;\n"
"}\n"
"\n"
".QFrame{\n"
"background-color: #21252B ;\n"
"}\n"
"\n"
".QPushButton, .QLineEdit{\n"
"background-color: #E3E3E3;\n"
"border: 1px solid #3C4049; \n"
"border-radius: 2px;\n"
"}\n"
"\n"
"#saveButton, #clearButton, #startButton{\n"
"font-size: 14px;\n"
"}")
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.key1 = QtWidgets.QPushButton(self.centralwidget)
        self.key1.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.key1.setText("")
        self.key1.setObjectName("key1")
        self.key2 = QtWidgets.QPushButton(self.centralwidget)
        self.key2.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.key2.setText("")
        self.key2.setObjectName("key2")
        self.key3 = QtWidgets.QPushButton(self.centralwidget)
        self.key3.setGeometry(QtCore.QRect(20, 120, 81, 31))
        self.key3.setText("")
        self.key3.setObjectName("key3")
        self.key4 = QtWidgets.QPushButton(self.centralwidget)
        self.key4.setGeometry(QtCore.QRect(20, 170, 81, 31))
        self.key4.setText("")
        self.key4.setObjectName("key4")
        self.key5 = QtWidgets.QPushButton(self.centralwidget)
        self.key5.setGeometry(QtCore.QRect(20, 220, 81, 31))
        self.key5.setText("")
        self.key5.setObjectName("key5")
        self.key6 = QtWidgets.QPushButton(self.centralwidget)
        self.key6.setGeometry(QtCore.QRect(20, 270, 81, 31))
        self.key6.setText("")
        self.key6.setObjectName("key6")
        self.key7 = QtWidgets.QPushButton(self.centralwidget)
        self.key7.setGeometry(QtCore.QRect(20, 320, 81, 31))
        self.key7.setText("")
        self.key7.setObjectName("key7")
        self.key8 = QtWidgets.QPushButton(self.centralwidget)
        self.key8.setGeometry(QtCore.QRect(20, 370, 81, 31))
        self.key8.setText("")
        self.key8.setObjectName("key8")
        self.bind1 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind1.setGeometry(QtCore.QRect(160, 20, 321, 31))
        self.bind1.setObjectName("bind1")
        self.bind2 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind2.setGeometry(QtCore.QRect(160, 70, 321, 31))
        self.bind2.setObjectName("bind2")
        self.bind3 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind3.setGeometry(QtCore.QRect(160, 120, 321, 31))
        self.bind3.setObjectName("bind3")
        self.bind4 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind4.setGeometry(QtCore.QRect(160, 170, 321, 31))
        self.bind4.setObjectName("bind4")
        self.bind5 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind5.setGeometry(QtCore.QRect(160, 220, 321, 31))
        self.bind5.setObjectName("bind5")
        self.bind6 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind6.setGeometry(QtCore.QRect(160, 270, 321, 31))
        self.bind6.setObjectName("bind6")
        self.bind7 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind7.setGeometry(QtCore.QRect(160, 320, 321, 31))
        self.bind7.setObjectName("bind7")
        self.bind8 = QtWidgets.QLineEdit(self.centralwidget)
        self.bind8.setGeometry(QtCore.QRect(160, 370, 321, 31))
        self.bind8.setObjectName("bind8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 0, 41, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 410, 501, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 501, 16))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-10, 10, 21, 411))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(490, 9, 20, 411))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(-10, 430, 21, 121))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(489, 430, 21, 121))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(10, 510, 481, 21))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(20, 440, 141, 61))
        self.clearButton.setObjectName("clearButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(340, 440, 141, 61))
        self.startButton.setObjectName("startButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(180, 440, 141, 61))
        self.saveButton.setObjectName("saveButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binder by Axe_Cameron"))
        self.clearButton.setText(_translate("MainWindow", "Очистить"))
        self.startButton.setText(_translate("MainWindow", "Запустить"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
