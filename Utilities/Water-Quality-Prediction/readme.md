# Water Quality Prediction #ML

![Cover](assets/project_cover.png)

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

Water quality monitoring is critical for environmental management and public health, but collecting samples across large geographic areas is expensive and time-consuming. This project builds a machine learning model that predicts river water quality using environmental signals from satellite imagery, climate variables, and spatiotemporal features.

**Target variables** (multi-target regression):
- Total Alkalinity
- Electrical Conductance
- Dissolved Reactive Phosphorus

**Evaluation metric**: average R² across all three targets.

**Best models tested**: Random Forest, Gradient Boosting, LightGBM.

**Benchmark results**:
- Total Alkalinity R² ≈ 0.54
- Electrical Conductance R² ≈ 0.58
- Dissolved Reactive Phosphorus R² ≈ 0.53

---

## 2. About the Data

The dataset combines field water quality measurements with satellite and climate signals.

**Water Quality Dataset** — field samples (2011–2015) from rivers across South Africa:
- Latitude, Longitude, Date
- Total Alkalinity, Electrical Conductance, Dissolved Reactive Phosphorus

**Satellite Features (Landsat)**: nir, green, swir16, swir22, NDMI, MNDWI

**Climate Features (TerraClimate)**: PET (Potential Evapotranspiration)

**Engineered features** include seasonal indicators, spectral band ratios, and interaction terms (e.g., `water_stress_index = NDMI * PET`).

---

## 3. Usage Examples

Run notebooks in order:

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
jupyter notebook notebooks/02_feature_engineering.ipynb
jupyter notebook notebooks/03_model_training.ipynb
```

Final predictions are exported to `submissions/submission.csv`.

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
├── submissions/
│   └── submission.csv
├── assets/
│   └── project_cover.png
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- pandas · numpy
- scikit-learn · lightgbm
- matplotlib · seaborn
- jupyter

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

Based on a research dataset combining Landsat satellite imagery and TerraClimate data with field water quality measurements from South African rivers.
