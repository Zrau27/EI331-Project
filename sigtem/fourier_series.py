import numpy as np
import sigtem as st

def __ct_get_ak(signal,k,delta_taf=0.1):
    '''
    获得连续信号的k个傅立叶级数
    '''
    taf1 = 0
    taf2 = signal._T
    def integral(f,taf1,taf2,delta_taf):
        taf = np.arange(taf1,taf2,delta_taf)
        return (np.sum(f(taf)*delta_taf))
    def f(taf):
        return signal.get_x(taf)*np.exp((-k*2*np.pi/signal._T*taf*1j))
    return integral(f,taf1,taf2,delta_taf)/signal._T

__ct_get_ak = np.vectorize(__ct_get_ak)

def __dt_get_ak(signal,k):
    '''
    获得离散信号的第k个傅立叶级数
    '''
    k = k%signal._T
    r1 = 0
    r2 = signal._T
    def sum(f,r1,r2):
        r = np.arange(r1,r2,1)
        return np.sum(f(r))
    def f(r):
        return signal.get_x(r)*np.exp(-k*2*np.pi/signal._T*r*1j)
    return sum(f,r1,r2)/signal._T

__dt_get_ak = np.vectorize(__dt_get_ak)

def fs(signal,start=-4,end=6):
    '''
    接受一个周期信号，返回这个周期信号的傅立叶级数，返回的是一个离散信号；
    代表傅立叶级数；
    '''
    if not signal.is_periodic():
        raise RuntimeError('Can not define fourier_series on unperiod signal!')
    k = np.arange(start,end,1)
    if signal.get_stype() == "CT":
        ak = __ct_get_ak(signal,k)
    else:
        ak = __dt_get_ak(signal,k)
    new_signal = st.dt_signal()
    new_signal.set_sname('Fourier series')
    new_signal.set_array(k,ak)
    new_signal._spectrum_flag = True
    return new_signal

def ifs(signal,N,T,t1=-6,t2=6):
    '''
    接受一个傅立叶级数信号，输出其逆变换
    N，求和上下限
    T，傅立叶信号原信号的周期
    '''
    k = np.arange(-N-1,N,1)
    ak = signal.get_x(k)
    t_array = np.arange(t1,t2,0.01)
    x_array = np.zeros_like(t_array,dtype=np.complex)
    for index in range(k.shape[0]):
        x_i_array = ak[index]*np.exp(-1j*k[index]*2*np.pi/T*t_array)
        x_array += x_i_array
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    return new_signal
