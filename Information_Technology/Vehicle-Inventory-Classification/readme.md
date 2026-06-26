# Vehicle Inventory Classification #ComputerVision

![Cover](https://github.com/Dotto-Luis/Projects/blob/main/Information_Technology/Vehicle-Inventory-Classification/image.png?raw=true)

## Table of Contents

1. [Business Goal](#business-goal)
2. [About the Data](#about-the-data)
3. [Usage Examples](#usage-examples)
4. [Project Structure](#project-structure)
5. [Requirements](#requirements)
6. [Tests](#tests)
7. [Contributing](#contributing)
8. [License](#license)
9. [Project Origin](#project-origin)

---

## 1. Business Goal

A used car marketplace wants to automate vehicle identification from photos. Manually entering make and model for every car is time-consuming and error-prone. This project trains a CNN-based multi-class classifier to predict vehicle make and model from images across 25 different classes, targeting >80% accuracy on the test set.

Use case: auto-populate vehicle attributes when sellers upload car photos.

Tech stack: Python · TensorFlow · Keras · Matplotlib · Jupyter · Docker

---

## 2. About the Data

The dataset consists of JPG images organized into folders by label (vehicle make-model), split into train and test sets.

- **Classes**: 25 vehicle make-model combinations.
- **Format**: JPG images, folder structure = label.
- **Download**: automatically via the project notebook (`Section 1 - Getting the data`).

---

## 3. Usage Examples

**Option A — Virtual environment:**

```bash
pip install -r requirements.txt
jupyter notebook Vehicle-Inventory-Classification.ipynb
```

**Option B — Docker (CPU):**

```bash
docker build -t sp_04 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile .
docker run --rm --net host -it -v $(pwd):/home/app/src --workdir /home/app/src sp_04 bash
```

**Option B — Docker (GPU):**

```bash
docker build -t sp_04 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile_gpu .
docker run --rm --net host --gpus all -it -v $(pwd):/home/app/src --workdir /home/app/src sp_04 bash
```

> For GPU training on a free tier, use [Google Colab](https://colab.research.google.com) with Runtime → Change runtime type → GPU.

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── docker/
│   ├── Dockerfile
│   ├── Dockerfile.M1
│   └── Dockerfile_gpu
├── src/
│   └── models.py             # Model architecture (implement TODOs here)
├── tests/
│   └── test_models.py
├── Vehicle-Inventory-Classification.ipynb
├── image.png
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- TensorFlow · Keras
- matplotlib
- Jupyter
- black · isort (code formatting)

---

## 6. Tests

```bash
pytest tests/
```

---

## 7. Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Project Origin

Based on an AnyoneAI sprint project on deep learning and computer vision for vehicle classification.
