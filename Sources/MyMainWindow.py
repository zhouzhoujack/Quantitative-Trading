"""
对MainWindow的主界面进行详细设置
"""
import time
import sys
import os

from threading import Event
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QSettings, QTimer, QRegExp, QObject, QThread,pyqtSignal
from PyQt5.QtWidgets import qApp, QMessageBox, QMainWindow, QAction, QMenu, QLabel
from PyQt5.QtGui import QTextCursor

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from .AvgPositionForBinance import *
from Forms import Ui_MyMainWindow
from Resources import res_rc

class TimeThread(QThread):
    """
    多线程动态显示时间
    """
    time_signal = pyqtSignal(str)      # 定义时间变化信号

    def __init__(self):
        super().__init__()
        self.run_seconds = 0
        self.stop_flag = False      # 控制线程的停止

    def stopThread(self):
        self.stop_flag = True
        self.run_seconds = 0

    def run(self):
        """
        开一条线程，在状态栏显示策略的运行时间
        """
        self.stop_flag = False
        while(not self.stop_flag):
            self.time_signal.emit(seconds2time(self.run_seconds))            # 发送信号让statusbar更新时间
            time.sleep(1)
            self.run_seconds += 1

def seconds2time(seconds):
    # 将秒转换为xx-day 00:00:00格式的时间
    d = seconds //  (3600 * 24)
    h = (seconds // 3600) % 24
    m = (seconds // 60) % 60
    s = seconds % 60
    h = str(h) if h >= 10 else '0' + str(h)
    m = str(m) if m >= 10 else '0' + str(m)
    s = str(s) if s >= 10 else '0' + str(s)
    return "%s day %s:%s:%s"%(d, h, m, s)

# 重定向信号
class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
        # loop = QEventLoop()
        # QTimer.singleShot(1000, loop.quit)
        # loop.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 将console的内容重定向到textEdit中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        # 定时器用于定时执行脚本
        self.timer_ = QTimer(self)

        # 显示动态时间的线程
        self.run_time_thread = TimeThread()
        self.run_time_thread.time_signal.connect(self.showRunTime)

        self.all_params_info = {}

        # 界面的UI初始化,这部分代码由QT编译器自动生成，不用动
        self.ui = Ui_MyMainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # 加载上次策略的参数设置
        self.loadDefaultSettings()

        # 界面的一些设置
        self.windowSetting()

        # 控件的事件绑定和状态检测
        self.widgetsSetting()

    def outputWritten(self, text):
        # 将console的内容写入textedit空间中
        cursor = self.ui.logTextEdit.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.logTextEdit.setTextCursor(cursor)
        self.ui.logTextEdit.ensureCursorVisible()

    def windowSetting(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(":/img/icon.png"));

        # status bar
        self.connect_status_label = QLabel(self)
        status_bar = self.statusBar()
        status_bar.addPermanentWidget(self.connect_status_label)

    def widgetsSetting(self):
        self.ui.startPushButton.clicked.connect(lambda : self.onStartPushButtonClickedEvent())
        self.ui.stopPushButton.clicked.connect(lambda: self.onStopPushButtonClickedEvent())
        self.ui.clearPushButton.clicked.connect(lambda: self.onClearPushButtonClickedEvent())
        self.ui.testConnectPushButton.clicked.connect(lambda : self.onTestConnectPushButtonClickedEvent())        # 下面将输出重定向到textEdit中
        self.timer_.timeout.connect(lambda: self.refreshTimerSlot())

    def onClearPushButtonClickedEvent(self):
        # 清除日志
        self.ui.logTextEdit.clear()

    def onTestConnectPushButtonClickedEvent(self):
        ui = self.ui
        ui.testConnectPushButton.setEnabled(False)

        key = ui.keyLineEdit.text()
        secret = ui.secretLineEdit.text()

        if len(key) == 0 or len(secret) == 0:
            QMessageBox.warning(self, "Warning", "请提供交易所API密钥!", QMessageBox.Yes)
            return

        connect_flag, usdt, eth  = test_connect_exchange(key, secret)
        ui.usdtLineEdit.setText(str(usdt))
        ui.ethLineEdit.setText(str(eth))

        if not connect_flag:
            QMessageBox.critical(self, "Connect Error", " 连接交易所失败，请检查日志文件！", QMessageBox.Yes)
            self.connect_status_label.setText("交易所连接失败")
        else:
            QMessageBox.information(self, "Connect Successfully", " 连接交易所成功！", QMessageBox.Yes)
            self.connect_status_label.setText("交易所连接成功")

        ui.testConnectPushButton.setEnabled(True)

    def onStartPushButtonClickedEvent(self):
        ui = self.ui
        # Api密钥
        key = ui.keyLineEdit.text()
        secret = ui.secretLineEdit.text()

        if len(key) == 0 or len(secret) == 0:
            QMessageBox.warning(self, "Warning", "请提供交易所API密钥!", QMessageBox.Yes)
            return

        # 策略超参数
        volatility = ui.volaLineEdit.text()
        min_amount = ui.minAmountLineEdit.text()

        if len(volatility) == 0 or len(min_amount) == 0:
            QMessageBox.warning(self, "Warning", "请提供策略超参数!", QMessageBox.Yes)
            return

        # 其他设置
        auto_start_flag = ui.checkBox.isChecked()
        min_trading_limit = ui.minTradeQuanLineEdit.text()
        run_interval = ui.intervalLineEdit.text()
        ding_token = ui.tokenLineEdit.text()
        ding_secret = ui.secretLineEdit.text()

        if len(min_trading_limit) == 0 or len(run_interval) == 0:
            QMessageBox.warning(self, "Warning", "请提供其他设置!", QMessageBox.Yes)
            return

        # 获取所有参数信息
        self.all_params_info['key'] = key
        self.all_params_info['secret'] = secret
        self.all_params_info['volatility'] = float(volatility)
        self.all_params_info['min_amount'] = float(min_amount)
        self.all_params_info['auto_start_flag'] = auto_start_flag
        self.all_params_info['min_trading_limit'] = float(min_trading_limit)
        self.all_params_info['run_interval'] = int(run_interval)
        self.all_params_info['ding_access_token'] = ding_token
        self.all_params_info['ding_secret'] = ding_secret

        # 将页面参数保存到默认设置中，以便下次应用重启使用
        settings = QSettings("hxzz", "Quan_trading")
        settings.beginGroup("DefaultParams")
        settings.setValue("all_params_info", self.all_params_info)
        settings.endGroup()

        # 利用定时器在后台执行策略
        self.strategy = init_setting_of_strategy(self.all_params_info)
        self.timer_.setInterval(self.all_params_info['run_interval']*1000)
        self.timer_.start()

        # 开始计算策略的执行时间，显示在状态栏
        self.run_time_thread.start()

        # 开放停止按钮
        ui.stopPushButton.setEnabled(True)
        ui.startPushButton.setEnabled(False)
        ui.startPushButton.setText("运行中..")

    def showRunTime(self, run_time):
        self.statusBar().showMessage("策略已运行: "+run_time)

    def onStopPushButtonClickedEvent(self):
        ui = self.ui

        # 停止策略运行
        self.run_time_thread.stopThread()
        self.run_time_thread.wait();
        self.timer_.stop()

        strategy_status_info = {}
        strategy_status_info['eth'] = 0
        strategy_status_info['usdt'] = 0
        strategy_status_info['last'] = 0
        strategy_status_info['need_buy'] = 0
        strategy_status_info['need_sell'] = 0
        strategy_status_info['last_trade_price'] = 0
        self.updateStrategyStatusInfo(strategy_status_info)

        ui.startPushButton.setEnabled(True)
        ui.startPushButton.setText("启动")

        ui.logTextEdit.clear()

    def loadDefaultSettings(self):
        ui = self.ui
        # 用户第一次进程序，未保存任何设置参数
        # 若第二次进入，则加载上次参数设置
        settings = QSettings("hxzz", "Quan_trading")
        settings.beginGroup("DefaultParams")

        all_params_info = settings.value("all_params_info")
        if all_params_info is None:
            return

        try:
            ui.keyLineEdit.setText(all_params_info['key'])
            ui.secretLineEdit.setText(all_params_info['secret'])
            ui.volaLineEdit.setText(str(all_params_info['volatility']))
            ui.minAmountLineEdit.setText(str(all_params_info['min_amount']))
            ui.checkBox.setCheckable(all_params_info['auto_start_flag'])
            ui.minTradeQuanLineEdit.setText(str(all_params_info['min_trading_limit']))
            ui.intervalLineEdit.setText(str(all_params_info['run_interval']))
            ui.tokenLineEdit.setText(all_params_info['ding_access_token'])
            ui.ding_secretLineEdit.setText(all_params_info['ding_secret'])
        except Exception as e:
            print("Miss some default params!")

    def refreshTimerSlot(self):
        # 定时器的槽函数
        flag, strategy_status_info = self.strategy.make_need_account_info()
        if(flag):
            self.connect_status_label.setText("交易所连接成功")
            self.strategy.if_need_trade('price', self.all_params_info['volatility'])
            self.updateStrategyStatusInfo(strategy_status_info)
        else:
            self.connect_status_label.setText("交易所连接失败")

    def updateStrategyStatusInfo(self, status_info):
        ui = self.ui
        ui.usdtLineEdit.setText(str(status_info['usdt']))
        eth_usdt = status_info['eth']*status_info['last']

        ui.ethLineEdit.setText(str(status_info['eth'])+'('+str(round(eth_usdt, 2))+')')

        ui.buyLineEdit.setText(str(round(status_info['need_buy'], 6)))
        ui.sellLineEdit.setText(str(round(status_info['need_sell'], 6)))

        if status_info['last_trade_price'] != 0:
            amplitude = 100*(status_info['last']-status_info['last_trade_price'])/status_info['last_trade_price']
        else:
            amplitude = 0

        ui.lastLineEdit.setText(str(status_info['last'])+'('+str(round(amplitude, 4))+'%)')
        ui.lastTradingPriceLineEdit.setText(str(round(status_info['last_trade_price'], 2)))

    def closeEvent(self, event):
        if(self.run_time_thread.isRunning()):
            self.run_time_thread.stopThread()
            self.run_time_thread.wait()


                
