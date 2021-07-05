from PyQt5 import QtWidgets
from py.func6_1 import Ui_Form

class mywindow(QtWidgets.QWidget, Ui_Form):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())

