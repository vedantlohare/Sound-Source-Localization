# 🎯 Sound Source Localization using GCC-PHAT

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge\&logo=docker)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge\&logo=numpy)
![SciPy](https://img.shields.io/badge/SciPy-Optimization-8CAAE6?style=for-the-badge\&logo=scipy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Research-grade 3D acoustic source localization framework using **Generalized Cross Correlation with Phase Transform (GCC-PHAT)**, **Time Difference of Arrival (TDoA)** estimation, and **nonlinear least-squares optimization**.

Developed for the **IMAV 2025 Indoor Challenge** with an emphasis on modular software architecture, reproducibility, benchmarking, and visualization.

</p>

---

## ✨ Features

* 🎤 Physics-based four-microphone array simulation
* 📡 Automatic TDoA estimation using GCC-PHAT
* 📍 3D source localization with nonlinear optimization
* 📊 Benchmark framework with statistical evaluation
* 📈 Automatic visualization and report generation
* 🐳 Docker support for reproducible execution
* 🧪 Synthetic and real-audio validation tests
* ⚙️ Config-driven architecture for easy experimentation

---

## 🏗 Pipeline

```text
True Source Position
        │
        ▼
Microphone Simulation
        │
        ▼
Generate Microphone Recordings
        │
        ▼
GCC-PHAT
        │
        ▼
Automatic TDoA Estimation
        │
        ▼
Nonlinear Least Squares Localization
        │
        ▼
Estimated Position
        │
   ┌────┴────┐
   ▼         ▼
Evaluation  Visualization
```

---

## 📁 Repository Structure

```text
Sound-Source-Localization/

├── algorithms/
├── benchmark/
├── configs/
├── data/
│   ├── original/
│   └── generated/
├── results/
├── simulation/
├── tests/
├── visualization/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

---

## 🚀 Quick Start

### Docker (Recommended)

```bash
git clone https://github.com/<YOUR_USERNAME>/Sound-Source-Localization.git

cd Sound-Source-Localization

docker compose up --build
```

The pipeline automatically performs:

* Microphone simulation
* GCC-PHAT processing
* Automatic TDoA estimation
* Source localization
* Evaluation
* Visualization

---

### Native Installation

```bash
pip install -r requirements.txt

python main.py
```

Run the benchmark suite:

```bash
python -m benchmark.benchmark
```

---

## 📊 Output

The framework automatically generates:

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

---

## 🔬 Algorithm Overview

The localization pipeline consists of four major stages.

### 1. Microphone Simulation

A configurable tetrahedral microphone array is simulated. Given a known source position, propagation distances and arrival times are computed to generate synchronized microphone recordings with fractional delays.

### 2. GCC-PHAT

Pairwise microphone recordings are processed using GCC-PHAT to estimate robust Time Differences of Arrival (TDoAs). Phase normalization improves delay estimation under varying signal amplitudes.

### 3. Source Localization

The measured TDoAs are supplied to a nonlinear least-squares optimizer that estimates the three-dimensional source position.

### 4. Evaluation

Since the simulator knows the true source position, the framework automatically computes localization error, confidence, runtime, and benchmark statistics.

---

## 📈 Benchmarking

The benchmark framework repeatedly executes the complete localization pipeline using randomly generated source positions.

For every trial it records:

* True source position
* Estimated source position
* Euclidean localization error
* Confidence score
* Execution time

The benchmark automatically generates:

* CSV reports
* Summary statistics
* Error histogram
* Confidence histogram
* Runtime histogram

---

## 📸 Example Results

After executing the pipeline, replace the placeholders below with screenshots from your repository.

### 3D Localization

```text
docs/images/localization_scene.png
```

### Error Distribution

```text
docs/images/error_histogram.png
```

### Confidence Distribution

```text
docs/images/confidence_histogram.png
```

---

## 🧪 Testing

Run synthetic validation:

```bash
python -m tests.test_gcc
```

Run real-audio validation:

```bash
python -m tests.test_real_audio
```

Run the complete localization pipeline:

```bash
python main.py
```

Run the benchmark:

```bash
python -m benchmark.benchmark
```

---

## 🚀 Future Work

* Real-time localization using live microphone arrays
* ROS 2 integration
* Multi-source localization
* Alternative localization algorithms (SRP-PHAT, MUSIC, ESPRIT)
* GPU acceleration
* Hardware validation using MEMS microphone arrays
* UAV integration for autonomous acoustic navigation

---

## 📚 References

1. Knapp, C., & Carter, G. (1976). *The Generalized Correlation Method for Estimation of Time Delay.*

2. Brandstein, M., & Ward, D. *Microphone Arrays: Signal Processing Techniques and Applications.*

3. SciPy Documentation

4. NumPy Documentation

5. Librosa Documentation

---

## 👨‍💻 Author

**Vedant Lohare**

B.Tech., Aerospace Engineering
Indian Institute of Technology Kanpur

---

⭐ If you found this repository useful, consider giving it a star on GitHub.
