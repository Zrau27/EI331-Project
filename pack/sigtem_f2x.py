from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene

import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from py.menu import Ui_Form as menu_uf 
from py.func1_1 import Ui_Form as f11                    
from py.func1_2 import Ui_Form as f12
from py.func1_3 import Ui_Form as f13
from py.func1_4 import Ui_Form as f14
from py.func1_5 import Ui_Form as f15
from py.func2_1 import Ui_Form as f21
from py.func2_2 import Ui_Form as f22
from py.func2_3 import Ui_Form as f23
from py.func2_4 import Ui_Form as f24
from py.func2_21 import Ui_Form as f221
from py.func2_22 import Ui_Form as f222
from py.func2_23 import Ui_Form as f223
from py.func2_24 import Ui_Form as f224
from py.func2_25 import Ui_Form as f225
from py.func2_26 import Ui_Form as f226
from py.func2_31 import Ui_Form as f231
from py.func2_32 import Ui_Form as f232
from py.func2_33 import Ui_Form as f233
from py.func2_34 import Ui_Form as f234
from py.func2_35 import Ui_Form as f235
from py.func2_36 import Ui_Form as f236


import sigtem.ct_signals as ctsg  
import sigtem.dt_signals as dtsg
import os


class f24_window(QWidget,f24):
    '''
    显示图像
    '''
    def __init__(self):
        super(f24_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

#########################       离散部分       #####################################

class f231_window(QWidget,f231):
    '''
    离散单位冲激函数
    '''
    def __init__(self):
        super(f231_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f231)
        self.pushButton_7.clicked.connect(self.close)
        
    def show_f231(self):
        k_now = eval(self.lineEdit.text())
        n0_now = eval(self.lineEdit_2.text())
        dtui = dtsg.dt_impulse(t0 = n0_now, k = k_now)
        sgname = dtui.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            dtui.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
        

class f232_window(QWidget,f232):
    def __init__(self):
        super(f232_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f232)
        self.pushButton_7.clicked.connect(self.close)
        
    def show_f232(self):
        dtus = dtsg.dt_unit_step()
        sgname = dtus.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            dtus.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

        

class f233_window(QWidget,f233):
    '''
    离散复指数
    '''
    def __init__(self):
        super(f233_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f233)
        self.pushButton_7.clicked.connect(self.close)
        
    def show_f233(self):
        now_k = eval(self.lineEdit.text())
        now_s = eval(self.lineEdit_2.text())
        now_a = eval(self.lineEdit_4.text())
        now_b = eval(self.lineEdit_3.text())
        dtexp = dtsg.dt_exp(now_k,now_a,now_b,now_s)
        sgname = dtexp.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            dtexp.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f234_window(QWidget,f234):
    '''
    离散sample
    '''
    def __init__(self):
        super(f234_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f234)
        self.pushButton_7.clicked.connect(self.close)
        
    def show_f234(self):
        dtsa = dtsg.dt_sample()
        sgname = dtsa.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            dtsa.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f235_window(QWidget,f235):
    '''
    离散方波
    '''
    def __init__(self):
        super(f235_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_f235)
        self.pushButton_7.clicked.connect(self.close)
        self.scene = QGraphicsScene()
        self.f24_final = f24_window()

    def show_f235(self):
        now_T = eval(self.lineEdit.text())
        now_t1 = eval(self.lineEdit_2.text())
        ctrw = ctsg.ct_rect_period(now_t1,now_T)
        sgname = ctrw.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctrw.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f236_window(QWidget,f236):
    '''
    离散矩形
    '''
    def __init__(self):
        super(f236_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_f226)
        self.pushButton_7.clicked.connect(self.close)
        self.scene = QGraphicsScene()
        self.f24_final = f24_window()

    def show_f226(self):
        now_t1 = eval(self.lineEdit.text())
        now_t2 = eval(self.lineEdit_2.text())
        dtrc = dtsg.dt_rect(now_t2,now_t1)
        sgname = dtrc.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            dtrc.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


##################################    连续部分     ######################################

class f221_window(QWidget,f221):
    '''
    单位冲激函数
    '''
    def __init__(self):
        super(f221_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f221)
        self.pushButton_7.clicked.connect(self.close)
        

    def show_f221(self):
        k_now = eval(self.lineEdit.text())
        t0_now = eval(self.lineEdit_2.text())
        ctui = ctsg.ct_impulse(t0 = t0_now,k=k_now)
        sgname = ctui.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctui.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
        
        
class f222_window(QWidget,f222):
    def __init__(self):
        super(f222_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f222)
        self.pushButton_7.clicked.connect(self.close)
        
    def show_f222(self):
        ctus = ctsg.ct_unit_step()
        sgname = ctus.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctus.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f223_window(QWidget,f223):
    '''
    复指数函数
    '''
    def __init__(self):
        super(f223_window,self).__init__()
        self.setupUi(self)
        self.f24_final = f24_window()
        self.scene = QGraphicsScene()
        self.pushButton_2.clicked.connect(self.show_f223)
        self.pushButton_7.clicked.connect(self.close)
        
    
    def show_f223(self):
        now_k = eval(self.lineEdit.text())
        now_s = eval(self.lineEdit_2.text())
        now_a = eval(self.lineEdit_4.text())
        now_b = eval(self.lineEdit_3.text())
        ctexp = ctsg.ct_exp(now_k,now_a,now_b,now_s)
        sgname = ctexp.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctexp.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
        except Exception as e:
            print(e)



class f224_window(QWidget,f224):
    '''
    sa采样
    '''
    def __init__(self):
        super(f224_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_f224)
        self.pushButton_7.clicked.connect(self.close)
        self.scene = QGraphicsScene()
        self.f24_final = f24_window()

    def show_f224(self):
        ctsa = ctsg.ct_sample()
        sgname = ctsa.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctsa.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f225_window(QWidget,f225):
    '''
    连续周期方波信号
    '''
    def __init__(self):
        super(f225_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_f225)
        self.pushButton_7.clicked.connect(self.close)
        self.scene = QGraphicsScene()
        self.f24_final = f24_window()

    def show_f225(self):
        now_T = eval(self.lineEdit.text())
        now_t1 = eval(self.lineEdit_2.text())
        ctsa = ctsg.ct_rect_period(now_t1,now_T)
        sgname = ctsa.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctsa.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f226_window(QWidget,f226):
    '''
    矩形信号
    '''
    def __init__(self):
        super(f226_window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_f226)
        self.pushButton_7.clicked.connect(self.close)
        self.scene = QGraphicsScene()
        self.f24_final = f24_window()

    def show_f226(self):
        now_t2 = eval(self.lineEdit_2.text())
        ctrc = ctsg.ct_rect(now_t2)
        sgname = ctrc.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            ctrc.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f24_final.graphicsView.setScene(self.scene)
            self.f24_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


########################     主函数     ##########################


class f22_window(QWidget,f22):
    '''
    连续
    '''
    def __init__(self):
        super(f22_window,self).__init__()
        self.setupUi(self)
        self.f221_child = f221_window()
        self.f222_child = f222_window()
        self.f223_child = f223_window()
        self.f224_child = f224_window()
        self.f225_child = f225_window()
        self.f226_child = f226_window()

        self.pushButton.clicked.connect(self.f221_show)
        self.pushButton_2.clicked.connect(self.f222_show)
        self.pushButton_3.clicked.connect(self.f223_show)
        self.pushButton_4.clicked.connect(self.f224_show)
        self.pushButton_5.clicked.connect(self.f225_show)
        self.pushButton_6.clicked.connect(self.f226_show)
        self.pushButton_7.clicked.connect(self.close)

    def f221_show(self):
        self.f221_child.show()
    def f222_show(self):
        self.f222_child.show()
    def f223_show(self):
        self.f223_child.show()
    def f224_show(self):
        self.f224_child.show()
    def f225_show(self):
        self.f225_child.show()
    def f226_show(self):
        self.f226_child.show()


class f23_window(QWidget,f23):
    '''
    离散
    '''
    def __init__(self):
        super(f23_window,self).__init__()
        self.setupUi(self)
        self.f231_child = f231_window()
        self.f232_child = f232_window()
        self.f233_child = f233_window()
        self.f234_child = f234_window()
        self.f235_child = f235_window()
        self.f236_child = f236_window()

        self.pushButton.clicked.connect(self.f231_show)
        self.pushButton_2.clicked.connect(self.f232_show)
        self.pushButton_3.clicked.connect(self.f233_show)
        self.pushButton_4.clicked.connect(self.f234_show)
        self.pushButton_5.clicked.connect(self.f235_show)
        self.pushButton_6.clicked.connect(self.f236_show)
        self.pushButton_7.clicked.connect(self.close)
        
    def f231_show(self):
        self.f231_child.show()
    def f232_show(self):
        self.f232_child.show()
    def f233_show(self):
        self.f233_child.show()
    def f234_show(self):
        self.f234_child.show()
    def f235_show(self):
        self.f235_child.show()
    def f236_show(self):
        self.f236_child.show()


