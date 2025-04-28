import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def load_wav(filepath):
    """Load a WAV file."""
    rate, data = wav.read(filepath)
    return rate, data

def save_wav(filepath, rate, data):
    """Save a WAV file safely."""
    # Handle NaNs and Infs
    data = np.nan_to_num(data, nan=0.0, posinf=0.0, neginf=0.0)

    # Clip to int16 range
    data = np.clip(data, -32768, 32767)

    wav.write(filepath, rate, data.astype(np.int16))

def plot_signal(signal, rate, title='Signal', figsize=(10, 4)):
    """Plot the waveform of a signal."""
    times = np.arange(len(signal)) / float(rate)
    plt.figure(figsize=figsize)
    plt.plot(times, signal)
    plt.title(title)
    plt.ylabel('Amplitude')
    plt.xlabel('Time [s]')
    plt.grid()
    plt.tight_layout()
    plt.show()