"""
localization.py

3D Sound Source Localization using
Time Difference of Arrival (TDoA)
and Nonlinear Least Squares Optimization.

Author:
Team Aerial Robotics
IIT Kanpur
"""

from itertools import combinations

import numpy as np
from scipy.optimize import least_squares

from configs.config import (
    SPEED_OF_SOUND,
    CUBE_SIDE,
)

###############################################################################
#                           MICROPHONE GEOMETRY
###############################################################################


class MicrophoneArray:
    """
    Represents the geometry of the microphone array.
    """

    def __init__(self, cube_side=CUBE_SIDE):

        self.cube_side = cube_side

        self.microphones = np.array([
            [0.0, 0.0, 0.0],
            [cube_side, cube_side, 0.0],
            [cube_side, 0.0, cube_side],
            [0.0, cube_side, cube_side],
        ])

        self.pairs = list(
            combinations(
                range(len(self.microphones)),
                2,
            )
        )

    def number_of_microphones(self):

        return len(self.microphones)

    def number_of_pairs(self):

        return len(self.pairs)


###############################################################################
#                           TDOA MODEL
###############################################################################


def expected_tdoa(
    point,
    pair,
    microphones,
    speed_of_sound=SPEED_OF_SOUND,
):
    """
    Compute expected TDoA for one microphone pair.
    """

    mic1 = microphones[pair[0]]

    mic2 = microphones[pair[1]]

    d1 = np.linalg.norm(point - mic1)

    d2 = np.linalg.norm(point - mic2)

    return (d1 - d2) / speed_of_sound


###############################################################################
#                           RESIDUAL FUNCTION
###############################################################################


def residuals(
    point,
    measured_tdoas,
    microphone_array,
):
    """
    Residual vector for least squares optimization.
    """

    residual = []

    for pair in microphone_array.pairs:

        measured = measured_tdoas[pair]

        predicted = expected_tdoa(
            point,
            pair,
            microphone_array.microphones,
        )

        residual.append(
            predicted - measured
        )

    return residual


###############################################################################
#                       COARSE GRID SEARCH
###############################################################################


def coarse_search(
    measured_tdoas,
    microphone_array,
    coarse_resolution=0.05,
):

    lower = np.array([
        0.0,
        0.0,
        -2.5,
    ])

    upper = np.array([
        0.1,
        0.1,
        0.1,
    ])

    xs = np.arange(
        lower[0],
        upper[0] + coarse_resolution / 2,
        coarse_resolution,
    )

    ys = np.arange(
        lower[1],
        upper[1] + coarse_resolution / 2,
        coarse_resolution,
    )

    zs = np.arange(
        lower[2],
        upper[2] + coarse_resolution / 2,
        coarse_resolution,
    )

    grid = np.array(
        np.meshgrid(
            xs,
            ys,
            zs,
        )
    ).T.reshape(-1, 3)

    errors = np.zeros(len(grid))

    for i, point in enumerate(grid):

        r = residuals(
            point,
            measured_tdoas,
            microphone_array,
        )

        errors[i] = np.sum(
            np.square(r)
        )

    best = np.argmin(errors)

    return grid[best]



###############################################################################
#                   NONLINEAR LEAST SQUARES REFINEMENT
###############################################################################


def refine_position(
    initial_guess,
    measured_tdoas,
    microphone_array,
    search_radius=0.04,
):
    """
    Refine the coarse estimate using nonlinear least squares.
    """

    lower_limit = np.maximum(
        initial_guess - search_radius,
        np.array([0.0, 0.0, -2.5]),
    )

    upper_limit = np.minimum(
        initial_guess + search_radius,
        np.array([0.1, 0.1, 0.1]),
    )

    result = least_squares(
        residuals,
        x0=initial_guess,
        bounds=(lower_limit, upper_limit),
        args=(measured_tdoas, microphone_array),
        method="trf",
    )

    return result


###############################################################################
#                       LOCALIZATION ENGINE
###############################################################################


class LocalizationEngine:
    """
    High-level localization engine.

    Input
    -----
    Dictionary of measured TDoAs.

    Output
    ------
    Estimated source position.
    """

    def __init__(self):

        self.array = MicrophoneArray()

    def estimate_position(self, measured_tdoas):

        coarse = coarse_search(
            measured_tdoas,
            self.array,
        )

        result = refine_position(
            coarse,
            measured_tdoas,
            self.array,
        )

        return result

    def estimate_position_cm(self, measured_tdoas):

        result = self.estimate_position(
            measured_tdoas
        )

        return result.x * 100.0


###############################################################################
#                       CONFIDENCE METRICS
###############################################################################


def localization_error(result):
    """
    Sum of squared residuals.
    """

    return np.sum(result.fun ** 2)


def localization_rmse(result):
    """
    Root Mean Square Error.
    """

    return np.sqrt(
        np.mean(result.fun ** 2)
    )


def confidence_score(result):
    """
    Very simple confidence estimate.

    Will later be replaced by a statistically
    meaningful confidence metric.
    """

    rmse = localization_rmse(result)

    confidence = np.exp(-500 * rmse)

    confidence = np.clip(
        confidence,
        0.0,
        1.0,
    )

    return confidence * 100


###############################################################################
#                           RESULT DISPLAY
###############################################################################


def print_results(result):

    position = result.x * 100

    print("\n" + "=" * 70)

    print("LOCALIZATION RESULTS")

    print("=" * 70)

    print(
        f"Estimated Position (cm): "
        f"[{position[0]:.2f}, "
        f"{position[1]:.2f}, "
        f"{position[2]:.2f}]"
    )

    print(
        f"Residual Error : "
        f"{localization_error(result):.8e}"
    )

    print(
        f"RMSE : "
        f"{localization_rmse(result):.8e}"
    )

    print(
        f"Confidence : "
        f"{confidence_score(result):.2f}%"
    )

    print("=" * 70)


###############################################################################
#                           STANDALONE TEST
###############################################################################


def demo():

    """
    Temporary demo using dummy TDoAs.

    This function will disappear once
    microphone simulation is added.
    """

    measured_tdoas = {

        (0, 1): 0.0,

        (0, 2): -0.000272,

        (0, 3): -0.000272,

        (1, 2): -0.000272,

        (1, 3): -0.000272,

        (2, 3): 0.0,

    }

    engine = LocalizationEngine()

    result = engine.estimate_position(
        measured_tdoas
    )

    print_results(result)


###############################################################################
#                                   MAIN
###############################################################################


if __name__ == "__main__":

    demo()