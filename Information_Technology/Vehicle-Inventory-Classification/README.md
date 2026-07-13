# Vehicle Inventory Classification #ComputerVision

[![Tests](https://github.com/Dotto-Luis/Projects/actions/workflows/vehicle-inventory-tests.yml/badge.svg)](https://github.com/Dotto-Luis/Projects/actions/workflows/vehicle-inventory-tests.yml)

![Cover](images/cover.png)

## Table of Contents

1. [Business Goal](#1-business-goal)
2. [About the Data](#2-about-the-data)
3. [Usage Examples](#3-usage-examples)
4. [Project Structure](#4-project-structure)
5. [Requirements](#5-requirements)
6. [Tests](#6-tests)
7. [Results / Output](#7-results--output)
8. [License](#8-license)
9. [Project Origin](#9-project-origin)

---

## 1. Business Goal

A used car marketplace wants to automate vehicle identification from photos. Manually entering make and model for every car is time-consuming and error-prone. This project trains a CNN-based multi-class classifier to predict vehicle make and model from images across **25 classes**, targeting >80% accuracy on the test set.

The notebook walks through a deliberate model progression — the classic computer-vision escalation:

1. **MLP baseline** — flat dense layers, ignores spatial structure.
2. **LeNet CNN** — convolutions capture local patterns, trained from scratch.
3. **ResNet50 transfer learning** — ImageNet-pretrained backbone, frozen, with a new classification head.

---

## 2. About the Data

JPG images organized into folders by label (vehicle make-model), split into train and test sets.

- **Classes**: 25 vehicle make-model combinations.
- **Format**: JPG images, folder structure = label.
- **Download**: automatic via `src/data_utils.download_datasets()` (Google Drive) — also triggered from the notebook's Section 1.

---

## 3. Usage Examples

**Option A — Local environment (uses [uv](https://docs.astral.sh/uv/)):**

```bash
uv sync
uv run jupyter notebook Vehicle-Inventory-Classification.ipynb
```

**Option B — Docker (CPU):**

```bash
docker build -t vehicle_cnn --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile .
docker run --rm --net host -it -v $(pwd):/home/app/src --workdir /home/app/src vehicle_cnn bash
```

**Option C — Docker (GPU):**

```bash
docker build -t vehicle_cnn_gpu --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile_gpu .
docker run --rm --net host --gpus all -it -v $(pwd):/home/app/src --workdir /home/app/src vehicle_cnn_gpu bash
```

> For GPU training on a free tier, use [Google Colab](https://colab.research.google.com) with Runtime → Change runtime type → GPU. On Apple Silicon, see `docker/Dockerfile.M1`.

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── docker/
│   ├── Dockerfile                # CPU training environment
│   ├── Dockerfile.M1             # Apple Silicon variant
│   └── Dockerfile_gpu            # CUDA training environment
├── src/
│   ├── config.py                 # Dataset paths and download URL
│   ├── data_utils.py             # Dataset download + extraction
│   └── models.py                 # MLP, LeNet and ResNet50 builders
├── tests/
│   └── test_models.py            # Architecture tests (offline, no weights)
├── Vehicle-Inventory-Classification.ipynb
├── pyproject.toml                # Dependencies (managed with uv)
├── uv.lock
└── README.md
```
</details>

---

## 5. Requirements

Managed with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Key dependencies: tensorflow · scikit-learn · matplotlib · gdown

---

## 6. Tests

```bash
uv run pytest tests -v
```

14 architecture tests validate the three model builders: input/output shapes, layer counts, and activations. They build the models with `weights=None`, so no ImageNet download or dataset is needed — fully offline, CI-safe.

---

## 7. Results / Output

Validation accuracy by model — the progression tells the story:

| Model | Train acc. | Validation acc. |
|---|---|---|
| MLP baseline | 0.65 | 0.30 |
| LeNet (from scratch) | 0.85 | 0.32 |
| **ResNet50 (transfer learning)** | 0.97 | **0.74** |

Training from scratch overfits badly on a small dataset (LeNet: 85% train vs 32% validation). Reusing ImageNet features via transfer learning more than doubles validation accuracy — the standard result that makes pre-trained backbones the default choice for small image datasets. The notebook closes with a confusion matrix and per-class classification report for the ResNet50 model.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Project Origin

Based on an AnyoneAI sprint project on CNN image classification. Extended with offline-safe architecture tests and uv-managed dependencies.
