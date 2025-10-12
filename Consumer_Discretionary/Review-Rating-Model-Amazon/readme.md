# 🧠 ReviewRatingModel-Amazon #NLP

![image](https://user-images.githubusercontent.com/76250515/127223678-2b9938d2-a9ea-4eb8-b698-70ee804540ac.png)

## 1. Business Context
This project applies Natural Language Processing (NLP) to predict **Amazon product review ratings (1–5 stars)** based solely on written text.  
By analyzing linguistic patterns, it uncovers how customers express satisfaction or frustration and how sentiment correlates with rating intensity.

## 2. Data & Methods
The dataset originates from the **Amazon Product Data (UCSD)**, derived from the [SASRec repository](https://github.com/kang205/SASRec).  
It includes thousands of **Spanish-language reviews** of beauty products, containing reviewer, product, rating, and text fields.  

The analytical workflow includes:
- Text preprocessing with **spaCy** (lemmatization, stopword removal, normalization).  
- Feature extraction using **TF-IDF vectorization**.  
- Model training with **Logistic Regression** and evaluation through a confusion matrix and F1-score metrics.  

## 3. Key Results
- Achieved **~65% accuracy** in predicting review ratings.  
- Strong performance for 5-star reviews; more overlap between 2–4 star classes.  
- Clear correspondence between **emotional tone and numeric rating**.  
- Word frequency analysis reveals distinct emotional vocabularies:
  - Negative: *disappointed, waste, return, awful*  
  - Positive: *love, great, perfect, amazing*

| Visualization | Description |
|----------------|-------------|
| ![chart1](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Confusion_Matrix.png?raw=true) | Model confusion matrix showing clear separation for positive classes. |
| ![chart](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Top_great.png?raw=true) | Word frequency contrast - positive reviews. |
| ![chart](https://github.com/Dotto-Luis/Projects/blob/main/Consumer_Discretionary/Review-Rating-Model-Amazon/images/Results_Top_bad.png?raw=true) | Word frequency contrast - negative reviews. |


## 4. Tech Stack
Python · Pandas · Scikit-learn · spaCy · Matplotlib · Seaborn · Jupyter

## 5. License
MIT License.  
Dataset adapted from [Amazon Product Data – UCSD](https://jmcauley.ucsd.edu/data/amazon/).

<p align="center">
  <img src="https://raw.githubusercontent.com/Dotto-Luis/Dotto-Luis/main/signature.png" width="280"/>
</p>
