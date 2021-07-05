import numpy as np
from matplotlib import pyplot as plt
import sigtem as st

#dt_signals

class dt_signal(st.signal):
    '''
    离散信号类，无法改变类型
    '''
    def __init__(self):
        super().__init__()
        self.set_stype('DT')
        self.set_stype = self.__set_stype
    def __set_stype(self,stype):
        raise RuntimeError("Can not change the stype,try to use class 'signal' insteas of 'dt_signal'!")

class dt_impulse(dt_signal):
    '''
    单位冲击函数；
    t0：冲击零点，默认为0
    k：冲击大小，默认为1
    '''
    def __init__(self,t0=0,k=1): 
        super().__init__()
        self.t0 = t0
        self.k = k
        self._impulse_flag = True
        self.set_function(self.__set_function)
        self.set_t(-4+t0,5+t0)
        self.set_x(-1*k,2*k)
        self.set_sname('Unit_impulse')
        self.__ft == np.vectorize(self.__ft)
    def __set_function(self,t):
        if t == self.t0:
            return self.k
        return 0
    def __ft(self,omega):
        return np.exp(-1j*omega*self.t0)
    def __ft_str(self):
        if self.t0 == 0:
            return "1"
        return "e^(-j{}n0)".format(chr(969))
    def get_ft(self,t1=-10,t2=10):
        omega = np.arange(t1,t2,0.01)
        f_omega = self.__ft(omega)
        new_signal = st.ct_signal()
        new_signal.set_array(omega,f_omega)
        new_signal.set_sname(self.__ft_str())
        new_signal._spectrum_flag = True
        return new_signal

class dt_unit_step(dt_signal):
    '''
    单位阶跃函数；
    无参数；
    x = u(t)
    '''
    def __init__(self):
        super().__init__()
        self.set_t(-2,2)
        self.set_x(-1,2)
        self.set_function(self.__set_function)
        self.set_sname('Unit_step')
        self.__ft = np.vectorize(self.__ft)
        
    def __set_function(self,t):
        if t >= 0:
            return 1
        return 0
    def __ft(self,omega):
        other = 1/(1-np.exp(-1j*omega))
        omega = omega%(2*np.pi)
        if omega<=0 and omega >=-0.1*np.pi:
            impulse = 10*(omega)+np.pi
        elif omega>=0 and omega<=0.1*np.pi:
            impulse = -10*(omega)+np.pi
        else:
            impulse = 0
        return other + impulse

    def __ft_str(self):
        return "1/(1-e^(-jω)) + ∑πδ(ω-2πk)"

    def get_ft(self,t1=-10,t2=10):
        omega = np.arange(t1,t2,0.01)
        f_omega = self.__ft(omega)
        new_signal = st.ct_signal()
        new_signal.set_array(omega,f_omega)
        new_signal.set_sname(self.__ft_str())
        new_signal._spectrum_flag = True
        return new_signal

class dt_exp(dt_signal):
    '''
    指数函数，有四个参量，具体指代如下，无默认缺省值
    x(t) = k*e^((r+ji)*t) + b
    '''
    def __init__(self,k,r,i,b): 
        super().__init__()
        self.k = k
        self.r = r
        self.i = i
        self.b = b
        self.set_function(self.__set_function)
        self.set_t(-20,20)
        self.set_x(-20,20)
        self.set_sname('Exp')
        self.__ft = np.vectorize(self.__ft,otypes=[complex])
    def __set_function(self,t):
        return (self.k*np.exp(np.complex(self.r, self.i)*t) + self.b)

    def __ft(self,omega):
        def delta(omega):
            if omega<=0 and omega >=-0.1:
                return(10*(omega)+1)
            elif omega>=0 and omega<=0.1:
                return(-10*(omega)+1)
            return 0
        ft1 = 0
        ft2 = 0
        if(self.k != 0):
            ft1 = self.k*delta(omega-self.i)
        if(self.b != 0):
            ft2 = self.b*delta(omega)
        return ft1+ft2

    def __ft_str(self):
        if(self.k!=0 and self.r!=0):
            raise RuntimeError("not converge")
        if(self.k != 0):
            if(self.i==0):
                return str((self.k+self.b)*2)+"πδ(ω)"
            else:
                if(self.b!=0):
                    return str((self.k)*2)+"πδ(ω-"+str(self.i)+")+"+str((self.b)*2)+"πδ(ω)"
                else:
                    return str((self.k)*2)+"πδ(ω-"+str(self.i)+")"
        else:
            return str((self.b)*2)+"πδ(ω)"

    def get_ft(self, t1=-5, t2=5):
        omega = np.arange(t1,t2,step=0.01)
        f_omega = self.__ft(omega)
        new_signal = st.ct_signal()
        new_signal.set_array(omega,f_omega)
        new_signal.set_sname(self.__ft_str())
        new_signal._spectrum_flag = True
        return new_signal

class dt_sample(dt_signal):
    '''
    采样信号；
    无参数；
    x(t) = Sa(t)
    '''
    def __init__(self): 
        super().__init__()
        self.set_function(self.__set_function)
        self.set_t(-10,11)
        self.set_x(-0.5,1.25)
        self.set_sname('Sample')
    def __set_function(self,t):
        return (np.sinc(t/np.pi))
    def get_ft(self, t1=-5, t2=5):
        new_signal = st.ct_rect_period(1,2*np.pi)
        new_signal._spectrum_flag = True
        return new_signal

class dt_rect_period(dt_signal):
    '''
    周期方波信号；
    周期：T；
    小方参数：T1；
    x(t) = 1 when x<=T1 cycle:T
    '''
    def __init__(self,T1,T): 
        super().__init__()
        self.T1 = T1
        self.set_function(self.__set_function)
        self._T = T
        self.set_t(-T,T+1)
        self.set_x(-0.5,2)
        self.set_sname('rect_period')
    def __set_function(self,t):
        rest = t%self._T
        if (rest<=self.T1)or (rest>=self._T-self.T1):
            return 1
        return 0

class dt_rect(dt_signal):
    '''
    矩形信号;
    x = T;
    '''
    def __init__(self,T1): 
        super().__init__()
        self.T1 = T1
        self.set_function(self.__set_function)
        self.set_t(-5/2*T1,5/2*T1)
        self.set_x(-0.5,1.5)
        self.set_sname('rect_non_period')
        self.__ft = np.vectorize(self.__ft)
    def __set_function(self,t):
        if t>=-self.T1 and t<=self.T1:
            return 1.
        return 0.

    def __ft(self,omega):
        return 2*np.sin(omega*self.T1)/omega
    
    def __ft_str(self):
        return "2*sin({}*T1)/{}".format(chr(969),chr(969))

    def get_ft(self,t1=-10, t2=10):
        omega = np.arange(t1,t2,step=0.01)
        f_omega = self.__ft(omega)
        new_signal = st.ct_signal()
        new_signal.set_array(omega,f_omega)
        new_signal.set_sname(self.__ft_str())
        new_signal._spectrum_flag = True
        return new_signal

# mode:
# class dt_***(dt_signal):
    # def __init__(self,v1,v2): 
    #     super().__init__()
    #     self.v1 = v1
    #     self.v2 = v2
    #     self.set_function(self.__set_function)
    #     self.set_t(t1,t2)
    #     self.set_x(x1,x2)
    #     self.set_sname('SIGNAL_NAME')
    # def __set_function(self,t):
    #     return 0