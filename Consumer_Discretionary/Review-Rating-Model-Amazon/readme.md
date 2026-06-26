# 🧠 ReviewRatingModel-Amazon #NLP

![image](https://user-images.githubusercontent.com/76250515/127223678-2b9938d2-a9ea-4eb8-b698-70ee804540ac.png)

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

This project applies Natural Language Processing (NLP) to predict **Amazon product review ratings (1–5 stars)** based solely on written text. By analyzing linguistic patterns, it uncovers how customers express satisfaction or frustration and how sentiment correlates with rating intensity.

The analytical workflow includes:
- Text preprocessing with **spaCy** (lemmatization, stopword removal, normalization).
- Feature extraction using **TF-IDF vectorization**.
- Model training with **Logistic Regression** and evaluation through a confusion matrix and F1-score metrics.

---

## 2. About the Data

The dataset originates from the **Amazon Product Data (UCSD)**, derived from the [SASRec repository](https://github.com/kang205/SASRec). It includes thousands of **Spanish-language reviews** of beauty products, containing reviewer, product, rating, and text fields.

---

## 3. Usage Examples

### Key Results

- Achieved **~65% accuracy** in predicting review ratings.
- Strong performance for 5-star reviews; more overlap between 2–4 star classes.
- Clear correspondence between **emotional tone and numeric rating**.
- Word frequency analysis reveals distinct emotional vocabularies:
  - Negative: *disappointed, waste, return, awful*
  - Positive: *love, great, perfect, amazing*

| Visualization | Description |
|----------------|-------------|
| ![chart1](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Confusion_Matrix.png?raw=true) | Model confusion matrix showing clear separation for positive classes. |
| ![chart](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Top_great.png?raw=true) | Word frequency contrast — positive reviews. |
| ![chart](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Top_bad.png?raw=true) | Word frequency contrast — negative reviews. |

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── images/
│   ├── Results_Confusion_Matrix.png
│   ├── Results_Top_great.png
│   └── Results_Top_bad.png
├── ReviewRatingModel-Amazon.ipynb
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Tech stack: Python · Pandas · Scikit-learn · spaCy · Matplotlib · Seaborn · Jupyter

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
Dataset adapted from [Amazon Product Data – UCSD](https://jmcauley.ucsd.edu/data/amazon/).

---

## 9. Project Origin

Based on the [Amazon Product Data](https://jmcauley.ucsd.edu/data/amazon/) dataset by UCSD, derived from the [SASRec repository](https://github.com/kang205/SASRec).

<p align="center">
  <img src="https://raw.githubusercontent.com/Dotto-Luis/Dotto-Luis/main/signature.png" width="280"/>
</p>
