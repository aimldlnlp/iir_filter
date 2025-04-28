import numpy as np
from scipy import signal
from src.filter_design import design_iir_lowpass, design_iir_bandstop, design_iir_highpass

def apply_filter(data, b, a):
    """Apply an IIR filter to a signal."""
    return signal.filtfilt(b, a, data)

def denoise_audio_lowpass(input_path, output_path, cutoff_freq, order=6, filter_type='butter'):
    """Denoise an audio file using an IIR lowpass filter."""
    from src.utils import load_wav, save_wav

    fs, data = load_wav(input_path)
    
    # If stereo, process each channel separately
    if len(data.shape) == 2:
        data_denoised = np.zeros_like(data)
        for ch in range(data.shape[1]):
            b, a = design_iir_lowpass(cutoff_freq, fs, order, filter_type)
            data_denoised[:, ch] = apply_filter(data[:, ch], b, a)
    else:
        b, a = design_iir_lowpass(cutoff_freq, fs, order, filter_type)
        data_denoised = apply_filter(data, b, a)

    save_wav(output_path, fs, data_denoised)

def denoise_audio_highpass(input_path, output_path, cutoff_freq, order=4, filter_type='butter'):
    """
    Denoise audio by applying a high-pass filter.

    Args:
        input_path: Path to the noisy wav file
        output_path: Where to save the denoised wav file
        cutoff_freq: Cutoff frequency for high-pass filter
        order: Filter order
        filter_type: 'butter' or 'cheby1'
    """
    from src.utils import load_wav, save_wav

    fs, data = load_wav(input_path)

    # If stereo, process each channel separately
    if len(data.shape) == 2:
        data_denoised = np.copy(data)
        for ch in range(data.shape[1]):
            b, a = design_iir_highpass(cutoff_freq, fs, order, filter_type)
            data_denoised[:, ch] = signal.filtfilt(b, a, data_denoised[:, ch])
    else:
        b, a = design_iir_highpass(cutoff_freq, fs, order, filter_type)
        data_denoised = signal.filtfilt(b, a, data)

    save_wav(output_path, fs, data_denoised)
    
def denoise_audio_multibandstop(input_path, output_path, bands, order=4, filter_type='butter'):
    """
    Denoise audio by applying multiple band-stop filters.

    Args:
        input_path: Path to the noisy wav file
        output_path: Where to save the denoised wav file
        bands: List of (lowcut, highcut) tuples in Hz
        order: Filter order
        filter_type: 'butter' or 'cheby1'
    """
    from src.utils import load_wav, save_wav

    fs, data = load_wav(input_path)
    
    # If stereo, process each channel separately
    if len(data.shape) == 2:
        data_denoised = np.copy(data)
        for ch in range(data.shape[1]):
            for band in bands:
                b, a = design_iir_bandstop(band, fs, order, filter_type)
                data_denoised[:, ch] = signal.filtfilt(b, a, data_denoised[:, ch])
    else:
        data_denoised = np.copy(data)
        for band in bands:
            b, a = design_iir_bandstop(band, fs, order, filter_type)
            data_denoised = signal.filtfilt(b, a, data_denoised)

    save_wav(output_path, fs, data_denoised)