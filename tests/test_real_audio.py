"""
test_real_audio.py

Integration test for the GCC-PHAT library.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import matplotlib.pyplot as plt
import numpy as np

from algorithms.gcc_phat import (
    estimate_delay,
    print_delay_summary,
)

from configs.config import (
    ORIGINAL_AUDIO,
    DELAYED_AUDIO,
    SAMPLE_RATE,
)


def visualize_correlation(correlation):

    plt.figure(figsize=(12, 5))

    plt.plot(correlation)

    plt.title("GCC-PHAT Cross Correlation")

    plt.xlabel("Lag")

    plt.ylabel("Correlation")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def visualize_peak(correlation):

    peak = np.argmax(correlation)

    radius = 250

    start = max(0, peak - radius)

    end = min(len(correlation), peak + radius)

    plt.figure(figsize=(12, 5))

    plt.plot(
        range(start, end),
        correlation[start:end],
    )

    plt.axvline(
        peak,
        color="red",
        linestyle="--",
        label="Estimated Delay",
    )

    plt.legend()

    plt.grid(True)

    plt.title("Peak Correlation")

    plt.tight_layout()

    plt.show()


def main():

    delay, correlation = estimate_delay(
        ORIGINAL_AUDIO,
        DELAYED_AUDIO,
    )

    print_delay_summary(
        delay,
        SAMPLE_RATE,
    )

    visualize_correlation(correlation)

    visualize_peak(correlation)


if __name__ == "__main__":

    main()