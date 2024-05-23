def frequency_zcr_classic(signal, sampling_frequency): 
    N = len(signal)
    summation = 0
    for i in range(1, N):  
        if (signal[i] * signal[i-1] < 0) : 
            summation=summation+1
    zcr = summation / (N-1) 
    #print(f" zcr = {zcr}, summation = {summation}, N = {N}") 
    return zcr * sampling_frequency / 2

def frequency_zcr_adapted(signal, sampling_frequency): 
    N = len(signal)
    summation = 0 
    for i in range(1, N): 
        summation = summation + abs(signal[i])
    L = 1.2 * summation / N 
    sum_ = 0  
    sp_minus = signal[0] - L 
    sn_minus = signal[0] + L 
    for i in range(1, N): 
        sp = signal[i] - L 
        sn = signal[i] + L 

        if ( (sp_minus < 0 and sp > 0) or (sn_minus < 0 and sn > 0)): 
            sum_ = sum_ + 1   

        sp_minus = signal[i - 1] - L 
        sn_minus = signal[i - 1] + L 
        zc = sum_ / (N - 1)
    return zc * sampling_frequency / 2
