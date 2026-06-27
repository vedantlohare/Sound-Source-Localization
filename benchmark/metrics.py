"""
metrics.py

Statistical metrics for localization benchmarking.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import numpy as np


def mean_error(errors):
    return float(np.mean(errors))


def median_error(errors):
    return float(np.median(errors))


def rmse(errors):
    errors = np.asarray(errors)
    return float(np.sqrt(np.mean(errors ** 2)))


def maximum_error(errors):
    return float(np.max(errors))


def minimum_error(errors):
    return float(np.min(errors))


def standard_deviation(errors):
    return float(np.std(errors))


def confidence_statistics(confidences):

    confidences = np.asarray(confidences)

    return {

        "mean": float(np.mean(confidences)),

        "minimum": float(np.min(confidences)),

        "maximum": float(np.max(confidences)),

        "std": float(np.std(confidences)),
    }


def summarize(errors, confidences):

    return {

        "Mean Error": mean_error(errors),

        "Median Error": median_error(errors),

        "RMSE": rmse(errors),

        "Maximum Error": maximum_error(errors),

        "Minimum Error": minimum_error(errors),

        "Std Dev": standard_deviation(errors),

        "Confidence": confidence_statistics(confidences),

    }