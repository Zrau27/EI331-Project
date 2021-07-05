from typing import ChainMap
import numpy as np
import sigtem as st
from matplotlib import pyplot as plt

class signal:
    '''
    基础信号类，最基本的类，包内所有其他信号从此继承而来
    '''
    def __init__(self):
        self.t_start = 0 #作图时间下限
        self.t_end = 10 #作图时间上限
        self.x_low = 0 #作图信号上限
        self.x_high = 10 #作图信号下限
        self.set_function(self.__defualt_function) #设定初始信号函数
        self.sname = "NONAME" #初始化信号名字
        self._T = np.nan #信号周期，默认信号周期为无限大即非周期信号
        self._impulse_flag = False #信号是否为冲击
        self._x_array = np.array([0,1]) #初始化数组信号
        self._t_array = np.array([0,1]) #初始化数组信号
        self.__stype = "CT" #设定信号类型为“CT”
        self.__array_flag = False #信号是否为数组形式（有些信号无法显式用函数表示)
        self._spectrum_flag = False #信号是否为频域信号，影响作图横坐标

        
    def __defualt_function(self,t):
        '''
        初始信号函数；
        '''
        return(t**2+2j)
    def __array_function(self,t):
        '''
        数组信号作图（用线性插值补足未查看点）
        '''
        delta_t = self._t_array[1] - self._t_array[0]
        start = self._t_array[0]
        end = self._t_array[-1]
        if t<start or t>=end:
            return 0
        index = int((t-start)//delta_t)
        fraction = ((t-start)%delta_t)/delta_t
        return self._x_array[index]+fraction*(self._x_array[index+1]-self._x_array[index])

    def set_function(self,function,period=np.nan):
        '''
        设定信号函数，参数为任意函数
        '''
        self._T = period
        self.__array_flag = False
        if self.is_periodic():
            def new_function(t):
                return function(t%self._T)
            self.__function = np.vectorize(new_function,otypes=[complex])
        else:
            self.__function = np.vectorize(function,otypes=[complex])
    def set_array(self,t_array='self',x_array='self'):
        '''
        设定数组信号，参数为两数组
        t_array必须为等间隔等时间数组，代表采样时间
        x_array每个时间对应的信号大小
        '''
        if t_array == 'self' and x_array == 'self':
            if self.get_stype() == "CT":
                t_array = np.arange(self.t_start,self.t_end,step=0.01)
                x_array = self.get_x(t_array)
            else:
                t_array = np.arange(self.t_start,self.t_end,step=1)
                x_array = self.get_x(t_array)
        else:
            t_array = np.array(t_array)
            x_array = np.array(x_array)
        if t_array.shape != x_array.shape:
            raise RuntimeError('x and t array has different shape!')
        self._t_array = t_array.copy()
        self._x_array = x_array.copy()
        self.set_function(self.__array_function)
        self.__array_flag = True
        self.set_t(t_array[0],t_array[-1])
        self.set_x(np.min(x_array)-0.2,np.max(x_array)+0.5)
        self._T = np.nan
    def set_stype(self,stype):
        '''
        设定信号的类型；
        作图使用这个函数可以改变某一个信号的显示方式；
        stype参数可选字符串 "CT","DT"，其他报错
        '''
        if stype in ["CT","DT"]:
            self.__stype = stype
        else :
            raise RuntimeError("Unknown stype,try 'CT' or 'DT'!")
    def set_t(self,t_start,t_end):
        '''
        设定显示窗口的时间范围
        '''
        self.t_start = t_start
        self.t_end = t_end
    def set_x(self,x_low,x_high):
        '''
        设定显示窗口的大小范围
        '''
        self.x_low = x_low
        self.x_high = x_high
    def set_loc(self,t1,t2,x1,x2):
        self.set_t(t1,t2)
        self.set_x(x1,x2)
    def set_sname(self,sname):
        '''
        为你喜欢的信号设定一个响亮的名字吧！名字可显示在作图中
        '''
        self.sname = sname

    def get_x(self,t):
        '''
        输入时间t得到对应的x值，t可以为一个np数组
        '''
        return(self.__function(t))

    def get_x_form(self,t,form='real'):
        '''
        输入时间t，得到x的不同部分的信号；
        form参量可选'real','imag','angle','abs'，每个部分如字面意思，不再赘述
        '''
        if form == "real":  
            return(np.real(self.__function(t)))
        elif form == "imag":
            return(np.imag(self.__function(t)))
        elif form == "abs":
            return(np.abs(self.__function(t)))
        elif form == "angle":
            return(np.angle(self.__function(t)))
        else:
            raise RuntimeError("Unknown form type,try 'real','imag','angle','abs'!")

    def get_x_real(self,t):
        '''
        获得实数部分
        '''
        return(self.get_x_form(t,form='real'))
    def get_x_imag(self,t):
        '''
        获得虚数部分
        '''
        return(self.get_x_form(t,form='imag'))
    def get_x_abs(self,t):
        '''
        获得模
        '''
        return(self.get_x_form(t,form='abs'))
    def get_x_angle(self,t):
        '''
        获得角度
        '''
        return(self.get_x_form(t,form='angle'))

    def get_fs(self,t1=-4,t2=6):
        '''
        获得信号的傅立叶级数信号
        参数t1，t2描述傅立叶级数信号范围
        '''
        return st.fs(self,t1,t2)

    def get_ft(self,t1=-5,t2=5):
        '''
        获得信号的傅立叶变换信号
        参数t1，t2描述傅立叶级数信号范围
        '''
        return st.ft(self,t1,t2)

    def get_stype(self):
        '''
        获得信号的类型
        '''
        return(self.__stype)
    def get_sname(self):
        '''
        获得信号的名字
        '''
        return(self.sname)
    def get_period(self):
        '''
        获得信号的周期
        '''
        return(self._T)

    def is_impulse(self):
        '''
        判断信号是否为一个冲击信号
        '''
        return (self._impulse_flag)
    def is_array(self):
        '''
        判断信号是否为一个数组信号
        '''
        return (self.__array_flag)
    def is_periodic(self):
        '''
        判断一个信号是否为周期函数
        '''
        return (not np.isnan(self._T))
    def is_spectrum(self):
        '''
        判断一个信号是否为频域信号
        '''
        return self._spectrum_flag

    def draw(self,form="real"):
        '''
        画出信号的各个部分;
        参数form可选 'real','imag','angle','abs'
        '''
        if self.get_stype() == "CT":
            t = np.arange(self.t_start,self.t_end,step=0.01)
            x = self.get_x_form(t,form = form)
            plt.grid()
            plt.title("CT Signal {} ({} part)".format(self.sname,form))
            if form == "angle":
                plt.ylim(-4,4)
            else :
                plt.ylim((self.x_low,self.x_high))
            if self.is_spectrum():
                plt.xlabel(chr(969))
                plt.ylabel("x {} part".format(form))
            else:
                plt.xlabel("t") 
                plt.ylabel("X {} part".format(form))
            plt.plot(t,x)
        else:
            t = np.arange(self.t_start,self.t_end,step=1)
            x = self.get_x_form(t,form = form)
            plt.grid()
            plt.title("DT Signal {} ({} part)".format(self.sname,form))
            if form == "angle":
                plt.ylim(-4,4)
            else :
                plt.ylim((self.x_low,self.x_high))
            plt.xticks(t)
            if self.is_spectrum():
                plt.xlabel(chr(969))
                plt.ylabel("x")
            else:
                plt.xlabel("t") 
                plt.ylabel("X")
            plt.stem(t,x)

    def draw_all(self):
        '''
        将信号的每个部分作为子图画在一张图中
        '''
        if self.get_stype() == "CT":
            t = np.arange(self.t_start,self.t_end,step=0.01)
            plt.subplot(221)
            plt.grid()
            x = self.get_x_real(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("real_part") 
            plt.plot(t,x)

            plt.subplot(222)
            plt.grid()
            x = self.get_x_imag(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("imag_part") 
            plt.plot(t,x)

            plt.subplot(223)
            plt.grid()
            x = self.get_x_abs(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("abs_part") 
            plt.plot(t,x)

            plt.subplot(224)
            plt.grid()
            x = self.get_x_angle(t)
            plt.ylim(-4,4)
            plt.title("angle_part")
            plt.plot(t,x)

            plt.tight_layout()
        else:
            t = np.arange(self.t_start,self.t_end,step=1)
            plt.subplot(221)
            plt.grid()
            x = self.get_x_real(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("real_part") 
            plt.stem(t,x)

            plt.subplot(222)
            plt.grid()
            x = self.get_x_imag(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("imag_part") 
            plt.stem(t,x)

            plt.subplot(223)
            plt.grid()
            x = self.get_x_abs(t)
            plt.ylim((self.x_low,self.x_high))
            plt.title("abs_part") 
            plt.stem(t,x)

            plt.subplot(224)
            plt.grid()
            x = self.get_x_angle(t)
            plt.ylim(-4,4)
            plt.title("angle_part")
            plt.stem(t,x)

            plt.tight_layout()

    
    def show(self,form='real'):
        '''
        展示信号的某个部分，默认展示实数部分
        '''
        plt.figure()
        self.draw(form=form)
        plt.show()

    def show_all(self):
        '''
        将信号的每个部分作为子图画在一张图中，并进行展示
        '''
        plt.figure()
        self.draw_all()
        plt.show()

    def show_real(self):
        self.show('real')
    def show_imag(self):
        self.show('imag')
    def show_abs(self):
        self.show('abs')
    def show_angle(self):
        self.show('angle')

    def save(self,path,form):
        '''
        将信号的某个部分画出后保存，无默认部分
        path参数表示保存路径，可选；
        '''
        plt.figure()
        self.draw(form=form)
        plt.savefig(path)
    def save_all(self,path):
        '''
        将信号的每个部分作为子图画在一张图中，并进行保存
        '''
        plt.figure()
        self.draw_all()
        plt.savefig(path)