# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelefoneditorQT.ui'
#
# Created: Wed Apr 02 20:19:57 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb, config
IP ="192.168.2.200"
#IP = "172.24.105.118"


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1080, 518)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 518))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 518))
        #MainWindow.setStyle(QtGui.QStyleFactory.create("win"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("E:/Radistart_Dev/test.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 891, 331))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 370, 1059, 58))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.EditLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.EditLayout.setMargin(0)
        self.EditLayout.setObjectName(_fromUtf8("EditLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.EditLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.EName = QtGui.QLineEdit(self.layoutWidget)
        self.EName.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EName.sizePolicy().hasHeightForWidth())
        self.EName.setSizePolicy(sizePolicy)
        self.EName.setAlignment(QtCore.Qt.AlignCenter)
        self.EName.setReadOnly(False)
        self.EName.setObjectName(_fromUtf8("EName"))
        self.horizontalLayout.addWidget(self.EName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.EInfo = QtGui.QLineEdit(self.layoutWidget)
        self.EInfo.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EInfo.sizePolicy().hasHeightForWidth())
        self.EInfo.setSizePolicy(sizePolicy)
        self.EInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.EInfo.setReadOnly(False)
        self.EInfo.setObjectName(_fromUtf8("EInfo"))
        self.horizontalLayout.addWidget(self.EInfo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ENummer = QtGui.QLineEdit(self.layoutWidget)
        self.ENummer.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ENummer.sizePolicy().hasHeightForWidth())
        self.ENummer.setSizePolicy(sizePolicy)
        self.ENummer.setAlignment(QtCore.Qt.AlignCenter)
        self.ENummer.setReadOnly(False)
        self.ENummer.setObjectName(_fromUtf8("ENummer"))
        self.horizontalLayout.addWidget(self.ENummer)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.EFax = QtGui.QLineEdit(self.layoutWidget)
        self.EFax.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EFax.sizePolicy().hasHeightForWidth())
        self.EFax.setSizePolicy(sizePolicy)
        self.EFax.setAlignment(QtCore.Qt.AlignCenter)
        self.EFax.setReadOnly(False)
        self.EFax.setObjectName(_fromUtf8("EFax"))
        self.horizontalLayout.addWidget(self.EFax)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.EVisable = QtGui.QLineEdit(self.layoutWidget)
        self.EVisable.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EVisable.sizePolicy().hasHeightForWidth())
        self.EVisable.setSizePolicy(sizePolicy)
        self.EVisable.setAlignment(QtCore.Qt.AlignCenter)
        self.EVisable.setReadOnly(False)
        self.EVisable.setObjectName(_fromUtf8("EVisable"))
        self.horizontalLayout.addWidget(self.EVisable)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.LID = QtGui.QLabel(self.layoutWidget)
        self.LID.setAlignment(QtCore.Qt.AlignCenter)
        self.LID.setObjectName(_fromUtf8("LID"))
        self.horizontalLayout.addWidget(self.LID)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.EName_3 = QtGui.QLineEdit(self.layoutWidget)
        self.EName_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EName_3.sizePolicy().hasHeightForWidth())
        self.EName_3.setSizePolicy(sizePolicy)
        self.EName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.EName_3.setReadOnly(False)
        self.EName_3.setObjectName(_fromUtf8("EName_3"))
        self.horizontalLayout_2.addWidget(self.EName_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.EInfo_3 = QtGui.QLineEdit(self.layoutWidget)
        self.EInfo_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EInfo_3.sizePolicy().hasHeightForWidth())
        self.EInfo_3.setSizePolicy(sizePolicy)
        self.EInfo_3.setAlignment(QtCore.Qt.AlignCenter)
        self.EInfo_3.setReadOnly(False)
        self.EInfo_3.setObjectName(_fromUtf8("EInfo_3"))
        self.horizontalLayout_2.addWidget(self.EInfo_3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.ENummer_3 = QtGui.QLineEdit(self.layoutWidget)
        self.ENummer_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ENummer_3.sizePolicy().hasHeightForWidth())
        self.ENummer_3.setSizePolicy(sizePolicy)
        self.ENummer_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ENummer_3.setReadOnly(False)
        self.ENummer_3.setObjectName(_fromUtf8("ENummer_3"))
        self.horizontalLayout_2.addWidget(self.ENummer_3)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.EFax_3 = QtGui.QLineEdit(self.layoutWidget)
        self.EFax_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EFax_3.sizePolicy().hasHeightForWidth())
        self.EFax_3.setSizePolicy(sizePolicy)
        self.EFax_3.setAlignment(QtCore.Qt.AlignCenter)
        self.EFax_3.setReadOnly(False)
        self.EFax_3.setObjectName(_fromUtf8("EFax_3"))
        self.horizontalLayout_2.addWidget(self.EFax_3)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.EVisable_3 = QtGui.QLineEdit(self.layoutWidget)
        self.EVisable_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EVisable_3.sizePolicy().hasHeightForWidth())
        self.EVisable_3.setSizePolicy(sizePolicy)
        self.EVisable_3.setAlignment(QtCore.Qt.AlignCenter)
        self.EVisable_3.setReadOnly(False)
        self.EVisable_3.setObjectName(_fromUtf8("EVisable_3"))
        self.horizontalLayout_2.addWidget(self.EVisable_3)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.LID_3 = QtGui.QLabel(self.layoutWidget)
        self.LID_3.setAlignment(QtCore.Qt.AlignCenter)
        self.LID_3.setObjectName(_fromUtf8("LID_3"))
        self.horizontalLayout_2.addWidget(self.LID_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.EditLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(770, 440, 301, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget1.sizePolicy().hasHeightForWidth())
        self.layoutWidget1.setSizePolicy(sizePolicy)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.ButtonLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.ButtonLayout.setMargin(0)
        self.ButtonLayout.setObjectName(_fromUtf8("ButtonLayout"))
        self.BAnwenden = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BAnwenden.sizePolicy().hasHeightForWidth())
        self.BAnwenden.setSizePolicy(sizePolicy)
        self.BAnwenden.setObjectName(_fromUtf8("BAnwenden"))
        self.ButtonLayout.addWidget(self.BAnwenden)
        self.BAbbrechen = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BAbbrechen.sizePolicy().hasHeightForWidth())
        self.BAbbrechen.setSizePolicy(sizePolicy)
        self.BAbbrechen.setObjectName(_fromUtf8("BAbbrechen"))
        self.ButtonLayout.addWidget(self.BAbbrechen)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 11, 161, 221))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.RNeu = QtGui.QRadioButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RNeu.sizePolicy().hasHeightForWidth())
        self.RNeu.setSizePolicy(sizePolicy)
        self.RNeu.setChecked(True)
        self.RNeu.setObjectName(_fromUtf8("RNeu"))
        self.verticalLayout.addWidget(self.RNeu)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.SucheLayout = QtGui.QVBoxLayout()
        self.SucheLayout.setObjectName(_fromUtf8("SucheLayout"))
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.SucheLayout.addWidget(self.label)
        self.ESuche = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ESuche.sizePolicy().hasHeightForWidth())
        self.ESuche.setSizePolicy(sizePolicy)
        self.ESuche.setObjectName(_fromUtf8("ESuche"))
        self.SucheLayout.addWidget(self.ESuche)
        self.BSuche = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BSuche.sizePolicy().hasHeightForWidth())
        self.BSuche.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("E:/Radistart_Dev/Telefonedit/Telefoneditor QT/lupe.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BSuche.setIcon(icon1)
        self.BSuche.setObjectName(_fromUtf8("BSuche"))
        self.SucheLayout.addWidget(self.BSuche)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.SucheLayout.addItem(spacerItem12)
        self.RAendernloeschen = QtGui.QRadioButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAendernloeschen.sizePolicy().hasHeightForWidth())
        self.RAendernloeschen.setSizePolicy(sizePolicy)
        self.RAendernloeschen.setObjectName(_fromUtf8("RAendernloeschen"))
        self.SucheLayout.addWidget(self.RAendernloeschen)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.SucheLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.SucheLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        self.menu_ber = QtGui.QMenu(self.menubar)
        self.menu_ber.setObjectName(_fromUtf8("menu_ber"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setMinimumSize(QtCore.QSize(100, 10))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDatenbank_exportieren = QtGui.QAction(MainWindow)
        self.actionDatenbank_exportieren.setObjectName(_fromUtf8("actionDatenbank_exportieren"))
        self.actionEditor_beenden = QtGui.QAction(MainWindow)
        self.actionEditor_beenden.setObjectName(_fromUtf8("actionEditor_beenden"))
        self.actionHilfe = QtGui.QAction(MainWindow)
        self.actionHilfe.setObjectName(_fromUtf8("actionHilfe"))
        self.actionKontakt = QtGui.QAction(MainWindow)
        self.actionKontakt.setObjectName(_fromUtf8("actionKontakt"))
        self.actionLizenz = QtGui.QAction(MainWindow)
        self.actionLizenz.setObjectName(_fromUtf8("actionLizenz"))
        self.menuDatei.addAction(self.actionDatenbank_exportieren)
        self.menuDatei.addAction(self.actionEditor_beenden)
        self.menu_ber.addAction(self.actionHilfe)
        self.menu_ber.addAction(self.actionKontakt)
        self.menu_ber.addAction(self.actionLizenz)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menu_ber.menuAction())

#Funktionen

        def suche():
            print "Suche läuft"
            search=self.ESuche.text()
            if str(search)=="":
                search="Radiologie"
            
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Info', 'Nummer', 'Fax', 'Autor', 'Datum', 'ID', 'Sichtbar'])
            conn = MySQLdb.connect(host=IP,
                                   user="radistart",
                                   passwd="radistart",
                                   db="Telefonbuch")
            cursor = conn.cursor()
            gesucht="'%"+str(search)+"%'"
            sql = ("SELECT * FROM Telefonbuch WHERE Name LIKE "+gesucht)
            cursor.execute(sql)
            rows = cursor.fetchall()
            #print rows
            for i in cursor:
                A=0
                #print i[0], i[1], i[2], i[3]
                
                for j in rows:
                    self.tableWidget.setItem(A,0, QtGui.QTableWidgetItem(j[0]))
                    self.tableWidget.setItem(A,1, QtGui.QTableWidgetItem(j[1]))
                    self.tableWidget.setItem(A,2, QtGui.QTableWidgetItem(j[2]))
                    self.tableWidget.setItem(A,3, QtGui.QTableWidgetItem(j[3]))
                    self.tableWidget.setItem(A,4, QtGui.QTableWidgetItem(j[4]))
                    self.tableWidget.setItem(A,5, QtGui.QTableWidgetItem(j[5]))
                    self.tableWidget.setItem(A,6, QtGui.QTableWidgetItem(str(j[6])))
                    self.tableWidget.setItem(A,7, QtGui.QTableWidgetItem(str(j[7])))

                    self.tableWidget.resizeColumnsToContents()

                    A=A+1

                
            cursor.close()
            conn.close()
        A=0
                
        def ausgesucht(row, column):

            self.tableWidget.clear()            #Hintergrund der tabelle resetten um dann einzufärben
            suche()

            self.RNeu.setChecked(False)
            self.RAendernloeschen.setChecked(True)

            self.EName_3.setEnabled(True)
            self.EInfo_3.setEnabled(True)
            self.ENummer_3.setEnabled(True)
            self.EFax_3.setEnabled(True)
            self.EVisable_3.setEnabled(True)
            for i in range (0,6):
                item = self.tableWidget.item(row,i)
                item.setBackground(QtGui.QColor(90,200,251))
            item=self.tableWidget.item(row, 6)
            item.setBackground(QtGui.QColor(100,240,251))
            item2=self.tableWidget.item(row, 7)
            item2.setBackground(QtGui.QColor(90,200,251))

            ID = item.text()
            ID=int(ID)
            global ID
            self.LID_3.setText(str(ID))
        
            conn = MySQLdb.connect(host=IP,
                                   user="radistart",
                                   passwd="radistart",
                                   db="Telefonbuch")
            cursor = conn.cursor()
            #gesucht="'%"+str(ID)+"%'"      #suche enthält...
            gesucht=str(ID)                 #nur die genaue ID
            sql = ("SELECT * FROM Telefonbuch WHERE ID LIKE "+gesucht)
            cursor.execute(sql)
            rows = cursor.fetchall()
            #print rows
            for i in cursor:
                A=0
                #print i[0], i[1], i[2], i[3]
                
                for j in rows:
                    self.EName_3.setText(str(j[0]))
                    self.EInfo_3.setText(str(j[1]))
                    self.ENummer_3.setText(str(j[2]))
                    self.EFax_3.setText(str(j[3]))
                    self.EVisable_3.setText(str(j[7]))

                    

        self.tableWidget.cellClicked.connect(ausgesucht)

        def wechsel():
            self.EName_3.setEnabled(True)
            self.RAendernloeschen.setChecked(False)
            self.EName.setEnabled(False)
            self.EInfo.setEnabled(False)
            self.ENummer.setEnabled(False)
            self.EFax.setEnabled(False)
            self.EVisable.setEnabled(False)

            self.EName_3.setEnabled(True)
            self.EInfo_3.setEnabled(True)
            self.ENummer_3.setEnabled(True)
            self.EFax_3.setEnabled(True)
            self.EVisable_3.setEnabled(True)
    
        self.RNeu.clicked.connect(wechsel)


        def run():
            if str(self.EVisable_3.text())==str("sichtbar"):
                Sichtbar=str("1")
            elif str(self.EVisable_3.text())==str("1"):
                Sichtbar=str("1")
                
            else:
                Sichtbar=str("0")

            Name =str(self.EName_3.text())                     #Keine Umlaute!!!
            Nummer =str(self.ENummer_3.text())                  #Keine Umlaute!!!
            Info =str(self.EInfo_3.text())
            Fax =str(self.EFax_3.text())
            Author=config.User
            Datum=config.Date2
           
               
            if self.RNeu.isChecked():
                print "Übertragung gestartet"
                conn = MySQLdb.connect(host=IP,
                                       user="radistart",
                                       passwd="radistart",
                                       db="Telefonbuch")
                cursor = conn.cursor()
                print "Connection established"
                cursor.execute("""INSERT INTO Telefonbuch (Name, Info, Nummer, Fax, Author, Datum, Sichtbar)
                        VALUES(%s, %s, %s, %s, %s, %s, %s)""",(Name, Info, Nummer, Fax, Author, Datum, Sichtbar))
                conn.commit()
                cursor.close()
                conn.close()
                self.ESuche.setText(str(self.EName.text()))
                suche()
                print "Auftrag erfolgreich"
            else:
                print ID
                conn = MySQLdb.connect(host=IP,
                                       user="radistart",
                                       passwd="radistart",
                                       db="Telefonbuch")
                cursor = conn.cursor()
                print "Connection established"
                cursor.execute("""
                        UPDATE Telefonbuch
                        SET Name=%s, Nummer=%s, Info=%s, Fax=%s, Author=%s, Datum=%s, Sichtbar=%s
                        WHERE id=%s
                        """, (Name, Nummer, Info, Fax, Author, Datum, Sichtbar, ID))
                conn.commit()
                cursor.close()
                conn.close()
                print "Auftrag erfolgreich"
                suche()
#Funktionen Ende






        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.BSuche, QtCore.SIGNAL(_fromUtf8("clicked()")), suche)
        suche()
        QtCore.QObject.connect(self.actionEditor_beenden, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.BAbbrechen, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.BAnwenden, QtCore.SIGNAL(_fromUtf8("clicked()")), run)
        QtCore.QObject.connect(self.RAendernloeschen, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update)
        QtCore.QObject.connect(self.RNeu, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.RNeu, self.ESuche)
        MainWindow.setTabOrder(self.ESuche, self.BSuche)
        MainWindow.setTabOrder(self.BSuche, self.EName_3)
        MainWindow.setTabOrder(self.EName_3, self.EInfo_3)
        MainWindow.setTabOrder(self.EInfo_3, self.ENummer_3)
        MainWindow.setTabOrder(self.ENummer_3, self.EFax_3)
        MainWindow.setTabOrder(self.EFax_3, self.EVisable_3)
        MainWindow.setTabOrder(self.EVisable_3, self.BAnwenden)
        MainWindow.setTabOrder(self.BAnwenden, self.BAbbrechen)
        MainWindow.setTabOrder(self.BAbbrechen, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.EVisable)
        MainWindow.setTabOrder(self.EVisable, self.ENummer)
        MainWindow.setTabOrder(self.ENummer, self.EFax)
        MainWindow.setTabOrder(self.EFax, self.EInfo)
        MainWindow.setTabOrder(self.EInfo, self.EName)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor für das Onlinetelefonbuch der Klinik für Radiologie und Neuroradiologie", None))
        self.tableWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Tabelle für die anzuzeigenden Daten</p></body></html>", None))
        self.tableWidget.setSortingEnabled(True)
        self.EName.setText(_translate("MainWindow", "Name", None))
        self.EInfo.setText(_translate("MainWindow", "Kurzinformation:", None))
        self.ENummer.setText(_translate("MainWindow", "Telefonnummer:", None))
        self.EFax.setText(_translate("MainWindow", "Faxnummer:", None))
        self.EVisable.setText(_translate("MainWindow", "sichtbar / unsichtbar", None))
        self.LID.setText(_translate("MainWindow", "ID", None))
        self.EName_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Namen oder eindeutige Bezeichnung eingeben.</p><p>(z.B. Dr. XYZ )</p></body></html>", None))
        self.EName_3.setText(_translate("MainWindow", "Name", None))
        self.EInfo_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ergänzende Informationen wie z.B. &quot;Pieper&quot; oder &quot;Study-Nurse&quot;</p></body></html>", None))
        self.EInfo_3.setText(_translate("MainWindow", "Info", None))
        self.ENummer_3.setText(_translate("MainWindow", "Nummer", None))
        self.EFax_3.setText(_translate("MainWindow", "Fax", None))
        self.EVisable_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sichtbar:</p><p>Der Eintrag wird im Telefonbuch normal angezeigt.</p><p><br/></p><p>Unsichtbar:</p><p>Der Eintrag wir nicht im Telefonbuch angezeigt, ist aber auch nicht gelöscht. Somit gehen keine Informationen verloren. Der Eintrag kann jederzeit bearbeitet oder sichtbar gemacht werden.</p></body></html>", None))
        self.EVisable_3.setText(_translate("MainWindow", "sichtbar / unsichtbar", None))
        self.LID_3.setText(_translate("MainWindow", "ID", None))
        self.BAnwenden.setText(_translate("MainWindow", "Anwenden", None))
        self.BAbbrechen.setText(_translate("MainWindow", "Abbrechen", None))
        self.RNeu.setText(_translate("MainWindow", "Neu eingeben      ", None))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Die Datenbank wird nach dem eingegebenen Begriff duchsucht.</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Suchbegriff eingeben:", None))
        self.ESuche.setToolTip(_translate("MainWindow", "<html><head/><body><p>Die Datenbank wird nach dem eingegebenen Begriff duchsucht.</p></body></html>", None))
        self.BSuche.setToolTip(_translate("MainWindow", "<html><head/><body><p>Die Datenbank wird nach dem eingegebenen Begriff duchsucht.</p></body></html>", None))
        self.BSuche.setText(_translate("MainWindow", "Suchen", None))
        self.RAendernloeschen.setText(_translate("MainWindow", "Ändern / Löschen", None))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Um einen Eintrag aus der Telefondatanbank auzuwählen einfach ein Feld anklicken. Die hinterlegten Daten werden dann automatisch geladen.</p><p>Die ID wird automatisch vergeben, wenn ein Eintrag erstellt wird.</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "ID in der Tabelle anklicken", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei", None))
        self.menu_ber.setTitle(_translate("MainWindow", "Über", None))
        self.actionDatenbank_exportieren.setText(_translate("MainWindow", "Datenbank exportieren", None))
        self.actionEditor_beenden.setText(_translate("MainWindow", "Editor beenden", None))
        self.actionHilfe.setText(_translate("MainWindow", "Hilfe", None))
        self.actionKontakt.setText(_translate("MainWindow", "Kontakt", None))
        self.actionLizenz.setText(_translate("MainWindow", "Lizenz", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

