from re import I
from PyQt5 import QtWidgets
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt5.QtWidgets import QGraphicsScene

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy.lib.type_check import real


from py.func3_1 import Ui_Form as f31
from py.func3_3 import Ui_Form as f33
from py.func3_4 import Ui_Form as f34
from py.func3_3_11 import Ui_Form as f3311
from py.func3_3_12 import Ui_Form as f3312
from py.func3_3_13 import Ui_Form as f3313
from py.func3_3_14 import Ui_Form as f3314
from py.func3_3_15 import Ui_Form as f3315
from py.func3_3_16 import Ui_Form as f3316
from py.func3_3_22 import Ui_Form as f3322
from py.func3_3_23 import Ui_Form as f3323
from py.func3_3_24 import Ui_Form as f3324
from py.func3_3_25 import Ui_Form as f3325
from py.func3_3_26 import Ui_Form as f3326
from py.func3_3_33 import Ui_Form as f3333
from py.func3_3_34 import Ui_Form as f3334
from py.func3_3_35 import Ui_Form as f3335
from py.func3_3_36 import Ui_Form as f3336
from py.func3_3_44 import Ui_Form as f3344
from py.func3_3_45 import Ui_Form as f3345
from py.func3_3_46 import Ui_Form as f3346
from py.func3_3_55 import Ui_Form as f3355
from py.func3_3_56 import Ui_Form as f3356
from py.func3_3_66 import Ui_Form as f3366
from py.func3_4_11 import Ui_Form as f3411
from py.func3_4_12 import Ui_Form as f3412
from py.func3_4_13 import Ui_Form as f3413
from py.func3_4_14 import Ui_Form as f3414
from py.func3_4_15 import Ui_Form as f3415
from py.func3_4_16 import Ui_Form as f3416
from py.func3_4_22 import Ui_Form as f3422
from py.func3_4_23 import Ui_Form as f3423
from py.func3_4_24 import Ui_Form as f3424
from py.func3_4_25 import Ui_Form as f3425
from py.func3_4_26 import Ui_Form as f3426
from py.func3_4_33 import Ui_Form as f3433
from py.func3_4_34 import Ui_Form as f3434
from py.func3_4_35 import Ui_Form as f3435
from py.func3_4_36 import Ui_Form as f3436
from py.func3_4_44 import Ui_Form as f3444
from py.func3_4_45 import Ui_Form as f3445
from py.func3_4_46 import Ui_Form as f3446
from py.func3_4_55 import Ui_Form as f3455
from py.func3_4_56 import Ui_Form as f3456
from py.func3_4_66 import Ui_Form as f3466
from py.func3_5 import Ui_Form as f35

from py.func1_5 import Ui_Form as f15

import sigtem as st
import sigtem.ct_signals as ctsg  
import sigtem.dt_signals as dtsg
import sigtem.cov_ct as cc
import sigtem.cov_dt as cd
import os


class f35_window(QWidget,f35):
    '''
    展示图像窗口
    '''
    def __init__(self):
        super(f35_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class f15_window(QWidget,f15):
    '''
    报错
    '''
    def __init__(self):
        super(f15_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

########################################    连续    #########################################

class f3311_window(QWidget,f3311):
    def __init__(self):
        super(f3311_window,self).__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.close)


class f3312_window(QWidget,f3312):
    def __init__(self):
        super(f3312_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        f1 = ctsg.ct_impulse(t01,k1)
        f2 = ctsg.ct_unit_step()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3313_window(QWidget,f3313):
    def __init__(self):
        super(f3313_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        k = eval(self.lineEdit_23.text())
        s = eval(self.lineEdit_24.text())
        a = eval(self.lineEdit_25.text())
        b = eval(self.lineEdit_26.text())
        f1 = ctsg.ct_impulse(t01,k1)
        f2 = ctsg.ct_exp(k,a,b,s)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3314_window(QWidget,f3314):
    def __init__(self):
        super(f3314_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
     
        f1 = ctsg.ct_impulse(t01,k1)
        f2 = ctsg.ct_sample()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3315_window(QWidget,f3315):
    def __init__(self):
        super(f3315_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = ctsg.ct_impulse(t01,k1)
        f2 = ctsg.ct_rect_period(T0,T)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3316_window(QWidget,f3316):
    def __init__(self):
        super(f3316_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        T1 = eval(self.lineEdit_9.text())
        f1 = ctsg.ct_impulse(t01,k1)
        f2 = ctsg.ct_rect(T1)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3322_window(QWidget,f3322):
    def __init__(self):
        super(f3322_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = ctsg.ct_unit_step()
        f2 = ctsg.ct_unit_step()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3323_window(QWidget,f3323):
    def __init__(self):
        super(f3323_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k = eval(self.lineEdit_23.text())
        s = eval(self.lineEdit_24.text())
        a = eval(self.lineEdit_25.text())
        b = eval(self.lineEdit_26.text())
        f1 = ctsg.ct_unit_step()
        f2 = ctsg.ct_exp(k,a,b,s)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3324_window(QWidget,f3324):
    def __init__(self):
        super(f3324_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = ctsg.ct_unit_step()
        f2 = ctsg.ct_sample()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3325_window(QWidget,f3325):
    def __init__(self):
        super(f3325_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)

    def show_f35(self):
        T0 = eval(self.lineEdit_7.text())
        T = eval(self.lineEdit_8.text())
        f1 = ctsg.ct_unit_step()
        f2 = ctsg.ct_rect_period(T0,T)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3326_window(QWidget,f3326):
    def __init__(self):
        super(f3326_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T1 = eval(self.lineEdit_10.text())
        f1 = ctsg.ct_unit_step()
        f2 = ctsg.ct_rect(T1)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3333_window(QWidget,f3333):
    def __init__(self):
        super(f3333_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        k2 = eval(self.lineEdit_23.text())
        s2 = eval(self.lineEdit_24.text())
        a2 = eval(self.lineEdit_25.text())
        b2 = eval(self.lineEdit_26.text())
        f1 = ctsg.ct_exp(k1,a1,b1,s1)
        f2 = ctsg.ct_exp(k2,a2,b2,s2)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3334_window(QWidget,f3334):
    def __init__(self):
        super(f3334_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        f1 = ctsg.ct_exp(k1,a1,b1,s1)
        f2 = ctsg.ct_sample()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
    
class f3335_window(QWidget,f3335):
    def __init__(self):
        super(f3335_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = ctsg.ct_exp(k1,a1,b1,s1)
        f2 = ctsg.ct_rect_period(T0,T)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3336_window(QWidget,f3336):
    def __init__(self):
        super(f3336_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        T0 = eval(self.lineEdit_9.text())
        f1 = ctsg.ct_exp(k1,a1,b1,s1)
        f2 = ctsg.ct_rect(T0)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3344_window(QWidget,f3344):
    def __init__(self):
        super(f3344_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = ctsg.ct_sample()
        f2 = ctsg.ct_sample()
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3345_window(QWidget,f3345):
    def __init__(self):
        super(f3345_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = st.ct_sample()
        f2 = st.ct_rect_period(T0,T)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3346_window(QWidget,f3346):
    def __init__(self):
        super(f3346_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T1 = eval(self.lineEdit_9.text())
        f1 = ctsg.ct_sample()
        f2 = ctsg.ct_rect(T1)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3355_window(QWidget,f3355):
    def __init__(self):
        super(f3355_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T01 = eval(self.lineEdit_7.text())
        T1 = eval(self.lineEdit_8.text())
        T02 = eval(self.lineEdit_6.text())
        T2 = eval(self.lineEdit_5.text())
        f1 = ctsg.ct_rect_period(T01,T1)
        f2 = ctsg.ct_rect_period(T02,T2)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3356_window(QWidget,f3356):
    def __init__(self):
        super(f3356_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_7.text())
        T = eval(self.lineEdit_8.text())
        T1 = eval(self.lineEdit_9.text())
        f1 = ctsg.ct_rect_period(T0,T)
        f2 = ctsg.ct_rect(T1)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3366_window(QWidget,f3366):
    def __init__(self):
        super(f3366_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_11.text())
        T1 = eval(self.lineEdit_10.text())
        f1 = ctsg.ct_rect(T0)
        f2 = ctsg.ct_rect(T1)
        f3 = cc.conv_ct(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

######################################  离散  #######################################

class f3411_window(QWidget,f3411):
    def __init__(self):
        super(f3411_window,self).__init__()
        self.setupUi(self)

class f3412_window(QWidget,f3412):
    def __init__(self):
        super(f3412_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        f1 = dtsg.dt_impulse(t01,k1)
        f2 = dtsg.dt_unit_step()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3413_window(QWidget,f3413):
    def __init__(self):
        super(f3413_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        k = eval(self.lineEdit_23.text())
        s = eval(self.lineEdit_24.text())
        a = eval(self.lineEdit_25.text())
        b = eval(self.lineEdit_26.text())
        f1 = dtsg.dt_impulse(t01,k1)
        f2 = dtsg.dt_exp(k,a,b,s)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3414_window(QWidget,f3414):
    def __init__(self):
        super(f3414_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
     
        f1 = dtsg.dt_impulse(t01,k1)
        f2 = dtsg.dt_sample()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3415_window(QWidget,f3415):
    def __init__(self):
        super(f3415_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = dtsg.dt_impulse(t01,k1)
        f2 = dtsg.dt_rect_wave(T0,T)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3416_window(QWidget,f3416):
    def __init__(self):
        super(f3416_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit.text())
        t01 = eval(self.lineEdit_2.text())
        T1 = eval(self.lineEdit_10.text())
        
        f1 = dtsg.dt_impulse(t01,k1)
        f2 = dtsg.dt_rect(T1)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3422_window(QWidget,f3422):
    def __init__(self):
        super(f3422_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = dtsg.dt_unit_step()
        f2 = dtsg.dt_unit_step()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3423_window(QWidget,f3423):
    def __init__(self):
        super(f3423_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k = eval(self.lineEdit_23.text())
        s = eval(self.lineEdit_24.text())
        a = eval(self.lineEdit_25.text())
        b = eval(self.lineEdit_26.text())
        f1 = dtsg.dt_unit_step()
        f2 = dtsg.dt_exp(k,a,b,s)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3424_window(QWidget,f3424):
    def __init__(self):
        super(f3424_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = dtsg.dt_unit_step()
        f2 = dtsg.dt_sample()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3425_window(QWidget,f3425):
    def __init__(self):
        super(f3425_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_7.text())
        T = eval(self.lineEdit_8.text())
        f1 = dtsg.dt_unit_step()
        f2 = dtsg.dt_rect_wave(T0,T)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3426_window(QWidget,f3426):
    def __init__(self):
        super(f3426_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T1 = eval(self.lineEdit_10.text())
        f1 = dtsg.dt_unit_step()
        f2 = dtsg.dt_rect(T1)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3433_window(QWidget,f3433):
    def __init__(self):
        super(f3433_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        k2 = eval(self.lineEdit_23.text())
        s2 = eval(self.lineEdit_24.text())
        a2 = eval(self.lineEdit_25.text())
        b2 = eval(self.lineEdit_26.text())
        f1 = dtsg.dt_exp(k1,a1,b1,s1)
        f2 = dtsg.dt_exp(k2,a2,b2,s2)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3434_window(QWidget,f3434):
    def __init__(self):
        super(f3434_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        f1 = dtsg.dt_exp(k1,a1,b1,s1)
        f2 = dtsg.dt_sample()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)
    
class f3435_window(QWidget,f3435):
    def __init__(self):
        super(f3435_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = dtsg.dt_exp(k1,a1,b1,s1)
        f2 = dtsg.dt_rect_wave(T0,T)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3436_window(QWidget,f3436):
    def __init__(self):
        super(f3436_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        k1 = eval(self.lineEdit_27.text())
        s1 = eval(self.lineEdit_28.text())
        a1 = eval(self.lineEdit_29.text())
        b1 = eval(self.lineEdit_30.text())
        T0 = eval(self.lineEdit_10.text())
        f1 = dtsg.dt_exp(k1,a1,b1,s1)
        f2 = dtsg.dt_rect(T0)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3444_window(QWidget,f3444):
    def __init__(self):
        super(f3444_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        f1 = dtsg.dt_sample()
        f2 = dtsg.dt_sample()
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3445_window(QWidget,f3445):
    def __init__(self):
        super(f3445_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_6.text())
        T = eval(self.lineEdit_5.text())
        f1 = dtsg.dt_sample()
        f2 = dtsg.dt_rect_wave(T0,T)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)


class f3446_window(QWidget,f3446):
    def __init__(self):
        super(f3446_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T1 = eval(self.lineEdit_10.text())
        f1 = dtsg.dt_sample()
        f2 = dtsg.dt_rect(T1)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3455_window(QWidget,f3455):
    def __init__(self):
        super(f3455_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T01 = eval(self.lineEdit_7.text())
        T1 = eval(self.lineEdit_8.text())
        T02 = eval(self.lineEdit_6.text())
        T2 = eval(self.lineEdit_5.text())
        f1 = dtsg.dt_rect_wave(T01,T1)
        f2 = dtsg.dt_rect_wave(T02,T2)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3456_window(QWidget,f3456):
    def __init__(self):
        super(f3456_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T0 = eval(self.lineEdit_7.text())
        T = eval(self.lineEdit_8.text())
        T1 = eval(self.lineEdit_10.text())
        f1 = dtsg.dt_rect_wave(T0,T)
        f2 = dtsg.dt_rect(T1)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)

class f3466_window(QWidget,f3466):
    def __init__(self):
        super(f3466_window,self).__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.f35_final = f35_window()
        self.pushButton_2.clicked.connect(self.show_f35)
        self.pushButton_7.clicked.connect(self.close)
    def show_f35(self):
        T1_1 = eval(self.lineEdit_11.text())
        T1_2 = eval(self.lineEdit_10.text())
        f1 = dtsg.dt_rect(T1_1)
        f2 = dtsg.dt_rect(T1_2)
        f3 = cd.conv_dt(f1,f2)
        sgname = f3.get_sname()
        try:
            now_path = os.getcwd() + r'{}'.format(sgname)+'.png'
            f3.save(now_path,'real')
            self.scene.addPixmap(QPixmap(now_path))
            self.f35_final.graphicsView.setScene(self.scene)
            self.f35_final.show()
            os.remove(now_path)
            
        except Exception as e:
            print(e)



########################################  主函数  #########################################
choice_map = {
    "单位冲激信号":1,
    "单位阶跃信号":2,
    "复指数信号":3,
    "Sa函数":4,
    "周期方波信号":5,
    "矩形波信号":6
}


def show_choice(c1,c2):
    '''
    读取文字选项
    '''
    n1 = choice_map[c1]
    n2 = choice_map[c2]

    if n1 <= n2:
        choice = n1*10 + n2
    else:
        choice = n2*10 + n1
    return choice


class f33_window(QWidget,f33):
    '''
    连续
    '''
    def __init__(self):
        super(f33_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.pushButton_2.clicked.connect(self.show_f33bc)
        self.pushButton.clicked.connect(self.close)
        self.f3311c = f3311_window()
        self.f3312c = f3312_window()
        self.f3313c = f3313_window()
        self.f3314c = f3314_window()
        self.f3315c = f3315_window()
        self.f3316c = f3316_window()
        self.f3322c = f3322_window()
        self.f3323c = f3323_window()
        self.f3324c = f3324_window()
        self.f3325c = f3325_window()
        self.f3326c = f3326_window()
        self.f3333c = f3333_window()
        self.f3334c = f3334_window()
        self.f3335c = f3335_window()
        self.f3336c = f3336_window()
        self.f3344c = f3344_window()
        self.f3345c = f3345_window()
        self.f3346c = f3346_window()
        self.f3355c = f3355_window()
        self.f3356c = f3356_window()
        self.f3366c = f3366_window()

    def show_f33bc(self):
        choice1 = self.comboBox.currentText()
        choice2 = self.comboBox_2.currentText()
        #print(choice1,choice2)
        choice = show_choice(choice1,choice2)
        c = choice
        #print(c)
        if c == 11:
            self.f15c.show()
        elif c == 12:
            self.f3312c.show()
        elif c==13:
            self.f3313c.show()
        elif c==14:
            self.f3314c.show()
        elif c==15:
            self.f3315c.show()
        elif c==16:
            self.f3316c.show()
        elif c==22:
            self.f3322c.show()
        elif c==23:
            self.f3323c.show()
        elif c==24:
            self.f3324c.show()
        elif c==25:
            self.f3325c.show()
        elif c==26:
            self.f3326c.show()
        elif c==33:
            self.f3333c.show()
        elif c==34:
            self.f3334c.show()
        elif c==35:
            self.f3335c.show()
        elif c==36:
            self.f3336c.show()
        elif c==44:
            self.f3344c.show()
        elif c==45:
            self.f3345c.show()
        elif c==46:
            self.f3346c.show()
        elif c==55:
            self.f3355c.show()
        elif c==56:
            self.f3356c.show()
        elif c==66:
            self.f3366c.show()
        else:
            print("someting wrong with show_f33bc")


class f34_window(QWidget,f34):
    '''
    离散
    '''
    def __init__(self):
        super(f34_window,self).__init__()
        self.setupUi(self)
        self.f15c = f15_window()
        self.pushButton_2.clicked.connect(self.show_f34bc)
        self.pushButton.clicked.connect(self.close)
        self.f3411c = f3411_window()
        self.f3412c = f3412_window()
        self.f3413c = f3413_window()
        self.f3414c = f3414_window()
        self.f3415c = f3415_window()
        self.f3416c = f3416_window()
        self.f3422c = f3422_window()
        self.f3423c = f3423_window()
        self.f3424c = f3424_window()
        self.f3425c = f3425_window()
        self.f3426c = f3426_window()
        self.f3433c = f3433_window()
        self.f3434c = f3434_window()
        self.f3435c = f3435_window()
        self.f3436c = f3436_window()
        self.f3444c = f3444_window()
        self.f3445c = f3445_window()
        self.f3446c = f3446_window()
        self.f3455c = f3455_window()
        self.f3456c = f3456_window()
        self.f3466c = f3466_window()

    def show_f34bc(self):
        choice1 = self.comboBox.currentText()
        choice2 = self.comboBox_2.currentText()
        choice = show_choice(choice1,choice2)
        c = choice
        if c == 11:
            self.f15c.show()
        elif c == 12:
            self.f3412c.show()
        elif c==13:
            self.f3413c.show()
        elif c==14:
            self.f3414c.show()
        elif c==15:
            self.f3415c.show()
        elif c==16:
            self.f3416c.show()
        elif c==22:
            self.f3422c.show()
        elif c==23:
            self.f3423c.show()
        elif c==24:
            self.f3424c.show()
        elif c==25:
            self.f3425c.show()
        elif c==26:
            self.f3426c.show()
        elif c==33:
            self.f3433c.show()
        elif c==34:
            self.f3434c.show()
        elif c==35:
            self.f3435c.show()
        elif c==36:
            self.f3436c.show()
        elif c==44:
            self.f3444c.show()
        elif c==45:
            self.f3445c.show()
        elif c==46:
            self.f3446c.show()
        elif c==55:
            self.f3455c.show()
        elif c==56:
            self.f3456c.show()
        elif c==66:
            self.f3466c.show()
        else:
            print("someting wrong with show_f34bc")



