import os
from src.denoise import denoise_audio_lowpass, denoise_audio_multibandstop, denoise_audio_highpass

def main():
    input_path = 'data/raw/seg_101.wav'
    output_path = 'data/processed'
    os.makedirs(output_path, exist_ok=True)

    cutoff_freq = 1700  # Hz, adjust according to your signal characteristics

    # for filename in os.listdir(input_dir):
    #     if filename.endswith('.wav'):
    #         input_path = os.path.join(input_dir, filename)
    #         output_path = os.path.join(output_dir, f"denoised_highpass_{filename}")

    #         print(f"Applying high-pass filtering to {filename}...")
    #         denoise_audio_highpass(input_path, output_path, cutoff_freq=cutoff_freq, order=4)
    
    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith('.wav'):
                input_file = os.path.join(input_path, filename)
                output_path = os.path.join(output_path, f"denoised_{filename}")

                print(f"Applying high-pass filtering to {filename}...")
                denoise_audio_highpass(input_path, output_path, cutoff_freq=cutoff_freq, order=4)
    elif os.path.isfile(input_path):
        filename = os.path.basename(input_path)
        output_path = os.path.join(output_path, f"denoised_{filename}")

        print(f"Applying high-pass filtering to {filename}...")
        denoise_audio_highpass(input_path, output_path, cutoff_freq=cutoff_freq, order=4)
    else:
        print(f"Error: {input_path} is not a valid file or directory.")

"""
def main():
    input_path = 'data/raw/seg_101.wav'
    output_path = 'data/processed'
    os.makedirs(output_path, exist_ok=True)

    # for filename in os.listdir(input_dir):
    #     if filename.endswith('.wav'):
    #         input_path = os.path.join(input_dir, filename)
    #         output_path = os.path.join(output_dir, f"denoised_{filename}")
            
    #         print(f"Denoising {filename}...")
    #         denoise_audio_lowpass(input_path, output_path)

    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith('.wav'):
                input_file = os.path.join(input_path, filename)
                output_path = os.path.join(output_path, f"denoised_{filename}")

                print(f"Denoising {filename}...")
                denoise_audio_lowpass(input_path, output_path)
    elif os.path.isfile(input_path):
        filename = os.path.basename(input_path)
        output_path = os.path.join(output_path, f"denoised_{filename}")

        print(f"Denoising {filename}...")
        denoise_audio_lowpass(input_path, output_path)
    else:
        print(f"Error: {input_path} is not a valid file or directory.")
"""
        
"""
def main():
    input_path = 'data/raw/seg_101.wav'  # can be a file or directory
    output_dir = 'data/processed'
    os.makedirs(output_dir, exist_ok=True)

    # Define noise bands you want to remove
    bands_to_remove = [
        (49.60, 49.80),
        # (438.10, 438.70),
        # (446.10, 446.30)
    ]

    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith('.wav'):
                input_file = os.path.join(input_path, filename)
                output_path = os.path.join(output_dir, f"denoised_{filename}")

                print(f"Applying multi-bandstop filtering to {filename}...")
                denoise_audio_multibandstop(input_file, output_path, bands=bands_to_remove, order=4)
    elif os.path.isfile(input_path):
        filename = os.path.basename(input_path)
        output_path = os.path.join(output_dir, f"denoised_{filename}")

        print(f"Applying multi-bandstop filtering to {filename}...")
        denoise_audio_multibandstop(input_path, output_path, bands=bands_to_remove, order=4)
    else:
        print(f"Error: {input_path} is not a valid file or directory.")
"""     
            
if __name__ == '__main__':
    main()