"""
report.py

Benchmark reporting utilities.

Author:
Team Aerial Robotics
IIT Kanpur
"""

from pathlib import Path
import csv

import matplotlib.pyplot as plt
import numpy as np

from configs.config import RESULTS_DIR


def save_csv(results):

    RESULTS_DIR.mkdir(exist_ok=True)

    csv_path = RESULTS_DIR / "benchmark_results.csv"

    with open(csv_path, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Trial",
            "True X",
            "True Y",
            "True Z",
            "Estimated X",
            "Estimated Y",
            "Estimated Z",
            "Error (m)",
            "Confidence (%)",
            "Runtime (s)",
        ])

        for i, trial in enumerate(results, start=1):

            writer.writerow([
                i,
                *trial["true_position"],
                *trial["estimated_position"],
                trial["error"],
                trial["confidence"],
                trial["runtime"],
            ])

    print(f"\nSaved CSV:\n{csv_path}")


def save_summary(summary, average_runtime):

    summary_path = RESULTS_DIR / "benchmark_summary.txt"

    with open(summary_path, "w") as f:

        f.write("Benchmark Summary\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Mean Error: {summary['Mean Error']*100:.2f} cm\n")
        f.write(f"Median Error: {summary['Median Error']*100:.2f} cm\n")
        f.write(f"RMSE: {summary['RMSE']*100:.2f} cm\n")
        f.write(f"Maximum Error: {summary['Maximum Error']*100:.2f} cm\n")
        f.write(f"Minimum Error: {summary['Minimum Error']*100:.2f} cm\n")
        f.write(f"Std Dev: {summary['Std Dev']*100:.2f} cm\n\n")

        f.write(f"Average Runtime: {average_runtime:.3f} s\n")

    print(f"Saved Summary:\n{summary_path}")


def histogram(values, xlabel, title, filename):

    plt.figure(figsize=(8, 5))

    plt.hist(values, bins=20)

    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.title(title)

    plt.tight_layout()

    path = RESULTS_DIR / filename

    plt.savefig(path, dpi=300)

    plt.close()

    print(f"Saved Plot:\n{path}")


def generate_plots(errors, confidences, runtimes):

    histogram(
        np.array(errors) * 100,
        "Localization Error (cm)",
        "Localization Error Distribution",
        "error_histogram.png",
    )

    histogram(
        confidences,
        "Confidence (%)",
        "Confidence Distribution",
        "confidence_histogram.png",
    )

    histogram(
        runtimes,
        "Runtime (s)",
        "Runtime Distribution",
        "runtime_histogram.png",
    )