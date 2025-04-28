import unittest
import numpy as np
from src.filter_design import design_iir_lowpass
from src.denoise import apply_filter

class TestIIRFilter(unittest.TestCase):

    def setUp(self):
        # Create a simple noisy sinusoidal signal
        np.random.seed(0)
        self.fs = 16000  # Sample rate
        t = np.linspace(0, 1.0, self.fs)
        self.clean_signal = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave
        noise = np.random.normal(0, 0.5, self.clean_signal.shape)
        self.noisy_signal = self.clean_signal + noise

    def test_design_iir_lowpass(self):
        b, a = design_iir_lowpass(cutoff_freq=1000, fs=self.fs, order=6)
        self.assertEqual(len(b), 7)  # For 6th order, 7 coefficients
        self.assertEqual(len(a), 7)

    def test_apply_filter_reduces_noise(self):
        b, a = design_iir_lowpass(cutoff_freq=1000, fs=self.fs, order=6)
        filtered_signal = apply_filter(self.noisy_signal, b, a)
        
        original_power = np.mean(self.noisy_signal**2)
        filtered_power = np.mean(filtered_signal**2)
        
        self.assertLess(filtered_power, original_power)

if __name__ == '__main__':
    unittest.main()