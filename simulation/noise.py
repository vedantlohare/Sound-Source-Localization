"""
Noise Injection Utility

Loads the delayed audio,
injects white Gaussian noise,
saves WAV,
converts to MP3.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import librosa
import numpy as np
import soundfile as sf

from configs.config import (
    DELAYED_AUDIO,
    GENERATED_AUDIO,
    GENERATED_WAV,
    NOISE_DURATION,
    NOISE_STD,
    RANDOM_SEED,
)

np.random.seed(RANDOM_SEED)


def load_audio(path):
    """
    Load audio file.

    Returns
    -------
    signal : np.ndarray
    sample_rate : int
    """

    print(f"\nLoading audio:\n{path}")

    signal, sample_rate = librosa.load(path, sr=None)

    print(f"Sample Rate : {sample_rate} Hz")
    print(f"Samples     : {len(signal)}")
    print(f"Duration    : {len(signal)/sample_rate:.2f} seconds")

    return signal, sample_rate


def inject_white_noise(signal, sample_rate):
    """
    Inject white Gaussian noise into the first NOISE_DURATION seconds.
    """

    modified_signal = signal.copy()

    noise_samples = int(NOISE_DURATION * sample_rate)

    if noise_samples > len(modified_signal):
        raise ValueError("Audio is shorter than configured noise duration.")

    noise = np.random.normal(
        loc=0.0,
        scale=NOISE_STD,
        size=noise_samples
    ).astype(np.float32)

    modified_signal[:noise_samples] = noise

    print(f"\nInjected white noise for first {NOISE_DURATION:.2f} seconds.")

    return modified_signal


def save_wav(signal, sample_rate):
    """
    Save generated WAV.
    """

    sf.write(GENERATED_WAV, signal, sample_rate)

    print(f"\nSaved WAV:\n{GENERATED_WAV}")



def main():

    print("=" * 60)
    print("Noise Injection Utility")
    print("=" * 60)

    signal, sample_rate = load_audio(DELAYED_AUDIO)

    noisy_signal = inject_white_noise(signal, sample_rate)

    save_wav(noisy_signal, sample_rate)


    print("\nCompleted Successfully.")


if __name__ == "__main__":
    main()