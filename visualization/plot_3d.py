"""
plot_3d.py

3D visualization for Sound Source Localization.

Author:
Team Aerial Robotics
IIT Kanpur
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from configs.config import RESULTS_DIR

from visualization.scene import build_scene


def plot_scene(true_position, estimated_position):

    scene = build_scene(
        true_position,
        estimated_position,
    )

    microphones = scene["microphones"]

    true_source = scene["true_source"]

    estimated_source = scene["estimated_source"]

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(
        111,
        projection="3d",
    )

    #######################################################################
    # Microphones
    #######################################################################

    ax.scatter(
        microphones[:, 0],
        microphones[:, 1],
        microphones[:, 2],
        s=80,
        marker="^",
        label="Microphones",
    )

    #######################################################################
    # True source
    #######################################################################

    ax.scatter(
        true_source[0],
        true_source[1],
        true_source[2],
        s=120,
        marker="o",
        label="True Source",
    )

    #######################################################################
    # Estimated source
    #######################################################################

    ax.scatter(
        estimated_source[0],
        estimated_source[1],
        estimated_source[2],
        s=120,
        marker="x",
        label="Estimated Source",
    )

    #######################################################################
    # Error vector
    #######################################################################

    ax.plot(
        [true_source[0], estimated_source[0]],
        [true_source[1], estimated_source[1]],
        [true_source[2], estimated_source[2]],
        linewidth=2,
        label="Localization Error",
    )

    #######################################################################

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")

    ax.set_title("3D Sound Source Localization")

    ax.legend()

    #######################################################################
    # Equal scaling
    #######################################################################

    all_points = np.vstack([
        microphones,
        true_source,
        estimated_source,
    ])

    mins = all_points.min(axis=0)
    maxs = all_points.max(axis=0)

    center = (mins + maxs) / 2
    radius = np.max(maxs - mins) / 2 + 0.05

    ax.set_xlim(center[0] - radius, center[0] + radius)
    ax.set_ylim(center[1] - radius, center[1] + radius)
    ax.set_zlim(center[2] - radius, center[2] + radius)

    plt.tight_layout()

    RESULTS_DIR.mkdir(exist_ok=True)

    output = RESULTS_DIR / "localization_scene.png"

    plt.savefig(
        output,
        dpi=300,
    )

    print(f"\nVisualization saved to:\n{output}")

    plt.show()