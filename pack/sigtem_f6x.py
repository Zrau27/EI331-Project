from sys import path
from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene

import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from py.func6_2 import Ui_Form as f62
from py.func6_3 import Ui_Form as f63
from py.func6_4 import Ui_Form as f64
from py.func6_5 import Ui_Form as f65
from py.func6_6 import Ui_Form as f66
from py.func6_7 import Ui_Form as f67
from py.func6_8 import Ui_Form as f68

import sigtem as st
import sigtem.ct_signals as ctsg
import sigtem.dt_signals as dtsg
import numpy as np
import os

pub_sg = st.ct_signal()        #全局变量，用于传参
pub_sg_sa = st.ct_signal()    #储存采样后频域
pub_T = 1                    #储存采样时T
pub_org = st.ct_signal()     #原时域信号
sa_time = np.array([1,2,3])
sa_xray = np.array([1,2,3])



class f62_window(QWidget,f62):
    def __init__(self):
        super(f62_window,self).__init__()
        self.setupUi(self)
        self.f63c = f63_window()
        self.pushButton.clicked.connect(self.show_f63c)
        self.pushButton_7.clicked.connect(self.close)
    
    def show_f63c(self):
        self.f63c.show()


class f63_window(QWidget,f63):
    '''
    采样
    '''
    def __init__(self):
        super(f63_window,self).__init__()
        self.setupUi(self)
        self.f64c = f64_window()
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f64c)
        self.pushButton_7.clicked.connect(self.close)

    def show_f64c(self):
        ws = self.lineEdit.text()
        given_code = self.textEdit.toPlainText()
        try:
            def s(t):
                return eval(given_code)
            org_sg = st.ct_signal()
            org_sg.set_function(function=s)
            sa_sg,sa_t,sa_x = st.sample_t(org_sg,1/eval(ws))

            global sa_xray,sa_time,pub_T,pub_org       #将sa_x,sa_t映射到全局变量，便于后续程序调用
            pub_T = 1/eval(ws)
            sa_xray = sa_x
            sa_time = sa_t
            pub_org = org_sg

            ft_sg = st.ft(org_sg)
            sa_ft_sg = st.sample_s(ft_sg,1/eval(ws))
            global pub_sg_sa
            pub_sg_sa = sa_ft_sg

            path1 = os.getcwd() + r'{}'.format('sg_t')+'.png'
            path2 = os.getcwd() + r'{}'.format('sg_s')+'.png'

            sa_sg.save(path1,'real')
            sa_ft_sg.save(path2,'real')
            global pub_sg
            pub_sg = sa_ft_sg

            self.scene1.addPixmap(QPixmap(path1))
            self.f64c.graphicsView.setScene(self.scene1)
            self.scene2.addPixmap(QPixmap(path2))
            self.f64c.graphicsView_2.setScene(self.scene2)
            self.f64c.show()
            os.remove(path1)
            os.remove(path2)
        
        except Exception as e:
            print(e)


class f64_window(QWidget,f64):
    '''
    展示采样结果
    '''
    def __init__(self):
        super(f64_window,self).__init__()
        self.setupUi(self)
        self.f65c = f65_window()
        self.pushButton.clicked.connect(self.show_f65c)
        self.pushButton_7.clicked.connect(self.close)
    
    def show_f65c(self):
        self.f65c.show()


class f65_window(QWidget,f65):
    '''
    滤波
    '''
    def __init__(self):
        super(f65_window,self).__init__()
        self.setupUi(self)
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f66c)
        self.pushButton_7.clicked.connect(self.close)
        self.f66c = f66_window()

    
    def show_f66c(self):
        #print('1')
        wc = self.lineEdit_2.text()  #截止频率
        k = self.lineEdit.text()    #增益
        try:
            global pub_sg
            lpf_sg = st.resample_t(pub_org,1/eval(wc),k = eval(k))
            lpf_ft_sg =  st.low_pass_filter( pub_sg,eval(wc),k = eval(k)  )
            path1 = os.getcwd() + r'{}'.format('lpf_s')+'.png'
            path2 = os.getcwd()+r'{}'.format('lps_t')+'.png'
            lpf_ft_sg.save(path1,'real')
            lpf_sg.save(path2,'real')
            self.scene1.addPixmap(QPixmap(path1))
            self.scene2.addPixmap(QPixmap(path2))
            self.f66c.graphicsView_2.setScene(self.scene1)
            self.f66c.graphicsView.setScene(self.scene2)
            self.f66c.show()
            os.remove(path1)
            os.remove(path2)
        
        except Exception as e:
            print(e)



class f66_window(QWidget,f66):
    '''
    滤波图像结果展示
    '''
    def __init__(self):
        super(f66_window,self).__init__()
        self.setupUi(self)
        self.f67c = f67_window()
        self.pushButton.clicked.connect(self.show_f67c)
        self.pushButton_7.clicked.connect(self.close)

    def show_f67c(self):
        self.f67c.show()


class f67_window(QWidget,f67):
    '''
    线性插值
    '''
    def __init__(self):
        super(f67_window,self).__init__()
        self.setupUi(self)
        self.f68c = f68_window()
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f68c)
        self.pushButton_7.clicked.connect(self.close)
    
    def show_f68c(self):
    
        try:
            global sa_time,sa_xray,pub_sg_sa,pub_T
            final_sg_t =  st.linear_interpolation(sa_time,sa_xray)
            final_sg_s =  st.resample_s(pub_sg_sa,pub_T)
            path1 = os.getcwd() + r'{}'.format('ip_t')+'.png'
            path2 = os.getcwd() + r'{}'.format('ip_s')+'.png'
            final_sg_t.save(path1,'real')
            final_sg_s.save(path2,'real')
            self.scene1.addPixmap(QPixmap(path1))
            self.scene2.addPixmap(QPixmap(path2))
            self.f68c.graphicsView.setScene(self.scene1)
            self.f68c.graphicsView_2.setScene(self.scene2)
            self.f68c.show()
            os.remove(path1)
        
        except Exception as e:
            print(e)


class f68_window(QWidget,f68):
    def __init__(self):
        super(f68_window,self).__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.close)

