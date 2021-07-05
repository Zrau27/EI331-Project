import numpy as np
import sigtem as st

def __ct_get_omega(signal,omega,delta_taf=0.1):
    '''
    获得连续信号傅立叶变换对应的omega值
    '''
    taf1 = -100 #积分上下限
    taf2 = 100
    def integral(f,taf1,taf2,delta_taf):
        taf = np.arange(taf1,taf2,delta_taf)
        return (np.sum(f(taf)*delta_taf))
    def f(taf):
        return signal.get_x(taf)*np.exp(-1j*omega*taf)
    return integral(f,taf1,taf2,delta_taf)

__ct_get_omega = np.vectorize(__ct_get_omega)

def __dt_get_omega(signal,omega):
    '''
    获得离散信号傅立叶变换对应的omega值
    '''
    r1 = -100 #累加上下限
    r2 = 100
    def sum(f,r1,r2):
        r = np.arange(r1,r2,1)
        return np.sum(f(r))
    def f(r):
        return signal.get_x(r)*np.exp(-1j*omega*r)
    return sum(f,r1,r2)

__dt_get_omega = np.vectorize(__dt_get_omega)

def ft(signal,start=-5,end=5):
    '''
    接受一个非周期信号，返回这个周期信号的傅立叶变换，返回的是一个连续数组信号；
    代表傅立叶变换；
    '''
    delta_omega = 0.1
    if  signal.is_periodic():
        raise RuntimeError('Can not define fourier_transform on period signal!')
    omega = np.arange(start,end,delta_omega)
    if signal.get_stype() == "CT":
        if signal.is_impulse():
            f_omega = signal.k*np.exp(-1j*omega*signal.t0)
        else:
            f_omega = __ct_get_omega(signal,omega)
    else:
        f_omega = __dt_get_omega(signal,omega)
    new_signal = st.ct_signal()
    new_signal.set_sname('Fourier transform')
    new_signal.set_array(omega,f_omega)
    new_signal._spectrum_flag = True
    return new_signal