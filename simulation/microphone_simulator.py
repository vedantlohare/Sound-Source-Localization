"""
microphone_simulator.py

Generate simulated recordings for a four microphone array.

Pipeline

Clean Audio
      ↓
Known Source Position
      ↓
Propagation Delay
      ↓
Fractional Delay
      ↓
mic1.wav
mic2.wav
mic3.wav
mic4.wav

Author:
Team Aerial Robotics
IIT Kanpur
"""

from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
from scipy.ndimage import shift

from algorithms.localization import MicrophoneArray

from configs.config import (
    ORIGINAL_AUDIO,
    SAMPLE_RATE,
    SPEED_OF_SOUND,
    TRUE_SOURCE,
    MIC_OUTPUT_FILES,
)


###############################################################################
# AUDIO LOADING
###############################################################################


def load_source_audio():

    signal, sr = librosa.load(
        ORIGINAL_AUDIO,
        sr=SAMPLE_RATE,
        mono=True,
    )

    return signal.astype(np.float32), sr


###############################################################################
# PROPAGATION
###############################################################################


def propagation_distances(source, microphones):

    distances = []

    for mic in microphones:

        distance = np.linalg.norm(source - mic)

        distances.append(distance)

    return np.array(distances)


###############################################################################
# ARRIVAL TIMES
###############################################################################


def arrival_times(distances):

    return distances / SPEED_OF_SOUND


###############################################################################
# FRACTIONAL DELAY
###############################################################################


def apply_delay(signal, delay_seconds, sample_rate):

    delay_samples = delay_seconds * sample_rate

    delayed = shift(
        signal,
        delay_samples,
        mode="constant",
        cval=0.0,
        order=3,
    )

    return delayed.astype(np.float32)


###############################################################################
# SAVE AUDIO
###############################################################################


def save_recordings(signals, sample_rate):

    for signal, path in zip(signals, MIC_OUTPUT_FILES):

        sf.write(path, signal, sample_rate)


###############################################################################
# MAIN SIMULATION
###############################################################################


def simulate_microphones(source_position=None):

    print("=" * 70)
    print("MICROPHONE SIMULATION")
    print("=" * 70)

    if source_position is None:

        source_position = np.array(TRUE_SOURCE)

    signal, sr = load_source_audio()

    array = MicrophoneArray()

    distances = propagation_distances(
        source_position,
        array.microphones,
    )

    arrivals = arrival_times(distances)

    earliest = arrivals.min()

    relative_delays = arrivals - earliest

    simulated = []

    print()

    for i in range(len(array.microphones)):

        simulated_signal = apply_delay(
            signal,
            relative_delays[i],
            sr,
        )

        simulated.append(simulated_signal)

        print(f"Microphone {i+1}")

        print(
            f"Distance      : {distances[i]:.4f} m"
        )

        print(
            f"Arrival Time  : {arrivals[i]*1000:.3f} ms"
        )

        print(
            f"Relative Delay: {relative_delays[i]*1000:.3f} ms"
        )

        print(
            f"Delay Samples : {relative_delays[i]*sr:.2f}"
        )

        print("-" * 50)

    save_recordings(
        simulated,
        sr,
    )

    print()

    print("Generated files:")

    for path in MIC_OUTPUT_FILES:

        print(path)

    print()

    return {
        "microphones": array.microphones,
        "distances": distances,
        "arrival_times": arrivals,
        "relative_delays": relative_delays,
    }


###############################################################################
# STANDALONE TEST
###############################################################################

if __name__ == "__main__":

    simulate_microphones()