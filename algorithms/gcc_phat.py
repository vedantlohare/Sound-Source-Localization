"""
gcc_phat.py

Core signal processing library for acoustic time-delay estimation
using Generalized Cross Correlation with Phase Transform (GCC-PHAT).

Author:
Team Aerial Robotics
IIT Kanpur

Refactored for modular use.
"""

from pathlib import Path

import librosa
import numpy as np

from configs.config import (
    SAMPLE_RATE,
    ANALYSIS_LENGTH,
    MAX_DELAY,
    INTERPOLATION,
)

################################################################################
#                               AUDIO LOADING
################################################################################


def load_audio(filepath, target_sr=SAMPLE_RATE):
    """
    Load an audio file.

    Parameters
    ----------
    filepath : str | Path

    target_sr : int

    Returns
    -------
    signal : ndarray

    sample_rate : int
    """

    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(
            f"Audio file not found:\n{filepath}"
        )

    signal, sample_rate = librosa.load(
        filepath,
        sr=target_sr,
        mono=True,
    )

    return signal.astype(np.float32), sample_rate


################################################################################
#                           AUDIO PREPROCESSING
################################################################################


def preprocess_audio(
    signal1,
    signal2,
    sample_rate,
    analysis_length=ANALYSIS_LENGTH,
):
    """
    Prepare two signals before GCC-PHAT.

    Steps

    1. Truncate to analysis length.

    2. Make equal length.
    """

    max_samples = int(
        analysis_length * sample_rate
    )

    signal1 = signal1[:max_samples]
    signal2 = signal2[:max_samples]

    minimum = min(
        len(signal1),
        len(signal2),
    )

    signal1 = signal1[:minimum]
    signal2 = signal2[:minimum]

    return signal1, signal2


################################################################################
#                           GCC-PHAT ALGORITHM
################################################################################


def gcc_phat(
    signal,
    reference,
    sample_rate,
    max_tau=MAX_DELAY,
    interpolation=INTERPOLATION,
):
    """
    Estimate Time Difference of Arrival using GCC-PHAT.

    Parameters
    ----------
    signal

    reference

    sample_rate

    max_tau

    interpolation

    Returns
    -------
    tau

    correlation
    """

    n = signal.shape[0] + reference.shape[0]

    SIGNAL = np.fft.rfft(signal, n=n)

    REFERENCE = np.fft.rfft(reference, n=n)

    cross_power = SIGNAL * np.conj(REFERENCE)

    magnitude = np.abs(cross_power)

    magnitude[magnitude == 0] = np.finfo(float).eps

    cross_correlation = np.fft.irfft(
        cross_power / magnitude,
        n=interpolation * n,
    )

    max_shift = int(interpolation * n / 2)

    if max_tau is not None:

        max_shift = min(
            int(interpolation * sample_rate * max_tau),
            max_shift,
        )

    cross_correlation = np.concatenate(

        (
            cross_correlation[-max_shift:],
            cross_correlation[: max_shift + 1],
        )

    )

    shift = np.argmax(cross_correlation)

    shift -= max_shift

    tau = shift / float(interpolation * sample_rate)

    return tau, cross_correlation

################################################################################
#                       HIGH LEVEL DELAY ESTIMATION
################################################################################


def estimate_delay(
    reference_audio,
    target_audio,
    sample_rate=SAMPLE_RATE,
    analysis_length=ANALYSIS_LENGTH,
    max_delay=MAX_DELAY,
    interpolation=INTERPOLATION,
):
    """
    Complete delay estimation pipeline.

    Parameters
    ----------
    reference_audio : str | Path
        Reference audio file.

    target_audio : str | Path
        Delayed audio file.

    Returns
    -------
    delay : float
        Estimated delay in seconds.

    correlation : ndarray
        GCC-PHAT correlation.
    """

    print("=" * 70)
    print("GCC-PHAT Delay Estimation")
    print("=" * 70)

    print("\nLoading audio files...")

    reference_signal, sr1 = load_audio(
        reference_audio,
        target_sr=sample_rate,
    )

    target_signal, sr2 = load_audio(
        target_audio,
        target_sr=sample_rate,
    )

    if sr1 != sr2:
        raise RuntimeError(
            "Sample rates do not match."
        )

    print(f"Sample Rate : {sr1} Hz")

    print("\nPreprocessing signals...")

    reference_signal, target_signal = preprocess_audio(
        reference_signal,
        target_signal,
        sample_rate=sr1,
        analysis_length=analysis_length,
    )

    print("Running GCC-PHAT...")

    delay, correlation = gcc_phat(
        signal=target_signal,
        reference=reference_signal,
        sample_rate=sr1,
        max_tau=max_delay,
        interpolation=interpolation,
    )

    print("\nCompleted.")

    return delay, correlation


################################################################################
#                           RESULT DISPLAY
################################################################################


def print_delay_summary(delay, sample_rate):
    """
    Pretty-print delay estimation results.
    """

    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    print(f"Delay (seconds)      : {delay:.6f}")

    print(f"Delay (milliseconds) : {delay*1000:.3f}")

    print(f"Delay (samples)      : {delay*sample_rate:.2f}")

    print("=" * 70)


################################################################################
#                           STANDALONE TEST
################################################################################


if __name__ == "__main__":

    from configs.config import (
        ORIGINAL_AUDIO,
        DELAYED_AUDIO,
    )

    delay, correlation = estimate_delay(
        ORIGINAL_AUDIO,
        DELAYED_AUDIO,
    )

    print_delay_summary(
        delay,
        SAMPLE_RATE,
    )