import sys
from PyQt5.QtWidgets import QApplication
from Sources import MyMainWindow

# 测试
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # print(sys.argv[0])
    # print(qApp.applicationFilePath())
    # print(os.path.realpath(sys.executable))
    window = MyMainWindow.MainWindow()
    window.show()
    sys.exit(app.exec_())

