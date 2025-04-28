import os
import sys
sys.path.append("C:/Users/Zidan/Documents/Kuliah/Semester 6/Signal Processing/iir_audio_denoise")
from src.filtering import apply_notch_filter
from src.utils import read_audio, save_audio

def denoise_audio(input_path, output_path, fs, notch_freqs, Q=30):
    """
    Denoise an audio file by applying notch filters to remove noise frequencies.

    input_path: Path to the input raw audio file
    output_path: Path to save the denoised audio file
    fs: Sampling rate
    notch_freqs: List of frequencies to remove using notch filters
    Q: Quality factor for the notch filter
    """
    _, signal = read_audio(input_path)

    for f0 in notch_freqs:
        signal = apply_notch_filter(signal, f0, Q, fs)

    save_audio(output_path, signal, fs)
    print(f"Denoised audio saved to {output_path}")

if __name__ == "__main__":
    input_audio = "data/raw/seg_101.wav"
    output_audio = "data/processed/denoised_seg_101.wav"
    
    notch_freqs = [49.6, 49.8, 438.2, 438.6, 446.2]  # You can add more as needed
    
    fs, _ = read_audio(input_audio)
    
    denoise_audio(input_audio, output_audio, fs, notch_freqs)