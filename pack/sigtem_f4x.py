from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene

import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from py.func4_1 import Ui_Form as f41
from py.func4_2 import Ui_Form as f42
from py.func4_3 import Ui_Form as f43
from py.func4_4 import Ui_Form as f44
from py.func4_5 import Ui_Form as f45
from py.func4_6 import Ui_Form as f46
from py.func4_7 import Ui_Form as f47
from py.func1_5 import Ui_Form as f15
 
import numpy as np
import sigtem as st
import sigtem.ct_signals as ctsg
import sigtem.dt_signals as dtsg
import os
'''
self.pushButton_2.setText(_translate("Form", "连续矩形波信号"))
self.pushButton_3.setText(_translate("Form", "离散单位冲激信号"))
self.pushButton_5.setText(_translate("Form", "离散单位阶跃信号"))
self.pushButton_6.setText(_translate("Form", "离散复指数信号"))
self.pushButton_7.setText(_translate("Form", "离散Sa函数"))

'''

class f15_window(QWidget,f15):
    '''
    报错
    '''
    def __init__(self):
        super(f15_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class f47_window(QWidget,f47):
    '''
    图像
    '''
    def __init__(self):
        super(f47_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)


###################################   child window   ############################

class f42_window(QWidget,f42):
    '''
    连续矩形波
    '''
    def __init__(self):
        super(f42_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f47c = f47_window()
        self.scene = QGraphicsScene()
        self.pushButton_4.clicked.connect(self.show_ft_str)
        self.pushButton_2.clicked.connect(self.show_ft_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close
    
    def show_ft_str(self):
        t1 = self.lineEdit.text()
        try:
            now_sg =  ctsg.ct_rect(eval(t1))    #注意这里的t1
            new_sg = now_sg.get_ft()
            self.textBrowser.setText(str(new_sg.get_sname()))
        except Exception as e:
            print(e)
            self.error()

    def show_ft_window(self):
        t1 = self.lineEdit.text()
        try:
            now_sg =  ctsg.ct_rect(eval(t1))
            sgname = "rc_ft"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg = now_sg.get_ft()
            new_sg.save(now_path,"real")
            self.scene.addPixmap(QPixmap(now_path))
            self.f47c.graphicsView.setScene(self.scene)
            self.f47c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()

class f43_window(QWidget,f43):
    '''
    x = kδ[n - n0]
    '''
    def __init__(self):
        super(f43_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f47c = f47_window()
        self.scene = QGraphicsScene()
        self.pushButton_4.clicked.connect(self.show_ft_str)
        self.pushButton_2.clicked.connect(self.show_ft_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close
    
    def show_ft_str(self):
        k = self.lineEdit.text()
        n0 = self.lineEdit_2.text()
        try:
            now_sg =  dtsg.dt_impulse(t0 = eval(n0),k = eval(k))   
            new_sg = now_sg.get_ft()
            
            self.textBrowser.setText(str(new_sg.get_sname()))
        except Exception as e:
            print(e)
            self.error()

    def show_ft_window(self):
        k = self.lineEdit.text()
        n0 = self.lineEdit_2.text()
        try:
            now_sg =  st.dt_impulse(t0 = eval(n0),k = eval(k))
            new_sg = now_sg.get_ft()
            sgname = "离散单位冲激的傅里叶变换"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg.save_all(now_path)
            self.scene.addPixmap(QPixmap(now_path))
            self.f47c.graphicsView.setScene(self.scene)
            self.f47c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()

class f44_window(QWidget,f44):
    '''
    dt_unit_step
    '''
    def __init__(self):
        super(f44_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f47c = f47_window()
        self.scene = QGraphicsScene()
        self.pushButton_4.clicked.connect(self.show_ft_str)
        self.pushButton_2.clicked.connect(self.show_ft_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close
    
    def show_ft_str(self):
        try:
            now_sg =  st.dt_unit_step() 
            new_sg = now_sg.get_ft()
            
            self.textBrowser.setText(str(new_sg.get_sname()))
        except Exception as e:
            print(e)
            self.error()

    def show_ft_window(self):

        try:
            now_sg =  st.dt_unit_step()
            new_sg = now_sg.get_ft()
            sgname = '离散单位阶跃的傅里叶变换'  
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg.save_all(now_path)
            self.scene.addPixmap(QPixmap(now_path))
            self.f47c.graphicsView.setScene(self.scene)
            self.f47c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()

class f45_window(QWidget,f45):
    '''
    离散复指数信号
    '''
    def __init__(self):
        super(f45_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f47c = f47_window()
        self.scene = QGraphicsScene()
        self.pushButton_4.clicked.connect(self.show_ft_str)
        self.pushButton_2.clicked.connect(self.show_ft_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close
    
    def show_ft_str(self):
        k = self.lineEdit_3.text()
        s = self.lineEdit_4.text()
        a = self.lineEdit_5.text()
        b = self.lineEdit_6.text()
        try:
            now_sg =  st.dt_exp(eval(k),eval(a),eval(b),eval(s))
            new_sg = now_sg.get_ft()
            
            self.textBrowser.setText(str(new_sg.get_sname()))
        except Exception as e:
            print(e)
            self.error()

    def show_ft_window(self):
        k = self.lineEdit_3.text()
        s = self.lineEdit_4.text()
        a = self.lineEdit_5.text()
        b = self.lineEdit_6.text()
        try:
            now_sg =  st.dt_exp(eval(k),eval(a),eval(b),eval(s))
            new_sg = now_sg.get_ft()
            sgname = "离散复指数信号的傅里叶变换" 
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f47c.graphicsView.setScene(self.scene)
            self.f47c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()


class f46_window(QWidget,f46):
    '''
    离散sa函数
    '''
    def __init__(self):
        super(f46_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f47c = f47_window()
        self.scene = QGraphicsScene()
        self.pushButton_4.clicked.connect(self.show_ft_str)
        self.pushButton_2.clicked.connect(self.show_ft_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close
    
    def show_ft_str(self):
        try:
            now_sg =  st.dt_sample()
            new_sg = now_sg.get_ft()
            
            self.textBrowser.setText(str(new_sg.get_sname()))
        except Exception as e:
            print(e)
            self.error()

    def show_ft_window(self):

        try:
            now_sg =  st.dt_unit_step()
            new_sg = now_sg.get_ft()
            sgname = "离散Sample函数的傅里叶变换"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg.save_all(now_path)
            self.scene.addPixmap(QPixmap(now_path))
            self.f47c.graphicsView.setScene(self.scene)
            self.f47c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()


