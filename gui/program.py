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
        self.checkedOptions = [0]
        self.fileCreationIntervalFile = None
        self.fileCertainPercentageFiles = []
        self.fileChangesFiles = []
        self.fileIntervalChangesFiles = []
        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(590, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(590, 750))
        self.setMaximumSize(QtCore.QSize(590, 16777215))

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

       # Commit on conditions
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setObjectName("radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Commit to a certain time interval (minutes)       
        self.timeFrame = QtWidgets.QFrame(self.verticalFrame)
        self.timeFrame.setObjectName("timeFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.timeFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.checkBox = QtWidgets.QCheckBox(self.timeFrame)
        self.checkBox.setObjectName("checkBox")
        
        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.spinBox = QtWidgets.QSpinBox(self.timeFrame)
        self.spinBox.setObjectName("spinBox")
        
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addWidget(self.timeFrame)
        
        # Commit to a certain time interval based on the creation time of a file
        self.verticalFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalFrame_2)
        self.checkBox_2.setObjectName("checkBox_2")
        
        self.horizontalLayout_22.addWidget(self.checkBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        
        # Browse File Button
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalFrame_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.fileCreationAddFiles)

        self.horizontalLayout_22.addWidget(self.pushButton_13)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)

        # File Info
        self.verticalFrame_21 = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame_21.setObjectName("verticalFrame_21")
        
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame_21)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        
        # file1

        self.verticalLayout_13.addWidget(self.verticalFrame_21)
        self.verticalLayout.addWidget(self.verticalFrame_2)

        # Commit when changes occur to a file of more than a certain percentage
        self.verticalFrame_22 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame_22.setObjectName("verticalFrame_22")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_22)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalFrame_22)
        self.checkBox_3.setObjectName("checkBox_3")

        self.horizontalLayout_10.addWidget(self.checkBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        
        # Browse Files
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalFrame_22)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.fileCertainPercentageAddFiles)
        
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        # File Info
        self.verticalFrame_4 = QtWidgets.QFrame(self.verticalFrame_22)
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        # file1  
        
        # file2

        self.verticalLayout_6.addWidget(self.verticalFrame_4)
        self.verticalLayout.addWidget(self.verticalFrame_22)
        
        # Commit when particular files changes
        self.fileFrame = QtWidgets.QFrame(self.verticalFrame)
        self.fileFrame.setObjectName("fileFrame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.fileFrame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.fileFrame)
        self.checkBox_4.setObjectName("checkBox_4")
        
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        
        # Browse File
        self.pushButton = QtWidgets.QPushButton(self.fileFrame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileChangesAddFiles)
        
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_18.addLayout(self.horizontalLayout_2)
        
        # File INFO
        self.frame = QtWidgets.QFrame(self.fileFrame)
        self.frame.setObjectName("frame")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # file1
        
        # file2

        self.verticalLayout_18.addWidget(self.frame)
        self.verticalLayout.addWidget(self.fileFrame)

        # Commit when a specific intervals of particular files changes
        self.fileIntervalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.fileIntervalFrame.setObjectName("fileIntervalFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fileIntervalFrame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.checkBox_5 = QtWidgets.QCheckBox(self.fileIntervalFrame)
        self.checkBox_5.setObjectName("checkBox_5")

        self.horizontalLayout_3.addWidget(self.checkBox_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)

        # Browse Button
        self.pushButton_2 = QtWidgets.QPushButton(self.fileIntervalFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fileIntervalChangesAddFiles)

        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        # FILE INFO
        self.frame1 = QtWidgets.QFrame(self.fileIntervalFrame)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        # file1 

        # file 2

        self.verticalLayout_10.addWidget(self.frame1)
        self.verticalLayout.addWidget(self.fileIntervalFrame)

        # Error Frame
        self.errorFrame = QtWidgets.QFrame(self.verticalFrame)
        self.errorFrame.setObjectName("errorFrame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.errorFrame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.checkBox_6 = QtWidgets.QCheckBox(self.errorFrame)
        self.checkBox_6.setObjectName("checkBox_6")

        self.verticalLayout_11.addWidget(self.checkBox_6)
        self.verticalLayout.addWidget(self.errorFrame)

        # Interrupt Frame
        self.interruptFrame = QtWidgets.QFrame(self.verticalFrame)
        self.interruptFrame.setObjectName("interruptFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.interruptFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.checkBox_9 = QtWidgets.QCheckBox(self.interruptFrame)
        self.checkBox_9.setObjectName("checkBox_9")

        self.horizontalLayout_7.addWidget(self.checkBox_9)
        self.verticalLayout.addWidget(self.interruptFrame)


        self.gridLayout.addWidget(self.verticalFrame, 4, 0, 1, 1)

        # Commit whenever changes occur
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setObjectName("radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Select Git-Auto-Commit Modes"))
        self.radioButton_2.setText(_translate("Dialog", "Commit on conditions"))
        self.checkBox.setText(_translate("Dialog", "Commit to a certain time interval (minutes)"))
        self.checkBox_2.setText(_translate("Dialog", "Commit to a certain time interval based on the creation time of a file"))
        self.pushButton_13.setText(_translate("Dialog", "Add files"))
        self.checkBox_3.setText(_translate("Dialog", "Commit when changes occur to a file of more than a certain percentage"))
        self.pushButton_7.setText(_translate("Dialog", "Add files"))
        self.checkBox_4.setText(_translate("Dialog", "Commit when particular files changes"))
        self.pushButton.setText(_translate("Dialog", "Add files"))
        self.checkBox_5.setText(_translate("Dialog", "Commit when a specific intervals of particular files changes"))
        self.pushButton_2.setText(_translate("Dialog", "Add files"))
        self.checkBox_6.setText(_translate("Dialog", "Commit in the event of an error"))
        self.checkBox_9.setText(_translate("Dialog", "Commit in the event of interrupt execution"))
        self.radioButton.setText(_translate("Dialog", "Commit whenever changes occur"))

    def fileCreationAddFiles(self):
        dialog = QtWidgets.QFileDialog()
        # TODO
        # Is working correctly? Really give list/tuple of selected file names? Need to check types
        file = dialog.getOpenFileName(None, "Select file to add")

        # nothing choose and just cancel -> what is it's condition?
        if file[0] != '':
            self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_25.setObjectName("horizontalLayout_25")

            self.label_12 = QtWidgets.QLabel(self.verticalFrame_21)
            self.label_12.setObjectName("label_12")

            self.horizontalLayout_25.addWidget(self.label_12)
            spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_25.addItem(spacerItem2)
            
            self.spinBox_11 = QtWidgets.QSpinBox(self.verticalFrame_21)
            self.spinBox_11.setObjectName("spinBox_11")
            
            self.horizontalLayout_25.addWidget(self.spinBox_11)
        
            # Delete Button
            self.pushButton_15 = QtWidgets.QPushButton(self.verticalFrame_21)
            self.pushButton_15.setObjectName("pushButton_15")
            self.pushButton_15.clicked.connect(lambda:(
                    self.verticalLayout_9.removeItem(self.horizontalLayout_25),
                )
            )
            
            self.horizontalLayout_25.addWidget(self.pushButton_15)
            self.verticalLayout_9.addLayout(self.horizontalLayout_25)

            _translate = QtCore.QCoreApplication.translate  
            self.label_12.setText(_translate("Dialog", file[0].split("/")[-1]))
            self.pushButton_15.setText(_translate("Dialog", "Delete"))

    def fileCertainPercentageAddFiles(self):
        dialog = QtWidgets.QFileDialog()
        # TODO
        # Is working correctly? Really give list/tuple of selected file names? Need to check types
        files = dialog.getOpenFileNames(None, "Select files to add")

        if files[0] != []:
            for f in files[0]:
                self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_14.setObjectName("horizontalLayout_14")
                
                self.label_7 = QtWidgets.QLabel(self.verticalFrame_4)
                self.label_7.setObjectName("label_7")

                self.horizontalLayout_14.addWidget(self.label_7)
                spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_14.addItem(spacerItem4)

                self.spinBox_6 = QtWidgets.QSpinBox(self.verticalFrame_4)
                self.spinBox_6.setObjectName("spinBox_6")

                self.horizontalLayout_14.addWidget(self.spinBox_6)

                # Delete Button
                self.pushButton_8 = QtWidgets.QPushButton(self.verticalFrame_4)
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_8.clicked.connect(lambda:(
                        self.verticalLayout_4.removeItem(self.horizontalLayout_14),
                    )
                )

                self.horizontalLayout_14.addWidget(self.pushButton_8)
                self.verticalLayout_4.addLayout(self.horizontalLayout_14)

                _translate = QtCore.QCoreApplication.translate  
                self.label_7.setText(_translate("Dialog", f.split("/")[-1]))
                self.pushButton_8.setText(_translate("Dialog", "Delete"))
            
    def fileChangesAddFiles(self):
        dialog = QtWidgets.QFileDialog()
        # TODO
        # Is working correctly? Really give list/tuple of selected file names? Need to check types
        files = dialog.getOpenFileNames(None, "Select files to add")

        if files[0] != []:
            for f in files[0]:
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setObjectName("label_4")
                
                self.horizontalLayout_6.addWidget(self.label_4)
                spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem7)
                
                # Delete Button
                self.pushButton_5 = QtWidgets.QPushButton(self.frame)
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_5.clicked.connect(lambda:(
                        self.verticalLayout_2.removeItem(self.horizontalLayout_6),
                    )
                )
                
                self.horizontalLayout_6.addWidget(self.pushButton_5)
                self.verticalLayout_2.addLayout(self.horizontalLayout_6)

                _translate = QtCore.QCoreApplication.translate
                self.label_4.setText(_translate("Dialog", f.split("/")[-1]))
                self.pushButton_5.setText(_translate("Dialog", "Delete"))

    def fileIntervalChangesAddFiles(self):
        dialog = QtWidgets.QFileDialog()
        # TODO
        # Is working correctly? Really give list/tuple of selected file names? Need to check types
        files = dialog.getOpenFileNames(None, "Select files to add")

        if files[0] != []:
            for f in files[0]:
                self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_11.setObjectName("horizontalLayout_11")

                self.label_2 = QtWidgets.QLabel(self.frame1)
                self.label_2.setObjectName("label_2")

                self.horizontalLayout_11.addWidget(self.label_2)
                spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_11.addItem(spacerItem10)
                
                # start line of interval
                self.spinBox_4 = QtWidgets.QSpinBox(self.frame1)
                self.spinBox_4.setObjectName("spinBox_4")
                
                self.horizontalLayout_11.addWidget(self.spinBox_4)
                self.label = QtWidgets.QLabel(self.frame1)
                self.label.setObjectName("label")
                self.horizontalLayout_11.addWidget(self.label)
                
                # last line of interval
                self.spinBox_2 = QtWidgets.QSpinBox(self.frame1)
                self.spinBox_2.setObjectName("spinBox_2")
                
                self.horizontalLayout_11.addWidget(self.spinBox_2)
                
                # Delete Button
                self.pushButton_3 = QtWidgets.QPushButton(self.frame1)
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(lambda:(
                        self.verticalLayout_5.removeItem(self.horizontalLayout_11),
                    )
                )

                self.horizontalLayout_11.addWidget(self.pushButton_3)
                self.verticalLayout_5.addLayout(self.horizontalLayout_11)

                _translate = QtCore.QCoreApplication.translate
                self.label_2.setText(_translate("Dialog", f.split("/")[-1]))
                self.label.setText(_translate("Dialog", "~"))
                self.pushButton_3.setText(_translate("Dialog", "Delete"))

    def saveInfo(self):
        self.checkedOptions = []
        
        self.fileCreationIntervalFile = None
        self.fileCertainPercentageFiles = []
        self.fileChangesFiles = []
        self.fileIntervalChangesFiles = []

        if self.radioButton.isChecked():
            self.checkedOptions.append(0)

        else:
            if self.checkBox.isChecked():
                self.checkedOptions.append(1)

            if self.checkBox_2.isChecked():
                self.checkedOptions.append(2)

            if self.checkBox_3.isChecked():
                self.checkedOptions.append(3)

            if self.checkBox_4.isChecked():
                self.checkedOptions.append(4)

            if self.checkBox_5.isChecked():
                self.checkedOptions.append(5)

            if self.checkBox_6.isChecked():
                self.checkedOptions.append(6)

            if self.checkBox_9.isChecked():
                self.checkedOptions.append(7)        

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
        self.checkedOptions = [0]
        self.fileCreationIntervalFile = None
        self.fileCertainPercentageFiles = []
        self.fileChangesFiles = []
        self.fileIntervalChangesFiles = []
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

        if selectModeQDialog.checkedOptions != []:
            self.checkedOptions = selectModeQDialog.checkedOptions
            self.fileCreationIntervalFile = selectModeQDialog.fileCreationIntervalFile
            self.fileCertainPercentageFiles = selectModeQDialog.fileCertainPercentageFiles
            self.fileChangesFiles = selectModeQDialog.fileChangesFiles
            self.fileIntervalChangesFiles = selectModeQDialog.fileIntervalChangesFiles

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
        if files[0] != []:
            subprocess.call(['bash', 'base/killProcess.sh'])
            for f in files[0]:
                subprocess.call(['sh', 'base/addFile.sh', f, self.repositoryPath])

            subprocess.call(['sh', 'base/continue.sh'])
            
            # TODO
            self.start()
            #subprocess.call(['sh', 'base/autoCommitProcess.sh'])

    def start(self):

            if self.checkedOptions[0] == 0:
                subprocess.call(['sh', 'base/continue.sh'])
                subprocess.call(['sh', 'base/autoCommitProcess.sh', self.repositoryPath])

            else:
                if 1 in self.checkedOptions:
                    pass

                if 2 in self.checkedOptions:
                    pass

                if 3 in self.checkedOptions:
                    pass

                if 4 in self.checkedOptions:
                    pass

                if 5 in self.checkedOptions:
                    pass

                if 6 in self.checkedOptions:
                    pass

                if 7 in self.checkedOptions:
                    pass

        # TODO
        # member variable - options : list
        # autoCommit with selected Modes

    def stop(self):
        if self.checkedOptions[0] == 0:
            subprocess.call(['bash', 'base/killProcess.sh'])

        else:
            if 1 in self.checkedOptions:
                pass

            if 2 in self.checkedOptions:
                pass

            if 3 in self.checkedOptions:
                pass

            if 4 in self.checkedOptions:
                pass

            if 5 in self.checkedOptions:
                pass

            if 6 in self.checkedOptions:
                pass

            if 7 in self.checkedOptions:
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
            
            subprocess.call(['sh', 'base/userCommit.sh', branch, msg, self.repositoryPath])
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

    # TODO
    # Seperate Tab from MainWindow

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



