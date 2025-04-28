import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

def plot_spectra_before_after(noisy_signal, denoised_signal, fs, title='Frequency Spectrum Comparison', figsize=(10, 6)):
    """
    Plot the frequency spectrum of the noisy and denoised signal.

    Args:
        noisy_signal: Original noisy signal
        denoised_signal: Signal after denoising
        fs: Sampling rate
        title: Title for the plot
        figsize: Size of the plot
    """
    # Calculate the Power Spectral Density (PSD)
    f_noisy, Pxx_noisy = welch(noisy_signal, fs, nperseg=1024)
    f_denoised, Pxx_denoised = welch(denoised_signal, fs, nperseg=1024)

    plt.figure(figsize=figsize)

    # Plot PSD of noisy signal
    plt.subplot(2, 1, 1)
    plt.semilogy(f_noisy, Pxx_noisy, label='Noisy Signal', color='red')
    plt.title(f'{title} - Noisy Signal Spectrum')
    plt.ylabel('Power/Frequency [dB/Hz]')
    plt.xlabel('Frequency [Hz]')
    plt.grid()

    # Plot PSD of denoised signal
    plt.subplot(2, 1, 2)
    plt.semilogy(f_denoised, Pxx_denoised, label='Denoised Signal', color='blue')
    plt.title(f'{title} - Denoised Signal Spectrum')
    plt.ylabel('Power/Frequency [dB/Hz]')
    plt.xlabel('Frequency [Hz]')
    plt.grid()

    plt.tight_layout()
    plt.show()