"""
main.py

Entry point for the Sound Source Localization framework.
"""

import time

from algorithms.pipeline import LocalizationPipeline

from algorithms.evaluation import (
    print_evaluation,
)

from algorithms.localization import (
    print_results,
)

from configs.config import (
    TRUE_SOURCE,
)

from visualization.plot_3d import (
    plot_scene,
)


def main():

    start = time.perf_counter()

    pipeline = LocalizationPipeline()

    output = pipeline.run(TRUE_SOURCE)

    print_results(
        output["optimization_result"]
    )

    print_evaluation(
        output["true_position"],
        output["estimated_position"],
        output["confidence"],
    )

    plot_scene(
        output["true_position"],
        output["estimated_position"],
    )

    print(
        f"\nExecution Time : "
        f"{time.perf_counter()-start:.3f} s"
    )


if __name__ == "__main__":

    main()