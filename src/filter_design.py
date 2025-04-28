from scipy import signal

def design_iir_lowpass(cutoff_freq, fs, order=5, filter_type='butter'):
    """
    Design an IIR lowpass filter.
    
    Args:
        cutoff_freq: Cutoff frequency in Hz
        fs: Sampling frequency
        order: Order of the filter
        filter_type: Type of IIR filter ('butter', 'cheby1', etc.)
    
    Returns:
        b, a: Numerator and denominator coefficients
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist

    if filter_type == 'butter':
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    elif filter_type == 'cheby1':
        b, a = signal.cheby1(order, 0.5, normal_cutoff, btype='low', analog=False)
    else:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    return b, a

def design_iir_highpass(cutoff_freq, fs, order=4, filter_type='butter'):
    """
    Design an IIR high-pass filter.

    Args:
        cutoff_freq: Cutoff frequency in Hz
        fs: Sampling frequency
        order: Filter order
        filter_type: Type of IIR filter ('butter', 'cheby1', etc.)

    Returns:
        b, a: Numerator and denominator coefficients
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist

    if filter_type == 'butter':
        b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    elif filter_type == 'cheby1':
        b, a = signal.cheby1(order, 0.5, normal_cutoff, btype='high', analog=False)
    else:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    return b, a

def design_iir_bandstop(band, fs, order=4, filter_type='butter'):
    """
    Design an IIR band-stop (notch) filter.

    Args:
        band: Tuple (lowcut, highcut) frequencies in Hz to attenuate
        fs: Sampling frequency
        order: Filter order
        filter_type: Type of IIR filter ('butter', 'cheby1', etc.)

    Returns:
        b, a: Numerator and denominator coefficients
    """
    nyquist = 0.5 * fs
    low = band[0] / nyquist
    high = band[1] / nyquist

    if filter_type == 'butter':
        b, a = signal.butter(order, [low, high], btype='bandstop')
    elif filter_type == 'cheby1':
        b, a = signal.cheby1(order, 0.5, [low, high], btype='bandstop')
    else:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    return b, a