from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # qfile_stats = QFile("test.ui")
        # qfile_stats.open(QFile.ReadOnly)
        # qfile_stats.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui_v2/func3_3_12.ui')
        # self.ui.actionquit.triggered.connect(QCoreApplication.instance().quit)

    
    # def help(self):
    
app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()