import numpy as np
import sigtem as st

def __conv_dt_nn(signal_1,signal_2,n,k1=-100,k2=100):
    '''
    定义累加函数；
    其中k1和k2定义了累加范围
    '''
    def sum(f,k1,k2,n):
        x = np.arange(k1,k2,1)
        return np.sum(f(x,n))
    def f(k,n):
        return signal_1.get_x(k)*signal_2.get_x(n-k)
    return sum(f,k1,k2,n)

#向量化
__conv_dt_nn = np.vectorize(__conv_dt_nn)

def conv_dt(signal_1,signal_2,start=-10,end=12):
    '''
    离散信号卷积函数，任意输入两个离散信号可得卷积结果；
    返回信号为数组信号模式；
    start与end参量控制返回数组信号的时间取样范围
    '''
    new_signal = st.dt_signal()
    new_signal.set_sname('Conved')
    t_array = np.arange(start,end,1)
    x_array = __conv_dt_nn(signal_1,signal_2,t_array)
    new_signal.set_array(t_array,x_array)
    return new_signal