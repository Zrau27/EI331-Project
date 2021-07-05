import numpy as np
import sigtem as st

#ct_signals
class ct_signal(st.signal):
    '''
    连续信号类，无法改变信号类型
    '''
    def __init__(self):
        super().__init__()
        self.set_stype('CT')
        self.set_stype = self.__set_stype
    def __set_stype(self,stype):
        raise RuntimeError("Can not change the stype,try to use class 'signal' insteas of 'ct_signal'!")

class ct_impulse(ct_signal):
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
        self.set_t(t0-2*k,t0+2*k)
        self.set_x(-0.5,1.5*k)
        self.set_sname('impulse')
    def __set_function(self,t):
        if t<=self.t0 and t >=self.t0-0.1*self.k:
            return((10*(t-self.t0)+1)*self.k)
        elif t>=self.t0 and t<=self.t0+0.1*self.k:
            return((-10*(t-self.t0)+1)*self.k)
        return 0

    def get_ft(self, t1=-5, t2=5):
        ft_signal = super().get_ft(t1,t2)

        if self.t0 == 0:
            sname = str(self.k)
        elif self.t0 == 1:
            sname =  str(self.k)+"(-jsin("+"ω)+cos("+"ω))"
        else:
            sname =  str(self.k)+"(-jsin("+str(self.t0)+"ω)+cos("+str(self.t0)+"ω))"

        ft_signal.set_sname(sname)
        ft_signal._signal._spectrum_flag = True
        return ft_signal

class ct_impulse_train(ct_signal):
    '''
    Impulse Train；
    ωc：周期
    k：冲击大小，默认为1
    '''
    def __init__(self,f,k=1): 
        super().__init__()
        self.k = k
        self.omega_c = f
        self._impulse_flag = True
        self.set_function(self.__set_function)
        self.set_t(-5*self.omega_c-1,5*self.omega_c)
        self.set_x(-0.5,1.5*self.k)
        self.set_sname('Impulse_train')
        self.__ft = np.vectorize(self.__ft)

    def __set_function(self,t):
        t = t%self.omega_c
        if t<=0 and t >=-0.1*self.k:
            return(10*(t)+self.k)
        elif t>=0 and t<=0.1*self.k:
            return(-10*(t)+self.k)
        return 0

    def __ft(self,omega):
        omega1 = (2*np.pi)/self.omega_c
        omega = omega%omega1
        k = self.k*2*np.pi/self.omega_c
        if omega<=omega1 and omega >=omega1-0.1*k*omega1:
            return 10*(omega-omega1)+k*omega1
        elif omega>=omega1 and omega<=omega1+0.1*k*omega1:
            return -10*(omega-omega1)+k*omega1
        return 0

    def __ft_str(self):
        return "∑("+str(2/(self.omega_c))+'π'+")δ(ω-k*"+str(2/(self.omega_c))+'π'+")"

    def get_ft(self, t1=-5, t2=5):
        omega = np.arange(t1,t2,step=0.01)
        f_omega = self.__ft(omega)
        ft_signal = st.ct_signal()
        ft_signal.set_array(omega,f_omega)
        ft_signal.set_sname(self.__ft_str())
        ft_signal._spectrum_flag = True
        return ft_signal

class ct_unit_step(ct_signal):
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
        def delta(t):
            if t<=0 and t >=-0.1:
                return(10*(t)+1)
            elif t>=0 and t<=0.1:
                return(-10*(t)+1)
            return 0
        return (0-1j)/omega+np.pi*delta(omega)

    def __ft_str(self):
        return "1/jω+π*δ(ω)"

    def get_ft(self, t1=-5, t2=5):
        omega = np.arange(t1,t2,step=0.01)
        f_omega = self.__ft(omega)
        new_signal = st.ct_signal()
        new_signal.set_array(omega,f_omega)
        new_signal.set_sname(self.__ft_str())
        new_signal._spectrum_flag = True
        return new_signal

class ct_exp(ct_signal):
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
        self.set_t(-10,10)
        self.set_x(-4*k,4*k)
        self.set_sname('exp')
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

class ct_sample(ct_signal):
    '''
    采样信号；
    无参数；
    x(t) = Sa(t)
    '''
    def __init__(self): 
        super().__init__()
        self.set_function(self.__set_function)
        self.set_t(-20,20)
        self.set_x(-0.5,1.25)
        self.set_sname('sample')
    def __set_function(self,t):
        return (np.sinc(t/np.pi))
    def get_ft(self, t1=-5, t2=5):
        new_signal = st.ct_rect(1)
        new_signal._spectrum_flag = True
        return new_signal

class ct_rect_period(ct_signal):
    '''
    周期方波信号；
    周期：T；
    小方参数：T1；
    '''
    def __init__(self,T1,T): 
        super().__init__()
        self.T1 = T1
        self.set_function(self.__set_function)
        self._T = T
        self.omega0 = 2*np.pi/self._T
        self.set_t(-3/2*T,3/2*T)
        self.set_x(-0.5,2)
        self.set_sname('rect_period')
        self.__fs = np.vectorize(self.__fs)

    def __set_function(self,t):
        rest = t%self._T
        if (rest<=self.T1)or (rest>=self._T-self.T1):
            return 1
        return 0
    def __fs(self,k):
        if k == 0:
            return 2*self.T1/self._T
        return np.sin(k*self.omega0*self.T1)/k/np.pi
    def __fs_str(self):
        return "sin(k{}T1)/k{}".format(chr(969),chr(960))
    def get_fs(self, t1=-10, t2=11):
        k = np.arange(t1,t2,step=1)
        ak = self.__fs(k)
        new_signal = st.dt_signal()
        new_signal.set_array(k,ak)
        new_signal.set_sname(self.__fs_str())
        new_signal._spectrum_flag = True
        return new_signal

class ct_rect(ct_signal):
    '''
    矩形信号;
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
# class ct_****(ct_signal):
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