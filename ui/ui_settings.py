# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 352)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 195, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 15, 591, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 21, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.le_password = QtWidgets.QLineEdit(self.groupBox)
        self.le_password.setGeometry(QtCore.QRect(130, 70, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.le_password.setFont(font)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.le_email = QtWidgets.QLineEdit(self.groupBox)
        self.le_email.setGeometry(QtCore.QRect(130, 21, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 145, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.te_msg = QtWidgets.QTextEdit(Dialog)
        self.te_msg.setGeometry(QtCore.QRect(40, 225, 531, 81))
        self.te_msg.setObjectName("te_msg")
        self.le_channel = QtWidgets.QLineEdit(Dialog)
        self.le_channel.setGeometry(QtCore.QRect(140, 145, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.le_channel.setFont(font)
        self.le_channel.setObjectName("le_channel")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(190, 315, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(330, 315, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bot Settings"))
        self.label_7.setText(_translate("Dialog", "Message:"))
        self.groupBox.setTitle(_translate("Dialog", "Discord Account"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_4.setText(_translate("Dialog", "Email:"))
        self.label_6.setText(_translate("Dialog", "Channel ID:"))
        self.btn_save.setText(_translate("Dialog", "Save"))
        self.btn_close.setText(_translate("Dialog", "Close"))