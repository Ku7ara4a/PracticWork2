# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(300, 510, 160, 22))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Numbers = QLCDNumber(self.centralwidget)
        self.Numbers.setObjectName(u"Numbers")
        self.Numbers.setGeometry(QRect(350, 470, 64, 23))
        font = QFont()
        font.setBold(False)
        self.Numbers.setFont(font)
        self.Numbers.setSmallDecimalPoint(False)
        self.Numbers.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.UpperText = QLabel(self.centralwidget)
        self.UpperText.setObjectName(u"UpperText")
        self.UpperText.setGeometry(QRect(230, 10, 311, 16))
        self.UpperText.setTextFormat(Qt.TextFormat.AutoText)
        self.UpperText.setScaledContents(True)
        self.Cat_Close = QLabel(self.centralwidget)
        self.Cat_Close.setObjectName(u"Cat_Close")
        self.Cat_Close.setGeometry(QRect(250, 50, 261, 211))
        self.Cat_Close.setMouseTracking(True)
        self.Cat_Close.setPixmap(QPixmap(u"Pictures\RandomCatClose.png"))
        self.Cat_Close.setScaledContents(True)
        self.Cat_Open = QLabel(self.centralwidget)
        self.Cat_Open.setObjectName(u"Cat_Open")
        self.Cat_Open.setEnabled(True)
        self.Cat_Open.setGeometry(QRect(250, 60, 271, 201))
        self.Cat_Open.setMouseTracking(True)
        self.Cat_Open.setPixmap(QPixmap(u"Pictures\RandomCatOpen.png"))
        self.Cat_Open.setScaledContents(True)
        self.Cat_Open.setIndent(-1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 270, 231, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 440, 201, 16))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 310, 160, 116))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn2 = QPushButton(self.verticalLayoutWidget)
        self.btn2.setObjectName(u"btn2")

        self.verticalLayout.addWidget(self.btn2)

        self.btn3 = QPushButton(self.verticalLayoutWidget)
        self.btn3.setObjectName(u"btn3")

        self.verticalLayout.addWidget(self.btn3)

        self.btn4 = QPushButton(self.verticalLayoutWidget)
        self.btn4.setObjectName(u"btn4")

        self.verticalLayout.addWidget(self.btn4)

        self.btn1 = QPushButton(self.verticalLayoutWidget)
        self.btn1.setObjectName(u"btn1")

        self.verticalLayout.addWidget(self.btn1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.Numbers.display)
        self.pushButton.clicked.connect(self.Cat_Open.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UpperText.setText(QCoreApplication.translate("MainWindow", u"\u042f \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u043b\u0441\u044f \u0441 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\u0438 Qt Designer", None))
        self.Cat_Close.setText("")
        self.Cat_Open.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u044c \u0437\u0435\u0432\u0430\u0442\u044c!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0431\u0430\u043b\u043b\u043e\u0432 \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u0435?", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435\u0442", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442, \u0440\u0435\u0430\u043b\u044c\u043d\u043e \u043d\u0438\u0447\u0435\u0433\u043e", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u0440\u044f\u044e, \u0441\u043a\u0440\u044b\u0442\u044b\u0435 \u043a\u043e\u043c\u0431\u043e", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0442", None))
    # retranslateUi




