# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 30, 401, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.keyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.keyLineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.secretLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.secretLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secretLineEdit.setObjectName("secretLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.secretLineEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 100, 401, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 401, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.volaLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.volaLineEdit.setObjectName("volaLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.volaLineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.minAmountLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.minAmountLineEdit.setObjectName("minAmountLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.minAmountLineEdit)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 200, 401, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 401, 67))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.minTradeQuanLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.minTradeQuanLineEdit.setObjectName("minTradeQuanLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.minTradeQuanLineEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.checkBox.setText("")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.intervalLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.intervalLineEdit.setObjectName("intervalLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.intervalLineEdit)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 590, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.startPushButton = QtWidgets.QPushButton(self.groupBox)
        self.startPushButton.setGeometry(QtCore.QRect(150, 610, 111, 31))
        self.startPushButton.setObjectName("startPushButton")
        self.testConnectPushButton = QtWidgets.QPushButton(self.groupBox)
        self.testConnectPushButton.setGeometry(QtCore.QRect(0, 610, 111, 31))
        self.testConnectPushButton.setObjectName("testConnectPushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 320, 401, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 20, 401, 171))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.usdtLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.usdtLineEdit.setReadOnly(True)
        self.usdtLineEdit.setObjectName("usdtLineEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usdtLineEdit)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ethLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.ethLineEdit.setReadOnly(True)
        self.ethLineEdit.setObjectName("ethLineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ethLineEdit)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.buyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.buyLineEdit.setObjectName("buyLineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buyLineEdit)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.sellLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.sellLineEdit.setObjectName("sellLineEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sellLineEdit)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lastLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lastLineEdit.setObjectName("lastLineEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lastLineEdit)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.stopPushButton = QtWidgets.QPushButton(self.groupBox)
        self.stopPushButton.setGeometry(QtCore.QRect(290, 610, 111, 31))
        self.stopPushButton.setObjectName("stopPushButton")
        self.verticalLayout.addWidget(self.groupBox)
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(430, 10, 771, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "均仓策略（仅支持币安/ETH-USDT现货）   联系作者：1259419892@qq.com"))
        self.groupBox.setTitle(_translate("MainWindow", "Api密钥"))
        self.label.setText(_translate("MainWindow", "key"))
        self.label_2.setText(_translate("MainWindow", "secret"))
        self.groupBox_2.setTitle(_translate("MainWindow", "策略超参数"))
        self.label_3.setText(_translate("MainWindow", "波动率（%）"))
        self.label_4.setText(_translate("MainWindow", "最小交易数量(>0.001)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "其他设置"))
        self.label_5.setText(_translate("MainWindow", "最小交易额（usdt）"))
        self.label_6.setText(_translate("MainWindow", "开机自启"))
        self.label_9.setText(_translate("MainWindow", "执行间隔（S）"))
        self.startPushButton.setText(_translate("MainWindow", "启动"))
        self.testConnectPushButton.setText(_translate("MainWindow", "测试连接"))
        self.groupBox_4.setTitle(_translate("MainWindow", "策略状态"))
        self.label_7.setText(_translate("MainWindow", "USDT"))
        self.label_8.setText(_translate("MainWindow", "ETH"))
        self.label_10.setText(_translate("MainWindow", "Buy"))
        self.label_11.setText(_translate("MainWindow", "Sell"))
        self.label_12.setText(_translate("MainWindow", "last price"))
        self.label_13.setText(_translate("MainWindow", "last trade price"))
        self.stopPushButton.setText(_translate("MainWindow", "停止"))
