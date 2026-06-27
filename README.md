# 🎯 Sound Source Localization using GCC-PHAT

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge&logo=numpy)
![SciPy](https://img.shields.io/badge/SciPy-Optimization-8CAAE6?style=for-the-badge&logo=scipy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Research-grade acoustic source localization framework that estimates the **3D position of a sound source** using **Generalized Cross Correlation with Phase Transform (GCC-PHAT)**, **Time Difference of Arrival (TDoA)** estimation, and **nonlinear least squares optimization**.

Built as part of the **IMAV 2025 Indoor Challenge** with an emphasis on clean software architecture, reproducibility, modularity, benchmarking, and visualization.

</p>

---

# 📖 Overview

This project implements an end-to-end acoustic localization pipeline capable of estimating the three-dimensional position of a sound source from multiple microphone recordings.

Unlike many competition-oriented implementations, this repository is structured as a reusable software framework rather than a collection of scripts. Every stage of the localization pipeline is modular, independently testable, and designed to support future research and development.

The framework includes:

- Microphone array simulation
- Fractional propagation delay generation
- GCC-PHAT based TDoA estimation
- Nonlinear optimization for source localization
- Automatic benchmarking
- 3D visualization
- Docker support for reproducible execution

The codebase emphasizes software engineering best practices, making it suitable as both a research prototype and a portfolio project.

---

# ✨ Features

## Signal Processing

- GCC-PHAT implementation from scratch
- High-resolution cross-correlation
- Configurable interpolation factor
- Automatic delay estimation
- Audio preprocessing pipeline

---

## Localization

- Four-microphone tetrahedral array
- Time Difference of Arrival (TDoA) estimation
- Nonlinear Least Squares optimization
- Confidence estimation
- Localization error computation

---

## Simulation

- Configurable microphone geometry
- Physics-based propagation delay
- Fractional sample delay simulation
- Automatic generation of synchronized microphone recordings

---

## Benchmarking

- Random source generation
- Automated performance evaluation
- RMSE computation
- Mean localization error
- Runtime analysis
- Confidence statistics

---

## Visualization

- 3D microphone array
- Ground-truth source
- Estimated source
- Localization error vector
- Automatic figure generation

---

## Software Engineering

- Modular architecture
- Docker support
- Config-driven design
- Unit and integration tests
- Research-style repository structure
- Fully reproducible experiments

---

# 🏗 Repository Structure

```text
Sound-Source-Localization/

├── algorithms/
│   ├── evaluation.py
│   ├── gcc_phat.py
│   ├── localization.py
│   ├── pipeline.py
│   └── tdoa.py
│
├── benchmark/
│   ├── benchmark.py
│   ├── metrics.py
│   └── report.py
│
├── configs/
│   └── config.py
│
├── data/
│   ├── generated/
│   └── original/
│
├── results/
│
├── simulation/
│   ├── microphone_simulator.py
│   └── noise.py
│
├── tests/
│   ├── test_gcc.py
│   └── test_real_audio.py
│
├── visualization/
│   ├── plot_3d.py
│   └── scene.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── main.py
```

---

# 🚀 Complete Processing Pipeline

The localization framework follows the pipeline below.

```text
                  True Source Position
                           │
                           ▼
              Microphone Array Simulation
                           │
                           ▼
                Generate Microphone Signals
                           │
                           ▼
                     GCC-PHAT Processing
                           │
                           ▼
               Time Difference of Arrival
                           │
                           ▼
             Nonlinear Least Squares Solver
                           │
                           ▼
               Estimated Source Position
                     │              │
                     ▼              ▼
              Performance      Visualization
               Evaluation
```

---

# ⚡ Quick Start (Docker)

The recommended way to run the project is using Docker.

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sound-Source-Localization.git

cd Sound-Source-Localization
```

## Build the Docker image

```bash
docker compose up --build
```

The pipeline will automatically execute:

- Microphone simulation
- GCC-PHAT delay estimation
- TDoA generation
- 3D localization
- Evaluation
- Visualization

No additional setup is required beyond Docker Desktop (Windows/macOS) or Docker Engine (Linux).

---

# 🖥 Native Execution

Install dependencies

```bash
pip install -r requirements.txt
```

Run the localization pipeline

```bash
python main.py
```

Run the benchmark suite

```bash
python -m benchmark.benchmark
```

Run the GCC-PHAT synthetic test

```bash
python -m tests.test_gcc
```

Run the real audio integration test

```bash
python -m tests.test_real_audio
```

---

# 📂 Output

After execution, the project automatically generates:

```text
data/generated/

mic1.wav
mic2.wav
mic3.wav
mic4.wav
```

and

```text
results/

localization_scene.png

benchmark_results.csv

benchmark_summary.txt

error_histogram.png

confidence_histogram.png

runtime_histogram.png
```

These outputs can be used for evaluation, debugging, visualization, and benchmarking.

---

# ⚙ Configuration

The project follows a **configuration-driven architecture**. All configurable parameters are centralized in:

```text
configs/config.py
```

This allows experiments to be reproduced without modifying the implementation.

The configuration file contains parameters such as:

| Parameter | Description |
|-----------|-------------|
| `SAMPLE_RATE` | Audio sampling frequency |
| `SPEED_OF_SOUND` | Speed of sound used for TDoA calculations |
| `CUBE_SIDE` | Side length of the tetrahedral microphone array |
| `TRUE_SOURCE` | Ground-truth sound source position |
| `ANALYSIS_LENGTH` | Duration of audio used for GCC-PHAT |
| `INTERPOLATION` | GCC-PHAT interpolation factor |
| `RANDOM_SEED` | Benchmark reproducibility |

Changing the experiment requires modifying only the configuration file rather than the algorithm implementations.

---

# 🧩 System Architecture

The project is intentionally divided into independent modules following the **Single Responsibility Principle**.

Each module performs one well-defined task and communicates with the others through clean interfaces.

```text
                    ┌────────────────────┐
                    │   Configuration    │
                    └─────────┬──────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │ Microphone Simulator   │
                  └─────────┬──────────────┘
                            │
                            ▼
                 Generated Microphone Audio
                            │
                            ▼
                  ┌────────────────────────┐
                  │     GCC-PHAT Engine    │
                  └─────────┬──────────────┘
                            │
                            ▼
                 Pairwise TDoA Estimation
                            │
                            ▼
                  ┌────────────────────────┐
                  │ Localization Engine    │
                  └─────────┬──────────────┘
                            │
                            ▼
                  Estimated Source Position
                     │                │
                     ▼                ▼
              Evaluation        Visualization
                     │
                     ▼
              Benchmark Reports
```

This modular design allows each component to be independently tested, improved, or replaced without affecting the rest of the system.

---

# 🔬 Localization Pipeline

The complete localization workflow consists of six stages.

## Stage 1 — Microphone Simulation

A synthetic sound source is placed at a known three-dimensional position.

Using the microphone geometry, the framework computes:

- Distance from source to each microphone
- Propagation time
- Relative arrival delay

Fractional delays are then applied to generate realistic synchronized microphone recordings.

Output:

```text
mic1.wav
mic2.wav
mic3.wav
mic4.wav
```

---

## Stage 2 — GCC-PHAT Processing

Every microphone pair is processed using the Generalized Cross Correlation with Phase Transform (GCC-PHAT).

The algorithm estimates the relative propagation delay while remaining robust to signal amplitude variations and reverberation.

Output:

```text
TDoA Dictionary

{
 (0,1): ...
 (0,2): ...
 ...
}
```

---

## Stage 3 — Localization

The estimated TDoAs are passed to the nonlinear localization engine.

The framework performs:

1. Coarse grid search
2. Nonlinear least squares refinement

The optimization returns the estimated source position.

---

## Stage 4 — Evaluation

Since the simulator knows the true source position, the framework automatically computes:

- Euclidean localization error
- Axis-wise error
- Confidence score
- Runtime statistics

This enables objective evaluation of localization accuracy.

---

## Stage 5 — Visualization

The localization result is visualized using a three-dimensional plot containing:

- Microphone array
- Ground-truth source
- Estimated source
- Localization error vector

The generated figure is automatically stored inside the `results/` directory.

---

## Stage 6 — Benchmarking

The benchmark framework executes the complete localization pipeline for multiple randomly generated source positions.

For each trial it records:

- Estimated position
- Localization error
- Confidence
- Execution time

At the end of the benchmark the framework generates:

- Summary statistics
- CSV reports
- Histograms
- Performance metrics

---

# 🛠 Core Technologies

The project is implemented entirely in Python using open-source scientific computing libraries.

| Library | Purpose |
|----------|----------|
| Python | Primary programming language |
| NumPy | Numerical computations |
| SciPy | Optimization and signal processing |
| Librosa | Audio loading and preprocessing |
| SoundFile | WAV file generation |
| Matplotlib | Visualization |
| Docker | Reproducible execution |

---

# 📐 Engineering Principles

Rather than implementing a monolithic script, the repository follows several software engineering principles.

### Modular Design

Every algorithm is implemented in its own module.

### Separation of Concerns

Simulation, localization, benchmarking, and visualization are independent.

### Config-Driven Development

Experimental parameters are stored separately from implementation.

### Reproducibility

Benchmark results can be reproduced through deterministic configuration.

### Extensibility

Future localization algorithms can be integrated without modifying the surrounding infrastructure.

---

# 📊 Example Console Output

```text
======================================================================
3D SOUND SOURCE LOCALIZATION
======================================================================

STEP 1 : Microphone Simulation
✔ Generated mic1.wav
✔ Generated mic2.wav
✔ Generated mic3.wav
✔ Generated mic4.wav

STEP 2 : GCC-PHAT

Pair (0,1)
Pair (0,2)
Pair (0,3)

STEP 3 : Localization

Estimated Position :
[5.02, 3.11, 1.96] cm

Confidence :
99.42 %

STEP 4 : Evaluation

Euclidean Error :
1.84 cm

STEP 5 : Visualization

Saved:

results/localization_scene.png
```

---

# 📁 Project Components

## `algorithms/`

Contains the core signal processing and localization algorithms.

Responsible for:

- GCC-PHAT
- TDoA estimation
- Localization
- Evaluation
- Pipeline orchestration

---

## `simulation/`

Contains the synthetic microphone simulator.

Responsible for:

- Propagation delay
- Fractional delay generation
- WAV creation

---

## `visualization/`

Responsible for producing publication-quality figures for localization results.

---

## `benchmark/`

Automates large-scale evaluation of localization performance and generates statistical reports.

---

## `tests/`

Contains synthetic and real-audio validation tests for the GCC-PHAT implementation.


---

# 📚 Algorithm Overview

This section provides a high-level overview of the algorithms implemented in the framework. It is intended to help readers understand the overall localization pipeline rather than serve as a complete theoretical derivation.

---

## 1. Generalized Cross Correlation with Phase Transform (GCC-PHAT)

The first step in the localization pipeline is estimating the relative arrival time of a sound signal at different microphones.

Instead of comparing signals directly in the time domain, GCC-PHAT performs cross-correlation in the frequency domain while normalizing the magnitude spectrum.

This normalization emphasizes phase information and improves robustness against:

- Signal amplitude variations
- Reverberation
- Environmental noise

The estimated delay corresponds to the peak of the normalized cross-correlation function.

---

## 2. Time Difference of Arrival (TDoA)

Once delays between every microphone pair are estimated, they are converted into a **Time Difference of Arrival (TDoA)** dictionary.

Example:

```python
{
    (0,1): -0.000231,
    (0,2): 0.000417,
    (0,3): -0.000112,
    ...
}
```

Each value represents the relative propagation delay between two microphones.

These measurements form the constraints used during localization.

---

## 3. Source Localization

The localization engine estimates the source position by minimizing the difference between:

- Measured TDoAs
- Predicted TDoAs computed from a candidate source position

The optimization consists of two stages:

### Coarse Search

A grid search provides a robust initial estimate.

### Nonlinear Refinement

The initial estimate is refined using nonlinear least squares optimization.

The resulting position corresponds to the estimated sound source location.

---

## 4. Evaluation

Since the microphone recordings are generated through simulation, the true source position is always known.

The framework automatically computes:

- Euclidean localization error
- Axis-wise localization error
- Root Mean Square Error (RMSE)
- Confidence score

These metrics allow quantitative evaluation of localization performance.

---

# 📈 Benchmark Framework

The benchmark module evaluates localization performance across many randomly generated source positions.

Each benchmark trial performs the complete localization pipeline:

```text
Random Source Position
        │
        ▼
Microphone Simulation
        │
        ▼
Generate Microphone Signals
        │
        ▼
GCC-PHAT
        │
        ▼
Automatic TDoA Estimation
        │
        ▼
Localization
        │
        ▼
Performance Evaluation
```

For every trial the framework stores:

- Ground truth position
- Estimated position
- Localization error
- Confidence
- Runtime

Summary statistics include:

- Mean Error
- Median Error
- RMSE
- Maximum Error
- Minimum Error
- Standard Deviation
- Average Confidence
- Average Runtime

The benchmark module also exports CSV reports and visualization plots for further analysis.

---

# 📊 Generated Results

Running the benchmark automatically generates the following outputs.

```text
results/

benchmark_results.csv

benchmark_summary.txt

error_histogram.png

confidence_histogram.png

runtime_histogram.png

localization_scene.png
```

These artifacts make it easy to compare algorithm performance across different experiments.

---

# 🧪 Testing

The repository includes both synthetic and real-audio tests.

## Synthetic GCC-PHAT Validation

```bash
python -m tests.test_gcc
```

Validates delay estimation using artificially delayed signals with known ground truth.

---

## Real Audio Validation

```bash
python -m tests.test_real_audio
```

Evaluates the GCC-PHAT implementation using recorded audio samples.

---

## Full Localization Pipeline

```bash
python main.py
```

Runs:

- Microphone simulation
- Automatic TDoA estimation
- Source localization
- Evaluation
- Visualization

---

## Benchmark

```bash
python -m benchmark.benchmark
```

Runs multiple localization experiments and generates benchmark reports.

---

# 📸 Example Results

After running the framework, the following visualizations are automatically generated.

> Replace the placeholders below with screenshots from your repository.

## 3D Localization

```text
docs/images/localization_scene.png
```

*(Insert screenshot here)*

---

## Error Distribution

```text
docs/images/error_histogram.png
```

*(Insert screenshot here)*

---

## Confidence Distribution

```text
docs/images/confidence_histogram.png
```

*(Insert screenshot here)*

---

# 🚀 Future Work

Potential improvements include:

- Real-time localization using live microphone arrays
- ROS 2 integration
- Multiple simultaneous sound source localization
- Adaptive speed-of-sound estimation
- Alternative localization algorithms (SRP-PHAT, MUSIC, ESPRIT)
- GPU acceleration for large-scale benchmarking
- Integration with autonomous aerial robots
- Real-world hardware validation using MEMS microphone arrays

---

# 📖 References

1. Knapp, C., & Carter, G. (1976). Generalized Correlation Method for Estimation of Time Delay.

2. Brandstein, M., & Ward, D. *Microphone Arrays: Signal Processing Techniques and Applications.*

3. SciPy Documentation

4. Librosa Documentation

5. NumPy Documentation

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

**Vedant Lohare**

Undergraduate Student  
Department of Aerospace Engineering  
Indian Institute of Technology Kanpur

---

# ⭐ Acknowledgements

This project was developed as part of preparation for the **IMAV 2025 Indoor Challenge** with the goal of building a modular and research-oriented acoustic source localization framework.

Special thanks to the open-source scientific Python community for the excellent ecosystem that made this project possible.

---

## If you found this repository useful

If this project helped you in your work or research, consider giving the repository a ⭐ on GitHub.

It helps others discover the project and motivates further development.
