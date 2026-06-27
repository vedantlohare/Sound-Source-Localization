"""
benchmark.py

Benchmark the complete localization pipeline.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import time
import numpy as np

from algorithms.pipeline import LocalizationPipeline

from benchmark.metrics import summarize

from benchmark.report import (
    save_csv,
    save_summary,
    generate_plots,
)


class Benchmark:
    """
    Runs repeated localization experiments using randomly
    generated source positions.
    """

    def __init__(
        self,
        number_of_trials=100,
        random_seed=42,
    ):

        self.pipeline = LocalizationPipeline()

        self.number_of_trials = number_of_trials

        self.rng = np.random.default_rng(random_seed)

    ###########################################################################
    # RANDOM SOURCE GENERATION
    ###########################################################################

    def random_source(self):
        """
        Generate a random source position inside
        the localization volume.
        """

        x = self.rng.uniform(0.0, 0.10)

        y = self.rng.uniform(0.0, 0.10)

        z = self.rng.uniform(-0.10, 0.10)

        return np.array([x, y, z])

    ###########################################################################
    # MAIN BENCHMARK
    ###########################################################################

    def run(self):

        errors = []

        confidences = []

        execution_times = []

        trial_results = []

        print("=" * 70)
        print("LOCALIZATION BENCHMARK")
        print("=" * 70)

        successful_trials = 0
        failed_trials = 0

        for trial in range(self.number_of_trials):
            try:
                source = self.random_source()

                start = time.perf_counter()

                result = self.pipeline.run(source)

                elapsed = time.perf_counter() - start

                execution_times.append(elapsed)

                errors.append(result["error"])

                confidences.append(result["confidence"])

                trial_results.append({

                    "true_position": result["true_position"],

                    "estimated_position": result["estimated_position"],

                    "error": result["error"],

                    "confidence": result["confidence"],

                    "runtime": elapsed,

                })

                print(

                    f"Trial {trial+1:03d}/{self.number_of_trials}"

                    f" | Error = {result['error']*100:.2f} cm"

                    f" | Confidence = {result['confidence']:.2f}%"

                    f" | Runtime = {elapsed:.3f} s"

                )
                
                successful_trials += 1


            except Exception as e:
                failed_trials += 1
                print(f"Trial {trial+1} failed: {e}")
                continue
        

        #######################################################################
        # Compute Statistics
        #######################################################################

        summary = summarize(
            errors,
            confidences,
        )

        average_runtime = np.mean(execution_times)

        #######################################################################
        # Console Summary
        #######################################################################

        print("\n" + "=" * 70)
        print("BENCHMARK SUMMARY")
        print("=" * 70)

        print(f"Trials            : {self.number_of_trials}")

        print(f"Mean Error        : {summary['Mean Error']*100:.2f} cm")

        print(f"Median Error      : {summary['Median Error']*100:.2f} cm")

        print(f"RMSE              : {summary['RMSE']*100:.2f} cm")

        print(f"Maximum Error     : {summary['Maximum Error']*100:.2f} cm")

        print(f"Minimum Error     : {summary['Minimum Error']*100:.2f} cm")

        print(f"Std Deviation     : {summary['Std Dev']*100:.2f} cm")

        print()

        print("Confidence Statistics")

        print("----------------------")

        print(
            f"Mean Confidence   : "
            f"{summary['Confidence']['mean']:.2f}%"
        )

        print(
            f"Minimum           : "
            f"{summary['Confidence']['minimum']:.2f}%"
        )

        print(
            f"Maximum           : "
            f"{summary['Confidence']['maximum']:.2f}%"
        )

        print(
            f"Std               : "
            f"{summary['Confidence']['std']:.2f}%"
        )

        print()

        print(
            f"Average Runtime   : "
            f"{average_runtime:.3f} s"
        )

        print("=" * 70)

        #######################################################################
        # Save Reports
        #######################################################################

        print("\nSaving benchmark reports...")

        save_csv(trial_results)

        save_summary(
            summary,
            average_runtime,
        )

        generate_plots(
            errors,
            confidences,
            execution_times,
        )

        print("\nBenchmark completed successfully.")

        #######################################################################

        return {

            "trial_results": trial_results,

            "errors": errors,

            "confidences": confidences,

            "execution_times": execution_times,

            "summary": summary,

        }


###############################################################################
# MAIN
###############################################################################

if __name__ == "__main__":

    benchmark = Benchmark(
        number_of_trials=10,
    )

    benchmark.run()