from re import I, T
from sys import dont_write_bytecode
from sigtem_f1x import f14_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene
import _thread

import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from py.func5_1 import Ui_Form as f51
from py.func5_2 import Ui_Form as f52
from py.func5_3 import Ui_Form as f53
from py.func5_4 import Ui_Form as f54
from py.func5_41 import Ui_Form as f541
from py.func5_42 import Ui_Form as f542
from py.func5_43 import Ui_Form as f543
from py.func5_44 import Ui_Form as f544
from py.func5_45 import Ui_Form as f545
from py.func5_5 import Ui_Form as f55
from py.func5_6 import Ui_widget as f56
from py.func1_5 import Ui_Form as f15

import sigtem as st
import sigtem.ct_signals as ctsg
import sigtem.dt_signals as dtsg
import numpy as np
import os

pub_func = 0
pub_T = 1



class f15_window(QWidget,f15):
    '''
    用于报错
    '''
    def __init__(self):
        super(f15_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        
class f56_window(QWidget,f56):
    '''
    Nth Partial sum of fs 的图像
    '''
    def __init__(self):
        super(f56_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        

class f55_window(QWidget,f55):
    '''
    图像,以及 Nth Partial sum of fs
    '''
    def __init__(self):
        super(f55_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f56c = f56_window()
        self.scene = QGraphicsScene()
        self.pushButton.clicked.connect(self.show_Nthsum)
        
    
    def show_Nthsum(self):
        N = self.lineEdit.text()
        try:
            Nthsum = st.ifs(pub_func,eval(N),pub_T)
            sgname = "Nthsum"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'

            Nthsum.save(now_path,"real")
            self.scene.addPixmap(QPixmap(now_path))
            self.f56c.graphicsView.setScene(self.scene)
            self.f56c.show()
            os.remove(now_path)
        except Exception as e:
            print(e)
    
  
        
    


#########################################    常用   ##################################
class f541_window(QWidget,f541):
    '''
    连续周期方波信号
    '''
    def __init__(self):
        super(f541_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_fs_window)
        self.pushButton_4.clicked.connect(self.show_fs_str)
        self.pushButton_7.clicked.connect(self.close)
        self.f15c = f15_window()
        self.f55c = f55_window()
       
        self.scene = QGraphicsScene()

    
    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close

    def show_fs_str(self):
        T = self.lineEdit.text()
        T0 = self.lineEdit_2.text()
        try:
            now_sg = st.ct_rect_period(T1 = eval(T0),T = eval(T))
            new_sg = now_sg.get_fs(t1=-1000,t2=1000)
            sgname = new_sg.get_sname()
            self.textBrowser.setText(str(sgname))
        except Exception as e:
            self.error()
            print(e)

    def show_fs_window(self):
        T = self.lineEdit.text()
        T0 = self.lineEdit_2.text()
        try:
            now_sg =  ctsg.ct_rect_period(T1 = eval(T0),T = eval(T))
            sgname = "fs_ctrcp"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            new_sg = now_sg.get_fs()

            global pub_func     #改变全局变量
            global pub_T
            print(pub_T)
            pub_func = new_sg
            pub_T = eval(T)

            new_sg.save(now_path,"real")
            self.scene.addPixmap(QPixmap(now_path))
            self.f55c.graphicsView.setScene(self.scene)
            self.f55c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.error()

 


######################################   任意周期信号   ##################################
class f52_window(QWidget,f52):
    '''
    连续
    '''
    def __init__(self):
        super(f52_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f55c = f55_window()
        self.scene = QGraphicsScene()

     
        self.pushButton_4.clicked.connect(self.show_fs_str)
        self.pushButton_2.clicked.connect(self.show_fs_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):
        self.f15c.show()
    
    def close(self):
        self.close()
    
    def show_fs_str(self):
        given_func = self.textEdit.toPlainText()
        T = self.lineEdit_2.text()
        try:
            def tempf(t):
                return eval(given_func)
            now_sg = st.ct_signal()         
            now_sg.set_function(function = tempf, period = eval(T))    #构建信号
            new_sg = st.fs(now_sg,start=-1000,end = 1000)      #计算傅里叶级数
            self.textBrowser.setText(new_sg.get_sname())     
        except Exception as e:
            print(e)

    def show_fs_window(self):
        given_func = self.textEdit.toPlainText()
        T = self.lineEdit_2.text()
        try:
            def tempf(t):
                return eval(given_func)
            
            now_sg = st.ct_signal()
            now_sg.set_function(function = tempf, period = eval(T))

            sgname = "fsctf"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'

            new_sg = st.fs(now_sg,start=-1000,end = 1000)
            global pub_T,pub_func
            pub_func = new_sg
            pub_T = eval(T)

            new_sg.save(now_path,"real")
            self.scene.addPixmap(QPixmap(now_path))
            self.f55c.graphicsView.setScene(self.scene)
            self.f55c.show()
            os.remove(now_path)

        except Exception as e:
            print(e)


class f53_window(QWidget,f53):
    '''
    离散
    '''
    def __init__(self):
        super(f53_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.f55c = f55_window()
        self.scene = QGraphicsScene()
     
        self.pushButton_4.clicked.connect(self.show_fs_str)
        self.pushButton_2.clicked.connect(self.show_fs_window)
        self.pushButton_7.clicked.connect(self.close)

    def error(self):      #报错
        self.f15c.show()
    
    def close(self):     #关闭
        self.close()
    
    def show_fs_str(self):        #展示解析式
        given_func = self.textEdit.toPlainText()
        T = self.lineEdit_2.text()
        try:
            def tempf(n):
                return eval(given_func)
            now_sg = st.dt_signal()
            now_sg.set_function(function = tempf, period = eval(T))
            new_sg = st.fs(now_sg)
            self.textBrowser.setText(new_sg.get_sname())
        except Exception as e:
            self.error
            print(e)

    def show_fs_window(self):      #展示图象
        given_func = self.textEdit.toPlainText()
        N = self.lineEdit_2.text()
        try:
            def tempf(n):
                return eval(given_func)
            now_sg = st.dt_signal()
            now_sg.set_function(function = tempf, period = eval(N))

            sgname = "fsctf"
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'

            new_sg = st.fs(now_sg,start=-1000,end=1000)
            global pub_T,pub_func
            pub_func = new_sg
            pub_T = eval(N)
            new_sg.save(now_path,"real")
            self.scene.addPixmap(QPixmap(now_path))
            self.f55c.graphicsView.setScene(self.scene)
            self.f55c.show()
            os.remove(now_path)

        except Exception as e:
            self.error
            print(e)

###############################   常见信号   #########################################

class f54_window(QWidget,f54):
    def __init__(self):
        super(f54_window,self).__init__()
        self.setupUi(self)
        self.f541c = f541_window()
        
        self.pushButton_2.clicked.connect(self.show_f541)
        self.pushButton_4.clicked.connect(self.close)
       
    def show_f541(self):
        self.f541c.show()
 







