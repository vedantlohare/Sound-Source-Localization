"""
tdoa.py

Automatic Time Difference of Arrival estimation
for every microphone pair using GCC-PHAT.

Author:
Team Aerial Robotics
IIT Kanpur
"""

from itertools import combinations

from algorithms.gcc_phat import estimate_delay

from configs.config import (
    MIC_OUTPUT_FILES,
)


###############################################################################
#                           TDOA ESTIMATOR
###############################################################################


class TDoAEstimator:
    """
    Automatically estimates TDoAs between
    every microphone pair.
    """

    def __init__(self):

        self.microphone_files = MIC_OUTPUT_FILES

        self.pairs = list(
            combinations(
                range(len(self.microphone_files)),
                2,
            )
        )

    def estimate(self):

        measured = {}

        print("\n" + "=" * 70)
        print("AUTOMATIC TDOA ESTIMATION")
        print("=" * 70)

        for pair in self.pairs:

            file1 = self.microphone_files[pair[0]]

            file2 = self.microphone_files[pair[1]]

            delay, _ = estimate_delay(
                file1,
                file2,
            )

            measured[pair] = delay

            print(
                f"Pair {pair}: "
                f"{delay*1000:.4f} ms"
            )

        print("=" * 70)

        return measured


###############################################################################
#                           STANDALONE TEST
###############################################################################

if __name__ == "__main__":

    estimator = TDoAEstimator()

    tdoas = estimator.estimate()

    print()

    print(tdoas)