import numpy as np
import sigtem as st

def _filter(omega,omega_c):
    if abs(omega)<=omega_c:
        return 1
    return 0
_filter = np.vectorize(_filter)


def low_pass_filter(signal,omega_c,k=1,t1=-10,t2=10):
    '''
    低通滤波器，接受一个频域信号，输出一个带宽omegac，增益k的频域信号
    '''
    if not signal.is_spectrum():
        raise RuntimeError("can not filter s on time series!")
    t_array = np.arange(t1,t2,0.01)
    filter = _filter(t_array,omega_c)
    x_array = signal.get_x(t_array)
    x_array = x_array*filter*k
    print(x_array)
    new_signal = st.ct_signal()
    new_signal.set_array(t_array,x_array)
    new_signal._spectrum_flag = True
    new_signal.set_sname("Filtered_in_spectrum")
    return new_signal