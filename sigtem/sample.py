import numpy as np
import sigtem as st

#采样
def _delta(t,t_sample,x_sample):
    '''
    画冲击串的函数
    '''
    if t<=t_sample and t >=t_sample-0.1:
        return (10*(t-t_sample)+1)*x_sample
    elif t>=t_sample and t<=t_sample+0.1:
        return (-10*(t-t_sample)+1)*x_sample
    return 0.

_delta = np.vectorize(_delta,otypes=[float])

#时域采样
def sample_t(signal,T,t1=-10,t2=10):
    '''
    返回一个冲击采样的信号，图像显示原信号的实部的采样
    同时返回采样时间，以及采样数据，采样数据包括虚部
    '''
    if signal.is_spectrum():
        raise RuntimeError("can not sample t on spectrum series!")
    t_sample = np.arange(t1,t2,T)
    x_sample = signal.get_x(t_sample)
    x_sample_real = signal.get_x_real(t_sample)
    t_array = np.arange(t1,t2,0.01)
    x_array = np.zeros_like(t_array)
    for index in range(t_sample.shape[0]):
        x_i_array = _delta(t_array,t_sample[index],x_sample_real[index])
        x_array += x_i_array
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    new_signal.set_sname("Sample_impulse")
    return new_signal,t_sample,x_sample

#频域采样
def sample_s(signal,T,t1=-10,t2=10):
    '''
    在频域上进行采样，实际上就是将其拉开到无限周期，采样频炉为T
    '''
    if not signal.is_spectrum():
        raise RuntimeError("can not sample s on time series!")
    omega_s = 2*np.pi / T
    t_array = np.arange(t1,t2,0.01)
    t_period = (t_array+omega_s/2)%omega_s - omega_s/2
    x_array = signal.get_x(t_period)/T
    
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    new_signal._spectrum_flag = True
    new_signal.set_sname("Samlped_in_spectrum")

    return new_signal


