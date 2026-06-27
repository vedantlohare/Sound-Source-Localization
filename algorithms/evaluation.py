"""
evaluation.py

Evaluation utilities for the Sound Source Localization framework.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import numpy as np


###############################################################################
# POSITION ERRORS
###############################################################################


def euclidean_error(true_position, estimated_position):
    """
    Euclidean localization error in meters.
    """
    return np.linalg.norm(
        estimated_position - true_position
    )


def axis_error(true_position, estimated_position):
    """
    Axis-wise signed errors.
    """
    return estimated_position - true_position


###############################################################################
# PRINT REPORT
###############################################################################


def print_evaluation(
    true_position,
    estimated_position,
    confidence,
):

    error = euclidean_error(
        true_position,
        estimated_position,
    )

    axis = axis_error(
        true_position,
        estimated_position,
    )

    print("\n" + "=" * 70)
    print("LOCALIZATION EVALUATION")
    print("=" * 70)

    print(
        f"True Position (cm): "
        f"[{true_position[0]*100:.2f}, "
        f"{true_position[1]*100:.2f}, "
        f"{true_position[2]*100:.2f}]"
    )

    print(
        f"Estimated Position (cm): "
        f"[{estimated_position[0]*100:.2f}, "
        f"{estimated_position[1]*100:.2f}, "
        f"{estimated_position[2]*100:.2f}]"
    )

    print()

    print(
        f"Error X : {axis[0]*100:.2f} cm"
    )

    print(
        f"Error Y : {axis[1]*100:.2f} cm"
    )

    print(
        f"Error Z : {axis[2]*100:.2f} cm"
    )

    print()

    print(
        f"Euclidean Error : {error*100:.2f} cm"
    )

    print(
        f"Confidence : {confidence:.2f}%"
    )

    print("=" * 70)