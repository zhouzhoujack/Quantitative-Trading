"""
对MainWindow的主界面进行详细设置
"""
import pyautogui as pg
import time
import sys

from threading import Event
from PyQt5.QtGui import QIcon
from pynput.mouse import Listener
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QSettings, QTimer, QRegExp, QObject
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import qApp, QMessageBox, QMainWindow, QSystemTrayIcon, QAction, QMenu, QLCDNumber
from .AvgPositionForBinance import *
from PyQt5.QtGui import QTextCursor


# import win32api
# import win32con, winreg
import sys,os 
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path) 
from Forms import Ui_MyMainWindow
# from Resources import res_rc


def pushButton_2ClickedEvent(win):
    ui = win.ui

    # 关闭云同步
    if win.timer_.isActive():
        win.timer_.stop()               # 停止云同步运行
        win.duration = win.resetDuration(interval)

    win.trayIcon_.setToolTip("桌面日历自动云同步")
    ui.lcdNumber.display("00:00:00")
    ui.lineEdit.setEnabled(True)
    ui.pushButton.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    win.setWindowIcon(QIcon(r":/img/icon_off.png"))
    ui.pushButton.setText("开始执行")

    print("结束执行")

def pushButton_3ClickedEvent(win):
    ui = win.ui
    # 初始化云同步步骤的按钮的坐标位置
    def on_click(x, y, button, pressed):
        global clickTimes
        if pressed:
            print('Pressed at X: {} Y: {}'.format(x, y))
            pos.append([x, y])
            clickTimes += 1

        if clickTimes == 3:
            return False

    global pos
    pos = []

    QMessageBox.information(win, "提示", "请手动执行一次桌面日历的云同步!") 
    win.setVisible(False)

    # 连接事件以及释放
    # 这里的Listener是监听鼠标点击事件来获取桌面坐标
    """
    TODO (多线程执行完未完全退出)
    """
    with Listener(on_click=on_click) as listener:
        listener.join()

    global clickTimes
    clickTimes = 0

    # 将button的坐标保存到默认设置中，以便下次重启使用
    settings = QSettings("HXZZ", "AutoCloudSync")
    settings.beginGroup("DefaultParams")
    settings.setValue("pos", pos)
    settings.endGroup()

    win.setVisible(True)
    
    QMessageBox.information(win, "提示", "自动云同步设置完成!")
    # QTimer.singleShot(1000, )
  
    ui.pushButton.setEnabled(True)
    ui.pushButton_2.setEnabled(True)

def checkBoxClickedEvent(win):
    pass
    # ui = win.ui
    # changedFlag = ui.checkBox.isChecked()
    #
    # # 第一次设置自启动时需要检测是否初始化坐标了
    # # 若没有，那么不允许设置自启动
    # if changedFlag and len(pos) != 3:
    #     QMessageBox.warning(win, "警告", "需要进行初始化操作!")
    #     ui.checkBox.setChecked(False)
    #     return
    #
    # if changedFlag:
    # # TODO 开机自动云同步一次，并隐藏在后台执行
    #     AutoRun(switch='open', key_name='AutoCloudSync')
    # else :
    #     AutoRun(switch='close', key_name='AutoCloudSync')

# def checkKey(key_name='AutoCloudSync',
#             reg_root=win32con.HKEY_CURRENT_USER,  # 根节点
#             reg_path=r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",  # 键的路径
#             abspath=os.path.abspath(sys.argv[0])
#             ):
#     """
#     检测自启动的注册表是否已经注册程序
#     :param key_name: #  要查询的键名
#     :param reg_root: # 根节点
#         #win32con.HKEY_CURRENT_USER
#         #win32con.HKEY_CLASSES_ROOT
#         #win32con.HKEY_CURRENT_USER
#         #win32con.HKEY_LOCAL_MACHINE
#         #win32con.HKEY_USERS
#         #win32con.HKEY_CURRENT_CONFIG
#     :param reg_path: #  键的路径
#     :return: feedback(True 则已经注册过否则为False)
#     """
#     reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
#     feedback = False
#     try:
#         key = winreg.OpenKey(reg_root, reg_path, 0, reg_flags)
#         location, type = winreg.QueryValueEx(key, key_name)
#         feedback = True
#         if location != abspath:
#             feedback = 1
#             print('键存在，但程序位置发生改变')
#     except FileNotFoundError as e:
#         print("键不存在", e)
#     except PermissionError as e:
#         print("权限不足", e)
#     except:
#         print("Error")
#
#     return feedback

# def AutoRun(switch="open",
#             key_name='AutoCloudSync',
#             abspath=os.path.abspath(sys.argv[0])):
#     # 如果没有自定义路径，就用os.path.abspath(sys.argv[0])获取主程序的路径，如果主程序已经打包成exe格式，就相当于获取exe文件的路径
#
#     flag = checkKey(reg_root=win32con.HKEY_CURRENT_USER,
#                         reg_path=r"Software\\Microsoft\\Windows\\CurrentVersion\\Run",  # 键的路径
#                         key_name=key_name,
#                         abspath=abspath)
#     # 注册表项名
#     KeyName = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
#     key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
#     if switch == "open":
#         # 异常处理
#         try:
#             if not flag:
#                 win32api.RegSetValueEx(key, key_name, 0, win32con.REG_SZ, abspath)
#                 win32api.RegCloseKey(key)
#                 print('开机自启动添加成功！')
#         except:
#             print('添加失败，未知错误')
#
#     elif switch == "close":
#         try:
#             if flag:
#                 win32api.RegDeleteValue(key, key_name)  # 删除值
#                 win32api.RegCloseKey(key)
#                 print('成功删除键！')
#         except:
#             print('删除失败,未知错误！')

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

        # 定时器执行的间隔时间
        # self.duration = self.resetDuration(interval)

        # 定时器用于定时执行脚本
        self.timer_ = QTimer(self)

        # 系统托盘
        # self.trayIcon_ = QSystemTrayIcon()
        # self.trayIcon_.activated.connect(self.trayClick)
        # self.trayIcon_.installEventFilter(MouseHoverEvent(self.trayIcon_))
        # self.trayIcon_.setToolTip("桌面日历自动云同步")
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

    def widgetsSetting(self):
        self.ui.startPushButton.clicked.connect(lambda : self.onStartPushButtonClickedEvent())
        self.ui.testConnectPushButton.clicked.connect(lambda : self.onTestConnectPushButtonClickedEvent())        # 下面将输出重定向到textEdit中
        self.timer_.timeout.connect(lambda: self.refreshTimerSlot())

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
        else:
            QMessageBox.information(self, "Connect Successfully", " 连接交易所成功！", QMessageBox.Yes)

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

        # 将页面参数保存到默认设置中，以便下次应用重启使用
        settings = QSettings("hxzz", "Quan_trading")
        settings.beginGroup("DefaultParams")
        settings.setValue("all_params_info", self.all_params_info)
        settings.endGroup()

        # 利用定时器在后台执行策略
        self.strategy = init_setting_of_strategy(self.all_params_info)
        self.timer_.setInterval(self.all_params_info['run_interval']*1000)
        self.timer_.start()

    def loadDefaultSettings(self):
        ui = self.ui
        # 用户第一次进程序，未保存任何设置参数
        # 若第二次进入，则加载上次参数设置
        settings = QSettings("hxzz", "Quan_trading")
        settings.beginGroup("DefaultParams")

        self.all_params_info = settings.value("all_params_info")
        if self.all_params_info is None:
            return

        ui.keyLineEdit.setText(self.all_params_info['key'])
        ui.secretLineEdit.setText(self.all_params_info['secret'])
        ui.volaLineEdit.setText(str(self.all_params_info['volatility']))
        ui.minAmountLineEdit.setText(str(self.all_params_info['min_amount']))
        ui.checkBox.setCheckable(self.all_params_info['auto_start_flag'])
        ui.minTradeQuanLineEdit.setText(str(self.all_params_info['min_trading_limit']))
        ui.intervalLineEdit.setText(str(self.all_params_info['run_interval']))

    def refreshTimerSlot(self):
        # 定时器的槽函数
        if(self.strategy.make_need_account_info()):
            self.strategy.if_need_trade('price', self.all_params_info['volatility'])

    #
    #     formatTime = seconds2time(win.duration)
    #     ui.lcdNumber.display(formatTime)
    #     win.trayIcon_.setToolTip(formatTime)

    # if leText == '':
    #     QMessageBox.warning(win, "提示", "请输入云同步间隔时间!")
    #     return
    #
    # if not ((interval > 0.1 and interval < 0.9 ) or (interval > 0 and interval < 10)):
    #     QMessageBox.warning(win, "提示", "请输入合法数据!")
    #     return

    # 将页面参数保存到默认设置中，以便下次应用重启使用，这里secret不保存
    # settings = QSettings("HXZZ", "AutoCloudSync")
    # settings.beginGroup("DefaultParams")
    # settings.setValue("interval", interval)
    # settings.endGroup()

    def changeEvent(self, event):
        """
        重写窗口状态改变函数
        """
        pass

        # def _showTrayIconMesg():
        #     self.trayIcon_.showMessage("桌面日历自动云同步","已最小化至托盘")
        #
        # if event.type() == QtCore.QEvent.WindowStateChange:
        #     if self.windowState() & QtCore.Qt.WindowMinimized:
        #         event.ignore()
        #         print("窗口最小化")
        #         quitAction = QAction(u"退出", self, triggered=qApp.quit)
        #         resetScriptAction = QAction(u"重置运行", self, triggered=self.resetScript)
        #         menu = QMenu()
        #         menu.addAction(resetScriptAction)
        #         menu.addAction(quitAction)
        #         self.trayIcon_.setContextMenu(menu)
        #         self.trayIcon_.setIcon(QIcon(r":/img/icon_off.png"))
        #
        #         if not self.ui.pushButton.isEnabled():
        #             self.trayIcon_.setIcon(QIcon(r":/img/icon_on.png"))
        #
        #         QTimer.singleShot(1000, lambda : _showTrayIconMesg())
        #
        #         self.hide()
        #         self.trayIcon_.show()
                
