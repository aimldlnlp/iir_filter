import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.signal as signal
import json
import os

def load_audio(filepath):
    data, fs = sf.read(filepath)
    if data.ndim > 1:
        data = data[:, 0]  # Use first channel if stereo
    return data, fs

def plot_waveform(data, fs, save_path):
    times = np.arange(len(data)) / fs
    plt.figure(figsize=(10, 2))
    plt.plot(times, data)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fft(data, fs, save_path):
    N = len(data)
    freqs = np.fft.rfftfreq(N, d=1/fs)
    spectrum = np.abs(np.fft.rfft(data)) / N
    spectrum_db = 20 * np.log10(spectrum + 1e-12)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs, spectrum_db)
    plt.title("Magnitude Spectrum (dB)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_spectrogram(data, fs, save_path):
    plt.figure(figsize=(10, 4))
    plt.specgram(data, NFFT=1024, Fs=fs, noverlap=512, cmap='plasma')
    plt.title("Spectrogram")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="dB")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_psd(data, fs, save_path):
    f, Pxx = signal.welch(data, fs, nperseg=1024)
    plt.figure(figsize=(10, 4))
    plt.semilogy(f, Pxx)
    plt.title("Power Spectral Density")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power/Frequency (dB/Hz)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def extract_analysis_metrics(data, fs):
    spectrum = np.abs(np.fft.rfft(data))
    freqs = np.fft.rfftfreq(len(data), d=1/fs)

    return {
        "average_energy_below_100Hz": float(spectrum[freqs < 100].mean()),
        "average_energy_above_8000Hz": float(spectrum[freqs > 8000].mean()),
        "average_energy_full_band": float(spectrum.mean())
    }

def save_analysis_result(result, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

def main():
    file_path = "data/raw/seg_101.wav"
    output_prefix = "analysis/results/sample"

    data, fs = load_audio(file_path)

    plot_waveform(data, fs, save_path=f"{output_prefix}_waveform.png")
    plot_fft(data, fs, save_path=f"{output_prefix}_fft.png")
    plot_spectrogram(data, fs, save_path=f"{output_prefix}_spectrogram.png")
    plot_psd(data, fs, save_path=f"{output_prefix}_psd.png")

    metrics = extract_analysis_metrics(data, fs)
    save_analysis_result(metrics, output_path=f"{output_prefix}_analysis.json")

    print(f"✅ Analysis complete. Results saved in 'analysis/results/'.")

if __name__ == "__main__":
    main()