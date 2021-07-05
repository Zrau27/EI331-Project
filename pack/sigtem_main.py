from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtWidgets import QGraphicsScene, QMainWindow,QWidget,QDialog
from PyQt5.QtGui import QPixmap
import numpy as np
import time
import os

from py.menu import Ui_Form as menu_uf 
from py.func1_1 import Ui_Form as f11                    
from py.func2_1 import Ui_Form as f21
from py.func3_1 import Ui_Form as f31
from py.func4_1 import Ui_Form as f41
from py.func5_1 import Ui_Form as f51
from py.func6_1 import Ui_Form as f61
from py.func_def import Ui_Form as df


import sigtem_f1x as f1x
import sigtem_f2x as f2x
import sigtem_f3x as f3x
import sigtem_f4x as f4x
import sigtem_f5x as f5x
import sigtem_f6x as f6x
import sigtem as st



"""
    f1 -> 任意信号图像展示
    f2 -> 典型信号波形展示
    f3 -> 典型信号卷积和
    f4 -> 典型信号傅里叶变换
    f5 -> 周期信号傅里叶级数
    f6 -> 采样

    self.label.setText(_translate("Form", "信号与系统软件"))
    self.pushButton.setText(_translate("Form", "任意信号图像展示"))
    self.pushButton_2.setText(_translate("Form", "典型信号波形展示"))
    self.pushButton_3.setText(_translate("Form", "典型信号卷积（和）"))
    self.pushButton_4.setText(_translate("Form", "典型信号傅里叶变换"))
    self.pushButton_5.setText(_translate("Form", "周期信号傅里叶级数"))
    self.pushButton_6.setText(_translate("Form", "连续信号离散处理"))
    self.pushButton_7.setText(_translate("Form", "退出"))
"""

class f11_window(QWidget,f11):
    def __init__(self):
        super(f11_window,self).__init__()
        self.setupUi(self)
        self.f12c_1 = f1x.f12_window_1()
        self.f12c_2 = f1x.f12_window_2()
        self.f13c = f1x.f13_window()
        
        self.pushButton.clicked.connect(self.show_f12_1)  
        self.pushButton_2.clicked.connect(self.show_f12_2)
        self.pushButton_3.clicked.connect(self.show_f13)

    def show_f12_1(self):
        self.f12c_1.show()
    def show_f12_2(self):
        self.f12c_2.show()
    def show_f13(self):
        self.f13c.show()

class f21_window(QWidget,f21):
    '''
    典型信号波形展示
    '''
    def __init__(self):
        super(f21_window,self).__init__()
        self.setupUi(self) 
        self.f22_child = f2x.f22_window()
        self.f23_child = f2x.f23_window()    #实例化f22,f23
        self.pushButton_2.clicked.connect(self.show_f22)   #连续信号
        self.pushButton_3.clicked.connect(self.show_f23)   #离散信号

    def show_f22(self):
        self.f22_child.show()
    def show_f23(self):
        self.f23_child.show()

class f31_window(QWidget,f31):
    '''
    典型信号卷积和  *结果为值还是图像
    '''
    def __init__(self):
        super(f31_window,self).__init__()
        self.setupUi(self)
        self.f33_child = f3x.f33_window()
        self.f34_child = f3x.f34_window()
        self.pushButton_2.clicked.connect(self.show_f33)
        self.pushButton_3.clicked.connect(self.show_f34)
        self.pushButton.clicked.connect(self.close)
    
    def show_f33(self):
        self.f33_child.show()
    def show_f34(self):
        self.f34_child.show()

class f41_window(QWidget,f41):
    '''
    典型信号傅里叶变换 *展示图片+解析式
    '''
    def __init__(self):
        super(f41_window,self).__init__()
        self.setupUi(self)
        self.f42c = f4x.f42_window() 
        self.f43c = f4x.f43_window()
        self.f44c = f4x.f44_window()
        self.f45c = f4x.f45_window()
        self.f46c = f4x.f46_window()
        self.pushButton_2.clicked.connect(self.show_f42)
        self.pushButton_3.clicked.connect(self.show_f43)
        self.pushButton_5.clicked.connect(self.show_f44)
        self.pushButton_6.clicked.connect(self.show_f45)
        self.pushButton_7.clicked.connect(self.show_f46)
        self.pushButton_4.clicked.connect(self.close)
    
    def show_f42(self):
        self.f42c.show()
    def show_f43(self):
        self.f43c.show()
    def show_f44(self):
        self.f44c.show()
    def show_f45(self):
        self.f45c.show()
    def show_f46(self):
        self.f46c.show()

class f51_window(QWidget,f51):
    def __init__(self):
        super(f51_window,self).__init__()
        self.setupUi(self)
        self.f52c = f5x.f52_window()
        self.f53c = f5x.f53_window()
        self.f54c = f5x.f54_window()
        self.pushButton_2.clicked.connect(self.show_f52)
        self.pushButton.clicked.connect(self.show_f53)
        self.pushButton_3.clicked.connect(self.show_f54)
        self.pushButton_4.clicked.connect(self.close)

    def show_f52(self):
        self.f52c.show()
    def show_f53(self):
        self.f53c.show()
    def show_f54(self):
        self.f54c.show()

class f61_window(QWidget,f61):
    def __init__(self):
        super(f61_window,self).__init__()
        self.setupUi(self)
        self.f62c = f6x.f62_window()
        self.f15c = f1x.f15_window()
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()

        self.pushButton_2.clicked.connect(self.f62_show)
        self.pushButton_7.clicked.connect(self.close)
    
    def error(self):
        self.f15c.show

    def f62_show(self):
        omega = self.lineEdit.text()
        given_code = self.textEdit.toPlainText()
        try:
            def s(t):
                return eval(given_code)
            org_sg = st.ct_signal()
            org_sg.set_function(function=s)
            am_sg = st.am_mdlt_t(org_sg,eval(omega))
            ft_sg = st.ft(org_sg)
            am_ft_sg = st.am_mdlt_s(ft_sg,eval(omega))
            
            
            path1 = os.getcwd() + r'{}'.format('sg_t')+'.png'
            path2 = os.getcwd() + r'{}'.format('sg_s')+'.png'
        

            am_sg.save(path1,'real')
            am_ft_sg.save(path2,'real')
            
            self.scene1.addPixmap(QPixmap(path1))
            self.f62c.graphicsView.setScene(self.scene1)
            self.scene2.addPixmap(QPixmap(path2))
            self.f62c.graphicsView_2.setScene(self.scene2)
            self.f62c.show()
            os.remove(path1)
            os.remove(path2)



        except Exception as e:
            print(e)
            self.error

class df_window(QWidget,df):
    def __init__(self):
        super(df_window,self).__init__()
        self.setupUi(self)

class main_window(QWidget, menu_uf):
    def  __init__ (self):
        super(main_window, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.show_f41)
        self.pushButton_2.clicked.connect(self.show_f21)
        self.pushButton_3.clicked.connect(self.show_f31)
        self.pushButton.clicked.connect(self.show_f11)
        self.pushButton_5.clicked.connect(self.show_f51)
        self.pushButton_6.clicked.connect(self.show_f61)
        self.pushButton_7.clicked.connect(self.close)
        self.pushButton_8.clicked.connect(self.show_df)
       
        

    def show_f11(self): 
        f11_child.show()

    def show_f21(self):
        f21_child.show()

    def show_f31(self):
        f31_child.show()

    def show_f41(self):
        f41_child.show()
        
    def show_f51(self):
        f51_child.show()

    def show_f61(self):
        f61_child.show()
    
    def show_df(self):
        func_df.show()

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    menu_main = main_window() 
    f11_child = f11_window()
    f21_child = f21_window()
    f31_child = f31_window()
    f41_child = f41_window()
    f51_child = f51_window()
    f61_child = f61_window()
    func_df = df_window()
    menu_main.show()
    
    sys.exit(app.exec_())


"""
两连续矩形信号

"""
