"""
Global configuration for the Sound Source Localization project.
Modify values here instead of hardcoding them throughout the project.
"""

from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

ORIGINAL_DIR = DATA_DIR / "original"
GENERATED_DIR = DATA_DIR / "generated"

RESULTS_DIR = PROJECT_ROOT / "results"

# =============================================================================
# Audio Files
# =============================================================================

ORIGINAL_AUDIO = ORIGINAL_DIR / "B_R-vocals.mp3"

DELAYED_AUDIO = GENERATED_DIR / "B_R-vocals_delayed.wav"

OUTPUT_AUDIO = GENERATED_DIR / "B_R-vocals_noisy.wav"

# Microphone simulator outputs

MIC1_AUDIO = GENERATED_DIR / "mic1.wav"
MIC2_AUDIO = GENERATED_DIR / "mic2.wav"
MIC3_AUDIO = GENERATED_DIR / "mic3.wav"
MIC4_AUDIO = GENERATED_DIR / "mic4.wav"

MIC_OUTPUT_FILES = [
    MIC1_AUDIO,
    MIC2_AUDIO,
    MIC3_AUDIO,
    MIC4_AUDIO,
]

# =============================================================================
# Audio Parameters
# =============================================================================

SAMPLE_RATE = 22050

ANALYSIS_LENGTH = 30

MAX_DELAY = 5.0

INTERPOLATION = 16

# =============================================================================
# Noise Parameters
# =============================================================================

NOISE_DURATION = 2.62

NOISE_STD = 0.10

RANDOM_SEED = 42

# =============================================================================
# Localization Parameters
# =============================================================================

SPEED_OF_SOUND = 343.0

MIC_COUNT = 4

CUBE_SIDE = 0.09

MIC_SPACING = 0.09

# =============================================================================
# Simulation Parameters
# =============================================================================

TRUE_SOURCE = (
    0.06,
    0.03,
    0.02,
)