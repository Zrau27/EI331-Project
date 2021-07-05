import re
import numpy as np
import sigtem as st

def linear_interpolation(t_sample,x_sample):
    '''
    接受采样的时间与信号大小，进行线性插值并返回插值信号
    '''
    new_signal = st.ct_signal()
    new_signal.set_array(t_sample,x_sample)
    return new_signal

def resample_t(signal,T,k,t1=-20,t2=20):
    t_array = np.arange(t1,t2,0.01)
    x_array = signal.get_x(t_array)*k/T
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    new_signal.set_sname("Resampled")
    return new_signal

def resample_s(signal,T,omega1=-10,omega2=10):
    omega_array = np.arange(omega1,omega2,0.01)
    def h(omega):
        return 1/T*(np.sin(omega*T/2)/omega*2)**2
    h = np.vectorize(h)
    x_array = h(omega_array)*signal.get_x(omega_array)
    new_signal = st.ct_signal()
    new_signal.set_array(omega_array,x_array)
    new_signal.set_sname("Resampled")
    new_signal._spectrum_flag = True
    return new_signal
