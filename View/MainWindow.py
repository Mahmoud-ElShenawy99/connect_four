# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(838, 933)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        GUI.setMinimumSize(QtCore.QSize(800, 933))
        GUI.setMaximumSize(QtCore.QSize(838, 933))
        GUI.setStyleSheet("background-color: rgb(0, 0, 106);\n"
"background-color: rgb(255, 136, 38);\n"
"background-color: rgb(0, 0, 59);\n"
"background-color: (255, 175, 83);\n"
"background-color: rgb(38, 38, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 87 63pt \"Source Code Pro Black\";\n"
"background-color: rgb(223, 246, 255);\n"
"color: rgb(37, 109, 133);\n"
"\n"
"border-radius: 15px;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.l04 = QtWidgets.QLabel(self.centralwidget)
        self.l04.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l04.setText("")
        self.l04.setObjectName("l04")
        self.gridLayout.addWidget(self.l04, 2, 6, 1, 1)
        self.l44 = QtWidgets.QLabel(self.centralwidget)
        self.l44.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l44.setText("")
        self.l44.setObjectName("l44")
        self.gridLayout.addWidget(self.l44, 2, 2, 1, 1)
        self.l24 = QtWidgets.QLabel(self.centralwidget)
        self.l24.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l24.setText("")
        self.l24.setObjectName("l24")
        self.gridLayout.addWidget(self.l24, 2, 4, 1, 1)
        self.l02 = QtWidgets.QLabel(self.centralwidget)
        self.l02.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l02.setText("")
        self.l02.setObjectName("l02")
        self.gridLayout.addWidget(self.l02, 4, 6, 1, 1)
        self.l03 = QtWidgets.QLabel(self.centralwidget)
        self.l03.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l03.setText("")
        self.l03.setObjectName("l03")
        self.gridLayout.addWidget(self.l03, 3, 6, 1, 1)
        self.l14 = QtWidgets.QLabel(self.centralwidget)
        self.l14.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l14.setText("")
        self.l14.setObjectName("l14")
        self.gridLayout.addWidget(self.l14, 2, 5, 1, 1)
        self.l51 = QtWidgets.QLabel(self.centralwidget)
        self.l51.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l51.setText("")
        self.l51.setObjectName("l51")
        self.gridLayout.addWidget(self.l51, 5, 1, 1, 1)
        self.l50 = QtWidgets.QLabel(self.centralwidget)
        self.l50.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l50.setText("")
        self.l50.setObjectName("l50")
        self.gridLayout.addWidget(self.l50, 6, 1, 1, 1)
        self.l13 = QtWidgets.QLabel(self.centralwidget)
        self.l13.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l13.setText("")
        self.l13.setObjectName("l13")
        self.gridLayout.addWidget(self.l13, 3, 5, 1, 1)
        self.l53 = QtWidgets.QLabel(self.centralwidget)
        self.l53.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l53.setText("")
        self.l53.setObjectName("l53")
        self.gridLayout.addWidget(self.l53, 3, 1, 1, 1)
        self.l52 = QtWidgets.QLabel(self.centralwidget)
        self.l52.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l52.setText("")
        self.l52.setObjectName("l52")
        self.gridLayout.addWidget(self.l52, 4, 1, 1, 1)
        self.l21 = QtWidgets.QLabel(self.centralwidget)
        self.l21.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l21.setText("")
        self.l21.setObjectName("l21")
        self.gridLayout.addWidget(self.l21, 5, 4, 1, 1)
        self.l42 = QtWidgets.QLabel(self.centralwidget)
        self.l42.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l42.setText("")
        self.l42.setObjectName("l42")
        self.gridLayout.addWidget(self.l42, 4, 2, 1, 1)
        self.l41 = QtWidgets.QLabel(self.centralwidget)
        self.l41.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l41.setText("")
        self.l41.setObjectName("l41")
        self.gridLayout.addWidget(self.l41, 5, 2, 1, 1)
        self.l40 = QtWidgets.QLabel(self.centralwidget)
        self.l40.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l40.setText("")
        self.l40.setObjectName("l40")
        self.gridLayout.addWidget(self.l40, 6, 2, 1, 1)
        self.l10 = QtWidgets.QLabel(self.centralwidget)
        self.l10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l10.setText("")
        self.l10.setObjectName("l10")
        self.gridLayout.addWidget(self.l10, 6, 5, 1, 1)
        self.l54 = QtWidgets.QLabel(self.centralwidget)
        self.l54.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l54.setText("")
        self.l54.setObjectName("l54")
        self.gridLayout.addWidget(self.l54, 2, 1, 1, 1)
        self.l55 = QtWidgets.QLabel(self.centralwidget)
        self.l55.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l55.setText("")
        self.l55.setObjectName("l55")
        self.gridLayout.addWidget(self.l55, 1, 1, 1, 1)
        self.l63 = QtWidgets.QLabel(self.centralwidget)
        self.l63.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l63.setText("")
        self.l63.setObjectName("l63")
        self.gridLayout.addWidget(self.l63, 3, 0, 1, 1)
        self.l33 = QtWidgets.QLabel(self.centralwidget)
        self.l33.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l33.setText("")
        self.l33.setObjectName("l33")
        self.gridLayout.addWidget(self.l33, 3, 3, 1, 1)
        self.l23 = QtWidgets.QLabel(self.centralwidget)
        self.l23.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l23.setText("")
        self.l23.setObjectName("l23")
        self.gridLayout.addWidget(self.l23, 3, 4, 1, 1)
        self.l12 = QtWidgets.QLabel(self.centralwidget)
        self.l12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l12.setText("")
        self.l12.setObjectName("l12")
        self.gridLayout.addWidget(self.l12, 4, 5, 1, 1)
        self.l01 = QtWidgets.QLabel(self.centralwidget)
        self.l01.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l01.setText("")
        self.l01.setObjectName("l01")
        self.gridLayout.addWidget(self.l01, 5, 6, 1, 1)
        self.l22 = QtWidgets.QLabel(self.centralwidget)
        self.l22.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l22.setText("")
        self.l22.setObjectName("l22")
        self.gridLayout.addWidget(self.l22, 4, 4, 1, 1)
        self.l32 = QtWidgets.QLabel(self.centralwidget)
        self.l32.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l32.setText("")
        self.l32.setObjectName("l32")
        self.gridLayout.addWidget(self.l32, 4, 3, 1, 1)
        self.l30 = QtWidgets.QLabel(self.centralwidget)
        self.l30.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l30.setText("")
        self.l30.setObjectName("l30")
        self.gridLayout.addWidget(self.l30, 6, 3, 1, 1)
        self.l45 = QtWidgets.QLabel(self.centralwidget)
        self.l45.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l45.setText("")
        self.l45.setObjectName("l45")
        self.gridLayout.addWidget(self.l45, 1, 2, 1, 1)
        self.l35 = QtWidgets.QLabel(self.centralwidget)
        self.l35.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l35.setText("")
        self.l35.setObjectName("l35")
        self.gridLayout.addWidget(self.l35, 1, 3, 1, 1)
        self.l31 = QtWidgets.QLabel(self.centralwidget)
        self.l31.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l31.setText("")
        self.l31.setObjectName("l31")
        self.gridLayout.addWidget(self.l31, 5, 3, 1, 1)
        self.l20 = QtWidgets.QLabel(self.centralwidget)
        self.l20.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l20.setText("")
        self.l20.setObjectName("l20")
        self.gridLayout.addWidget(self.l20, 6, 4, 1, 1)
        self.l34 = QtWidgets.QLabel(self.centralwidget)
        self.l34.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l34.setText("")
        self.l34.setObjectName("l34")
        self.gridLayout.addWidget(self.l34, 2, 3, 1, 1)
        self.l00 = QtWidgets.QLabel(self.centralwidget)
        self.l00.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l00.setText("")
        self.l00.setObjectName("l00")
        self.gridLayout.addWidget(self.l00, 6, 6, 1, 1)
        self.l43 = QtWidgets.QLabel(self.centralwidget)
        self.l43.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l43.setText("")
        self.l43.setObjectName("l43")
        self.gridLayout.addWidget(self.l43, 3, 2, 1, 1)
        self.l11 = QtWidgets.QLabel(self.centralwidget)
        self.l11.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l11.setText("")
        self.l11.setObjectName("l11")
        self.gridLayout.addWidget(self.l11, 5, 5, 1, 1)
        self.l25 = QtWidgets.QLabel(self.centralwidget)
        self.l25.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l25.setText("")
        self.l25.setObjectName("l25")
        self.gridLayout.addWidget(self.l25, 1, 4, 1, 1)
        self.l15 = QtWidgets.QLabel(self.centralwidget)
        self.l15.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l15.setText("")
        self.l15.setObjectName("l15")
        self.gridLayout.addWidget(self.l15, 1, 5, 1, 1)
        self.l05 = QtWidgets.QLabel(self.centralwidget)
        self.l05.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l05.setText("")
        self.l05.setObjectName("l05")
        self.gridLayout.addWidget(self.l05, 1, 6, 1, 1)
        self.l60 = QtWidgets.QLabel(self.centralwidget)
        self.l60.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l60.setText("")
        self.l60.setObjectName("l60")
        self.gridLayout.addWidget(self.l60, 6, 0, 1, 1)
        self.l61 = QtWidgets.QLabel(self.centralwidget)
        self.l61.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l61.setText("")
        self.l61.setObjectName("l61")
        self.gridLayout.addWidget(self.l61, 5, 0, 1, 1)
        self.l62 = QtWidgets.QLabel(self.centralwidget)
        self.l62.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l62.setText("")
        self.l62.setObjectName("l62")
        self.gridLayout.addWidget(self.l62, 4, 0, 1, 1)
        self.l64 = QtWidgets.QLabel(self.centralwidget)
        self.l64.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l64.setText("")
        self.l64.setObjectName("l64")
        self.gridLayout.addWidget(self.l64, 2, 0, 1, 1)
        self.l65 = QtWidgets.QLabel(self.centralwidget)
        self.l65.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(37, 109, 133);\n"
"border-radius:51px;\n"
"")
        self.l65.setText("")
        self.l65.setObjectName("l65")
        self.gridLayout.addWidget(self.l65, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.B1.setObjectName("B1")
        self.horizontalLayout.addWidget(self.B1)
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.B2.setObjectName("B2")
        self.horizontalLayout.addWidget(self.B2)
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.B3.setObjectName("B3")
        self.horizontalLayout.addWidget(self.B3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 26))
        self.menubar.setObjectName("menubar")
        GUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI)
        self.statusbar.setObjectName("statusbar")
        GUI.setStatusBar(self.statusbar)

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Connect Four"))
        self.label.setText(_translate("GUI", "Connect 4"))
        self.B1.setText(_translate("GUI", "PushButton"))
        self.B2.setText(_translate("GUI", "PushButton"))
        self.B3.setText(_translate("GUI", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
