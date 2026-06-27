"""
pipeline.py

End-to-end localization pipeline.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import numpy as np

from algorithms.evaluation import (
    euclidean_error,
)

from algorithms.localization import (
    LocalizationEngine,
    confidence_score,
)

from algorithms.tdoa import (
    TDoAEstimator,
)

from simulation.microphone_simulator import (
    simulate_microphones,
)


class LocalizationPipeline:
    """
    Complete localization pipeline.

    Simulation
        ↓
    GCC-PHAT
        ↓
    Localization
        ↓
    Evaluation
    """

    def __init__(self):

        self.engine = LocalizationEngine()

        self.tdoa = TDoAEstimator()

    def run(self, true_position):

        simulate_microphones(
            source_position=np.asarray(true_position)
        )

        measured_tdoas = self.tdoa.estimate()

        result = self.engine.estimate_position(
            measured_tdoas
        )

        estimated = result.x

        error = euclidean_error(
            np.asarray(true_position),
            estimated,
        )

        confidence = confidence_score(result)

        return {

            "true_position": np.asarray(true_position),

            "estimated_position": estimated,

            "error": error,

            "confidence": confidence,

            "optimization_result": result,

        }