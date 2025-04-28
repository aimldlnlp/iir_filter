import matplotlib.pyplot as plt
import numpy as np

def plot_signals_before_after(noisy_signal, denoised_signal, fs, title='Signal Comparison', figsize=(10, 6)):
    """
    Plot the original noisy signal and the denoised signal side by side.

    Args:
        noisy_signal: Original noisy signal
        denoised_signal: Signal after denoising
        fs: Sampling rate
        title: Title for the plot
        figsize: Size of the plot
    """
    times = np.arange(len(noisy_signal)) / float(fs)

    plt.figure(figsize=figsize)

    # Plot the original noisy signal
    plt.subplot(2, 1, 1)
    plt.plot(times, noisy_signal, label='Noisy Signal')
    plt.title(f'{title} - Noisy Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Time [s]')
    plt.grid()

    # Plot the denoised signal
    plt.subplot(2, 1, 2)
    plt.plot(times, denoised_signal, label='Denoised Signal', color='orange')
    plt.title(f'{title} - Denoised Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Time [s]')
    plt.grid()

    plt.tight_layout()
    plt.show()