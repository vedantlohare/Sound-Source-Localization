"""
test_gcc.py

Synthetic validation of the GCC-PHAT implementation.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from algorithms.gcc_phat import gcc_phat


FS = 8000


def generate_reference_signal():

    duration = 1.0

    t = np.linspace(
        0,
        duration,
        int(FS * duration),
        endpoint=False,
    )

    ref = signal.chirp(
        t,
        f0=100,
        f1=2000,
        t1=duration,
        method="linear",
    )

    ref += 0.05 * np.random.randn(len(ref))

    return ref


def create_delayed_signal(reference, delay_samples):

    delayed = np.concatenate(
        (
            np.zeros(delay_samples),
            reference,
            np.zeros(100),
        )
    )

    return delayed


def run_single_test(delay_samples):

    reference = generate_reference_signal()

    delayed = create_delayed_signal(
        reference,
        delay_samples,
    )

    expected_delay = delay_samples / FS

    estimated_delay, correlation = gcc_phat(
        delayed,
        reference,
        sample_rate=FS,
        max_tau=0.1,
    )

    error = abs(
        estimated_delay - expected_delay
    )

    print("=" * 60)

    print(
        f"Delay : {delay_samples} samples"
    )

    print(
        f"Expected : {expected_delay:.6f} s"
    )

    print(
        f"Estimated : {estimated_delay:.6f} s"
    )

    print(
        f"Error : {error:.8f} s"
    )

    return correlation


def visualize(correlation):

    plt.figure(figsize=(12,4))

    plt.plot(correlation)

    plt.title("Synthetic GCC-PHAT Correlation")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def main():

    delays = [
        10,
        25,
        50,
        100,
        200,
    ]

    last = None

    for delay in delays:

        last = run_single_test(delay)

    visualize(last)


if __name__ == "__main__":

    main()