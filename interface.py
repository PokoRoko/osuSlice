# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.interval = QtWidgets.QSpinBox(self.centralwidget)
        self.interval.setMaximum(30000)
        self.interval.setSingleStep(250)
        self.interval.setProperty("value", 6000)
        self.interval.setObjectName("interval")
        self.gridLayout.addWidget(self.interval, 5, 0, 1, 1)
        self.nameDifficulty = QtWidgets.QLineEdit(self.centralwidget)
        self.nameDifficulty.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.nameDifficulty.setMaxLength(30)
        self.nameDifficulty.setObjectName("nameDifficulty")
        self.gridLayout.addWidget(self.nameDifficulty, 1, 0, 1, 1)
        self.numRepeat = QtWidgets.QSpinBox(self.centralwidget)
        self.numRepeat.setMinimum(1)
        self.numRepeat.setSingleStep(1)
        self.numRepeat.setProperty("value", 20)
        self.numRepeat.setObjectName("numRepeat")
        self.gridLayout.addWidget(self.numRepeat, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonStartSlice = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStartSlice.setObjectName("buttonStartSlice")
        self.gridLayout.addWidget(self.buttonStartSlice, 6, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "osuSlice"))
        self.label_3.setText(_translate("MainWindow", "Interval between repeats (ms)"))
        self.nameDifficulty.setText(_translate("MainWindow", "train"))
        self.label_2.setText(_translate("MainWindow", "Number of repeat"))
        self.label.setText(_translate("MainWindow", "Name difficulty to create new train game"))
        self.buttonStartSlice.setText(_translate("MainWindow", "Start Slice"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
