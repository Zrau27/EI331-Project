from re import I
from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene
import numpy as np     #补充库

import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy.core.records import array

from py.menu import Ui_Form as menu_uf 
from py.func1_1 import Ui_Form as f11                    
from py.func1_2 import Ui_Form as f12
from py.func1_3 import Ui_Form as f13
from py.func1_4 import Ui_Form as f14
from py.func1_5 import Ui_Form as f15

import sigtem as st

import sigtem.ct_signals as ctsg  
import sigtem.dt_signals as dtsg
import os


class f14_window(QWidget,f14):
    '''
    图像
    '''
    def __init__(self):
        super(f14_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class f15_window(QWidget,f15):
    '''
    用于报错
    '''
    def __init__(self):
        super(f15_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

##############################   FUNC1   ##########################################
 
class f12_window_1(QWidget,f12):
    '''
    离散
    '''
    def __init__(self):
        super(f12_window_1,self).__init__()
        self.setupUi(self)
        self.error = f15_window()
        self.f14c = f14_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f14)
        self.pushButton.clicked.connect(self.close)
 
    def show_error(self):
        self.error.show()

    def show_f14(self):
        given_name = self.lineEdit.text()
        given_tmin = self.lineEdit_2.text()
        given_tmax = self.lineEdit_3.text()
        given_xmin = self.lineEdit_4.text()
        given_xmax = self.lineEdit_5.text()
        given_code = self.textEdit.toPlainText()


        if given_name == "" : sgname = "Unnamed dt_signal"
        else: sgname = given_name

        if given_tmin == "": tmin = -5
        else: tmin = eval(given_tmin)

        if given_tmax == "": tmax = 5
        else:tmax = eval(given_tmax) +1    #加1，因为实际区间为[tmin,tmax),对x同理

        if given_xmin == "": xmin = -5
        else: xmin = eval(given_xmin)

        if given_xmax == "": xmax = 5
        else: xmax = eval(given_xmax) +1 

        if given_code == "":
            self.show_error()
        else:
            def tempf(t):
                return eval(given_code)
            a = st.dt_signal()
            a.set_function(function=tempf)
            a.set_sname(sgname)
            a.set_t(tmin,tmax)
            a.set_x(xmin,xmax)
            try:
                now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
                a.save(now_path,'real')
                self.scene.addPixmap(QPixmap(now_path))
                self.f14c.graphicsView.setScene(self.scene)
                self.f14c.show()
                os.remove(now_path)
                
            except Exception as e:
                print(e)
                self.show_error()
            
            
      
        


class f12_window_2(QWidget,f12):
    '''
    连续
    '''
    def __init__(self):
        super(f12_window_2,self).__init__()
        self.setupUi(self)
        self.error = f15_window()
        self.f14c = f14_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f14)
        self.pushButton.clicked.connect(self.close)
 
    def show_error(self):
        self.error.show()

    def show_f14(self):
        given_name = self.lineEdit.text()
        given_tmin = self.lineEdit_2.text()
        given_tmax = self.lineEdit_3.text()
        given_xmin = self.lineEdit_4.text()
        given_xmax = self.lineEdit_5.text()
        given_code = self.textEdit.toPlainText()


        if given_name == "" : sgname = "Unnamed ct_signal"
        else: sgname = given_name

        if given_tmin == "": tmin = -5
        else: tmin = eval(given_tmin)

        if given_tmax == "": tmax = 5
        else:tmax = eval(given_tmax)

        if given_xmin == "": xmin = -5
        else: xmin = eval(given_xmin)

        if given_xmax == "": xmax = 5
        else: xmax = eval(given_xmax)  

        if given_code == "":
            self.show_error()
        else:
            try:
                def tempf(t):
                    return eval(given_code)
                a = st.ct_signal()
                a.set_function(function=tempf)
                a.set_sname(sgname)
                a.set_t(tmin,tmax)
                a.set_x(xmin,xmax)
                now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
                a.save(now_path,'real')
                self.scene.addPixmap(QPixmap(now_path))
                self.f14c.graphicsView.setScene(self.scene)
                self.f14c.show()
                os.remove(now_path)
                
            except Exception as e:
                print(e)
                self.show_error()
        


class f13_window(QWidget,f13):
    def __init__(self):
        super(f13_window,self).__init__()
        self.setupUi(self)
        self.error = f15_window()
        self.f14c = f14_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f14)
        self.pushButton.clicked.connect(self.close)
        self.textEdit.setText("[]")
        self.textEdit_2.setText("[]")
 
    def show_error(self):
        self.error.show()

    def show_f14(self):
        given_name = self.lineEdit.text()
        if given_name == "" : sgname = "Unnamed ct_signal"
        else: sgname = given_name

        given_t = self.textEdit.toPlainText()
        given_x = self.textEdit_2.toPlainText()

        try:
            a = st.ct_signal()
            a.set_array(eval(given_t),eval(given_x))
            a.set_sname(sgname)
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            a.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f14c.graphicsView.setScene(self.scene)
            self.f14c.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
            self.show_error()


        
        
     
        



        





