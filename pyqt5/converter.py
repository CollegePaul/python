# pyuic5 -x converter.ui -o converter.py




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setObjectName("title")

        #Input box
        self.inch_in = QtWidgets.QLineEdit(self.centralwidget)
        self.inch_in.setAlignment(QtCore.Qt.AlignCenter)
        self.inch_in.setGeometry(QtCore.QRect(120, 150, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inch_in.setFont(font)
        self.inch_in.setObjectName("inch_in")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #Button
        self.convert1 = QtWidgets.QPushButton(self.centralwidget, clicked = self.press)
        self.convert1.setGeometry(QtCore.QRect(250, 150, 171, 51))
        
        font.setPointSize(16)
        self.convert1.setFont(font)
        self.convert1.setObjectName("convert1")

        #output box
        self.cm_out = QtWidgets.QLabel(self.centralwidget)
        self.cm_out.setGeometry(QtCore.QRect(460, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cm_out.setFont(font)
        self.cm_out.setObjectName("cm_out")

        #error message
        self.error_message = QtWidgets.QLabel(self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(110, 210, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.error_message.setFont(font)
        self.error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.error_message.setObjectName("")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pauls Awsome converter"))
        self.title.setText(_translate("MainWindow", "My Converter"))
        self.label_2.setText(_translate("MainWindow", "Inches"))
        self.convert1.setText(_translate("MainWindow", "Convert to cm"))
        self.cm_out.setText(_translate("MainWindow", "TextLabel"))
        

    def press(self):
        x = self.inch_in.text()
        #presence check
        if len(x)<1:
            self.error_message.setText("<span style='color:red'>Please enter a number<span>")
            return

        try:
            #validate as a number
            y = float(x) * 2.54
            self.cm_out.setText(f'{y:.2f} cm')
            self.error_message.setText("")
        except:
            self.error_message.setText("<span style='color:red'>Please enter a valid number<span>")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
