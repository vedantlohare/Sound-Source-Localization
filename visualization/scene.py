"""
scene.py

Build visualization geometry for the localization scene.

Author:
Team Aerial Robotics
IIT Kanpur
"""

import numpy as np

from algorithms.localization import MicrophoneArray


def build_scene(true_position, estimated_position):
    """
    Returns all geometry required for visualization.
    """

    array = MicrophoneArray()

    scene = {

        "microphones": array.microphones,

        "true_source": np.asarray(true_position),

        "estimated_source": np.asarray(estimated_position),

    }

    return scene