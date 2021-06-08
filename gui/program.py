# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import subprocess
import time
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class SelectModeQDialog(QDialog):
    selectedMode = None # information of selected modes

    def __init__(self):
        # TODO
        # send checked list to "Start"
        # save in member variables?
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(588, 326)
        self.setMinimumSize(QtCore.QSize(588, 326))
        self.setMaximumSize(QtCore.QSize(588, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_18.addLayout(self.horizontalLayout_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_18)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_3.addWidget(self.checkBox_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBox_3 = QtWidgets.QSpinBox(self)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_5.addWidget(self.spinBox_3)
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_11.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_5 = QtWidgets.QCheckBox(self)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_7.addWidget(self.checkBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Select Git-Auto-Commit Modes"))
        self.checkBox.setText(_translate("Dialog", "Commit to a certain time interval (minutes)"))
        self.checkBox_2.setText(_translate("Dialog", "Commit when particular files changes"))
        self.pushButton.setText(_translate("Dialog", "Add files"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_5.setText(_translate("Dialog", "Delete"))
        self.pushButton_6.setText(_translate("Dialog", "Delete"))
        self.label_5.setText(_translate("Dialog", "file name"))
        self.checkBox_4.setText(_translate("Dialog", "Commit when a specific intervals of particular files changes"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "Delete"))
        self.pushButton_4.setText(_translate("Dialog", "Delete"))
        self.label_2.setText(_translate("Dialog", "file name"))
        self.label_3.setText(_translate("Dialog", "file name"))
        self.checkBox_3.setText(_translate("Dialog", "Commit in the event of an error"))
        self.checkBox_5.setText(_translate("Dialog", "Commit in the event of interrupt execution"))

class LoginQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(300, 200)
        self.setMinimumSize(QtCore.QSize(300, 200))
        self.setMaximumSize(QtCore.QSize(300, 200))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Welcome"))
        self.pushButton.setText(_translate("Dialog", "Sign in"))
        self.label.setText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Username"))

class CloneQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.repositoryName = None   # Name of cloned repository
        self.repositoryPath = None   # Path of cloned repository
        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(550, 105)
        self.setMinimumSize(QtCore.QSize(550, 105))
        self.setMaximumSize(QtCore.QSize(550, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Show selected Directory Path
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")


        self.horizontalLayout.addWidget(self.lineEdit)

        # Browse Button
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : (
            self.lineEdit.setText(self.selectDirectory())
            )
        )

        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        
        # lineEdit for input URL
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        # Clone the repo Button
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")

        # TODO
        # no input -> unable button, unable to see fullPath Label
        # at least one input - able button
        # self.lineEdit_2.textChanged.connect(self.fullPathChange)
        
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Clone a Repo"))
        self.label.setText(_translate("Dialog", "Where to clone to"))
        self.lineEdit.setText(_translate("Dialog", "Hello"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Clone the repo"))
        self.label_2.setText(_translate("Dialog", "URL"))

    def selectDirectory(self):
        dialog = QtWidgets.QFileDialog()
        repository_path = dialog.getExistingDirectory(None, "Select Repository")
        return repository_path

    def cloneRepository(self):
        pass

        # TODO
        # Check URL is correct
        # Clone the Repository
        # save local repository name & path in memeber variables

class LocalQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.repositoryName = None
        self.repositoryPath = None
        self.setupUI()

    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(551, 126)
        self.setMinimumSize(QtCore.QSize(551, 126))
        self.setMaximumSize(QtCore.QSize(551, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        
        # lineEdit for repositoryName
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # lineEdit that shows repository path
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")


        self.horizontalLayout.addWidget(self.lineEdit)

        # Browse Button
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : (
            self.lineEdit.setText(self.selectDirectory())
            )
        )
        # TODO
        # Change text of Full path label (label_4)

        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        # Button for Create Repository
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.initLocalRepository)
        
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        
        # Label for show Full Path
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        # TODO
        # when Name & Browse location -> Change FUll PATH

        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Initialize a Repo"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label.setText(_translate("Dialog", "Initialize in"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Create Repository"))
        self.label_4.setText(_translate("Dialog", "/"))
        self.label_2.setText(_translate("Dialog", "Full path"))

    def selectDirectory(self):
        dialog = QtWidgets.QFileDialog()
        repository_path = dialog.getExistingDirectory(None, "Select Repository")
        return repository_path

    def initLocalRepository(self):
        pass
        # TODO
        # no input -> unable button, unable to see fullPath Label
        # at least one input - able button
        # self.lineEdit_2.textChanged.connect(self.fullPathChange)

        # Make Folder
        # git init.

        # save repository name & path in membervariables

class PushQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.branch = None
        self.message = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(550, 102)
        self.setMinimumSize(QtCore.QSize(550, 102))
        self.setMaximumSize(QtCore.QSize(550, 102))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi()
        self.buttonBox.accepted.connect(lambda:(
            self.accept(),
            self.saveInfo(),
            )
        )
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Push"))
        self.label_3.setText(_translate("Dialog", "Branch"))
        self.label.setText(_translate("Dialog", "Commit Message"))
        self.comboBox.setItemText(0, _translate("Dialog", "master"))
        self.comboBox.setItemText(1, _translate("Dialog", "auto-commit"))

    def saveInfo(self):
        self.branch = self.comboBox.currentText()
        self.message = self.lineEdit.text()

class CheckoutQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.branch = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(550, 73)
        self.setMinimumSize(QtCore.QSize(550, 73))
        self.setMaximumSize(QtCore.QSize(550, 73))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi()
        self.buttonBox.accepted.connect(lambda:(
            self.accept(),
            self.saveInfo(),
            ))
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Where to checkout to?"))
        self.label_3.setText(_translate("Dialog", "Branch"))
        self.comboBox.setItemText(0, _translate("Dialog", "master"))
        self.comboBox.setItemText(1, _translate("Dialog", "auto-commit"))

    def saveInfo(self):
        self.branch = self.comboBox.currentText()


class Ui_MainWindow(object):

    def __init__(self):
        self.option = [0]
        self.repositoryName = None
        self.repositoryPath = None
    # TODO
    # How to show widget when clicked button

    # TODO
    # How to show login widget at the start of program?
    # How to login

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        if self.tabWidget.count() <= 0 :
            self.addNewTab(MainWindow)

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionNew_Tab.triggered.connect(self.addNewTab)
        self.actionClose_Tab = QtWidgets.QAction(MainWindow)
        self.actionClose_Tab.setObjectName("actionClose_Tab")
        self.actionClose_Tab.triggered.connect(self.tabWidget.removeTab)

        self.menuFile.addAction(self.actionNew_Tab)
        self.menuFile.addAction(self.actionClose_Tab)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git Auto Commit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Tab.setText(_translate("MainWindow", "New Tab"))
        self.actionNew_Tab.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionClose_Tab.setText(_translate("MainWindow", "Close Tab"))
        self.actionClose_Tab.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showLoginDialog(self):
        loginQDialog = LoginQDialog()
        loginQDialog.exec_()

    def openRepository(self, MainWindow):
        self.repositoryPath = self.selectDirectory()
        self.repositoryName = self.repositoryPath.split('/')[-1]

        if self.repositoryPath != "":
            self.addRepoTab(MainWindow)

            self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def cloneRepository(self, MainWindow):
        cloneQDialog = CloneQDialog()
        cloneQDialog.exec_()
        
        # TODO
        self.repositoryName = cloneQDialog.repositoryName
        self.repositoryPath = cloneQDialog.repositoryPath
        
        if self.repositoryName != None and self.repositoryPath != None:
            self.addRepoTab(MainWindow)

            self.tabWidget.removeTab(self.tabWidget.currentIndex())
        
    def initLocalRepository(self, MainWindow):
        localQDialog = LocalQDialog()
        localQDialog.exec_()

        self.repositoryName = localQDialog.repositoryName
        self.repositoryPath = localQDialog.repositoryPath
        
        if self.repositoryName != None and self.repositoryPath != None:
            self.addRepoTab(MainWindow)

            self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def showSelectMode(self):
        selectModeQDialog = SelectModeQDialog()
        selectModeQDialog.exec_()

    def selectDirectory(self):
        dialog = QtWidgets.QFileDialog()
        repository_path = dialog.getExistingDirectory(None, "Select Repository")
        return repository_path

    def addFiles(self):
        dialog = QtWidgets.QFileDialog()
        # TODO
        # Is working correctly? Really give list/tuple of selected file names? Need to check types
        files = dialog.getOpenFileNames(None, "Select files to add")

        # nothing choose and just cancel -> what is it's condition?
        if files is not list:
            return

        subprocess.call(['bash', 'base/killProcess.sh'])
        for f in files:
            subprocess.call(['sh', 'base/addFile.sh', f])

        subprocess.call(['sh', 'base/continue.sh'])
        subprocess.call(['sh', 'base/autoCommitProcess.sh'])

    def start(self):
        pass

        # TODO
        # member variable - options : list
        # autoCommit with selected Modes

    def stop(self):
        pass
        # TODO
        # kill all process

    def controlAutoCommit(self):
        if self.pushButton_5.text() == "Start":
            self.pushButton_5.setText("Stop")
            self.start()

        else:
            self.pushButton_5.setText("Start")
            self.stop()

    def push(self):
        subprocess.call(['bash', 'base/killProcess.sh'])

        # TODO
        # widget for get branch name and commit message...
        pushUI = PushQDialog()
        pushUI.exec_()


        if pushUI.branch != None and pushUI.message != None:
            branch = pushUI.branch
            msg = pushUI.message
            
            subprocess.call(['sh', 'base/userCommit.sh', branch, msg])

            subprocess.call(['sh', 'base/continue.sh']),
            
            # TODO
            # start()
            # subprocess.call(['sh', 'base/autoCommitProcess.sh'])

    def deleteBranch(self):
        checkoutQDialog = CheckoutQDialog()
        checkoutQDialog.exec_()

        branch = checkoutQDialog.branch

        if branch != None:
            subprocess.call(['bash', 'base/killProcess.sh'])
            subprocess.call(['bash', 'base/deleteBranch.sh', self.repositoryPath ,branch])

    def getGitLogGraph(self):
        command = "cd "+self.repositoryPath+ r"; git log --graph --all --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(bold white)— %an%C(reset)%C(bold yellow)%d%C(reset)' --abbrev-commit --date=relative"

        log = subprocess.run(command, capture_output=True, shell=True)

        return log.stdout.decode()

    def addNewTab(self, MainWindow):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openRepository)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cloneRepository)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.initLocalRepository)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)

        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "New Tab"))
        self.pushButton.setText(_translate("MainWindow", "Open a repo"))
        self.pushButton_2.setText(_translate("MainWindow", "Clone a repo"))
        self.pushButton_3.setText(_translate("MainWindow", "Start a local repo"))

    def addRepoTab(self, MainWindow):
        # TODO
        # repository_name : Extract Repository name & set it to tab Name
        # gitLog : text of git log --graph ...


        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 422, 284))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_4.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Start
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        # TODO
        # autoCommit.sh
        self.pushButton_5.clicked.connect(self.controlAutoCommit)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        # TODO
        # change mode
        # How to send modes to "Start"?
        # set member variables?
        # MultiChecking problem. Really can choose together?
        self.pushButton.clicked.connect(self.showSelectMode)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        # TODO
        # modify to do for multiple files
        self.pushButton_2.clicked.connect(self.addFiles)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        # TODO
        # push to specific branch
        self.pushButton_3.clicked.connect(self.push)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        # TODO
        # delete auto-commit branch
        self.pushButton_4.clicked.connect(self.deleteBranch)

        self.verticalLayout.addWidget(self.pushButton_4)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")

        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", self.repositoryName))
        self.plainTextEdit.setPlainText(_translate("MainWindow", self.getGitLogGraph()))
        self.pushButton_5.setText(_translate("MainWindow", "Start"))
        self.pushButton.setText(_translate("MainWindow", "ChangeMode"))
        self.pushButton_2.setText(_translate("MainWindow", "Add files"))
        self.pushButton_3.setText(_translate("MainWindow", "Push"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete auto-commit\nbranch"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



