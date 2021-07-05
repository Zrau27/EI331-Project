import numpy as np
import sigtem as st

def __conv_ct_nn(signal_1,signal_2,t,taf1=-100,taf2=100,delta_taf=0.1):
    '''
    普通信号的卷积计算，通过面积积分估算方法进行计算，针对某一时间得到值；
    taf指定积分上下限以及间隔面积条的边长；
    '''
    def integral(f,taf1,taf2,t,delta_taf):
        x = np.arange(taf1,taf2,delta_taf)
        return (np.sum(f(x,t)*delta_taf))
    def f(taf,t):
        return signal_1.get_x(taf)*signal_2.get_x(t-taf)
    return integral(f,taf1,taf2,t,delta_taf)

def __conv_ct_in(signal_impulse,signal,t):
    '''
    某一个冲击函数与一个正常信号的卷积，直接返回原信号的时移以及比例变换；
    '''
    return signal_impulse.k*(signal.get_x(t-signal_impulse.t0))

#向量化函数
__conv_ct_nn = np.vectorize(__conv_ct_nn)
__conv_ct_in = np.vectorize(__conv_ct_in)

def conv_ct(signal_1,signal_2,start=-10,end=10,delta_t=0.1):
    '''
    接受任意两个连续时间信号（必须要求信号的stype为“CT”），输出一个卷积信号，卷积信号为向量形式；
    其中start以及end变量规定了输出信号向量的起始终止时间，delta_t规定了向量信号的时间间隔
    '''
    new_signal = st.ct_signal()
    new_signal.set_sname("Conved")
    t_array = np.arange(start,end,delta_t)
    if signal_1.is_impulse() and signal_2.is_impulse():
        raise RuntimeError("Can't define conv on two impulse")
    elif signal_1.is_impulse() and (not signal_2.is_impulse()):
        x_array = __conv_ct_in(signal_1,signal_2,t_array)
    elif signal_2.is_impulse() and (not signal_1.is_impulse()):
        x_array = __conv_ct_in(signal_2,signal_1,t_array)
    else:
        x_array = __conv_ct_nn(signal_1,signal_2,t_array)
    new_signal.set_array(t_array,x_array)
    return new_signal