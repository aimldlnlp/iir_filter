import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal

# --- 1. Baca file WAV ---
file_path = "data/raw/seg_101.wav"  # Ganti dengan path file kamu
fs, data = wav.read(file_path)

# Jika stereo, ambil salah satu channel
if len(data.shape) > 1:
    data = data[:, 0]

# Normalisasi data (jika integer)
if data.dtype != np.float32 and data.dtype != np.float64:
    data = data / np.iinfo(data.dtype).max

# --- 2. Tampilkan waveform ---
duration = len(data) / fs
time = np.linspace(0, duration, len(data))

plt.figure(figsize=(12, 4))
plt.plot(time, data, color='steelblue')
plt.title("Waveform of Noisy Audio")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 3. Tampilkan spektrum frekuensi (FFT) ---
n = len(data)
frequencies = np.fft.rfftfreq(n, d=1/fs)
magnitude_spectrum = np.abs(np.fft.rfft(data))

plt.figure(figsize=(12, 4))
plt.plot(frequencies, 20 * np.log10(magnitude_spectrum + 1e-10), color='darkred')
plt.title("Magnitude Spectrum (dB)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.tight_layout()
plt.xlim(0, fs / 2)  # Fokus pada Nyquist range
plt.show()

# --- 4. (Opsional) Spectrogram untuk analisis waktu-frekuensi ---
f, t, Sxx = signal.spectrogram(data, fs=fs, nperseg=1024)

plt.figure(figsize=(12, 4))
plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='inferno')
plt.title("Spectrogram of Noisy Audio")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar(label='Power [dB]')
plt.ylim(0, fs / 2)
plt.tight_layout()
plt.show()