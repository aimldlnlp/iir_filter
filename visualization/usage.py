# visualization/usage.py

import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import load_wav
from visualization.plot_signals import plot_signals_before_after
from visualization.plot_spectra import plot_spectra_before_after

def visualize_audio_comparison(input_path_noisy, input_path_denoised):
    """
    Load noisy and denoised audio, and visualize them in both time and frequency domains.

    Args:
        input_path_noisy: Path to the noisy audio file
        input_path_denoised: Path to the denoised audio file
    """
    # Load the noisy signal (before filtering)
    _, noisy_signal = load_wav(input_path_noisy)
    
    # Load the denoised signal (after filtering)
    _, denoised_signal = load_wav(input_path_denoised)
    
    # Get the sampling rate
    fs = 16000  # Assuming 16kHz for example, change this to match your signal

    # Plot the time-domain comparison (waveform)
    plot_signals_before_after(noisy_signal, denoised_signal, fs, title='Noisy vs Denoised Signal')

    # Plot the frequency-domain comparison (Power Spectral Density)
    plot_spectra_before_after(noisy_signal, denoised_signal, fs, title='Noisy vs Denoised Signal Spectrum')

def main():
    # Define file paths for the noisy and denoised signals
    input_path_noisy = 'data/raw/seg_101.wav'          # Path to the noisy audio file
    input_path_denoised = 'data/processed/denoised_seg_101.wav'   # Path to the already denoised audio file
    
    # Visualize the comparison
    visualize_audio_comparison(input_path_noisy, input_path_denoised)

if __name__ == '__main__':
    main()