# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Secret.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_SideWindow(object):
    def setupUi(self, SideWindow):
        if not SideWindow.objectName():
            SideWindow.setObjectName(u"SideWindow")
        SideWindow.resize(800, 600)
        self.centralwidget = QWidget(SideWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 0, 691, 441))
        self.label.setPixmap(QPixmap(u"Pictures\CsarZverei.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 450, 91, 16))
        SideWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SideWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        SideWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SideWindow)
        self.statusbar.setObjectName(u"statusbar")
        SideWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SideWindow)

        QMetaObject.connectSlotsByName(SideWindow)
    # setupUi

    def retranslateUi(self, SideWindow):
        SideWindow.setWindowTitle(QCoreApplication.translate("SideWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SideWindow", u"\u0421\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043e\u0442", None))
    # retranslateUi

