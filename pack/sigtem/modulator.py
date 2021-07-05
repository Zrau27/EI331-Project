import sigtem as st
import numpy as np

def am_mdlt_t(signal,omega,t1=-5,t2=5):
    '''
    使用AM调制器在时域上进行调制，输入一个时域信号，参数omega，输出调制过后的信号
    '''
    if signal.get_stype()=="DT":
        raise RuntimeError("Can't define ct_am on DT signals!")
    t_array = np.arange(t1,t2,0.01)
    x_array = signal.get_x(t_array)
    x_array = x_array*np.cos(omega*t_array)
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    return new_signal

def am_mdlt_s(signal,omega):
    '''
    使用AM调制器在频域上进行调制，输入一个频域信号，参数omega，输出调制过后的频域信号
    '''
    t1 = -5/2*omega
    t2 = 5/2*omega
    if signal.get_stype()=="DT":
        raise RuntimeError("Can't define ct_am on DT signals!")
    t_array = np.arange(t1,t2,0.01)
    x_array_1 = signal.get_x(t_array-omega)
    x_array_2 = signal.get_x(t_array+omega)
    x_array = x_array_1 + x_array_2
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    return new_signal