# ReviewRatingModel-Amazon #NLP

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

## 1. Business Goal

The objective of this project is to build a **multilingual text classification model** using Amazon product reviews. The model will analyze written product reviews and **predict the corresponding star rating (1-5 stars)**. 

This problem can be approached as either:
- **Classification:** Assigning each review to one of five discrete rating categories.
- **Regression:** Predicting a continuous rating score.

Through this project, we aim to explore different modeling approaches and assess the impact of NLP preprocessing, feature engineering, and model selection.

## 2. About the Data

This project uses the **Multilingual Amazon Reviews Corpus**, a dataset provided by **AWS Open Data**. It contains product reviews across multiple languages from **November 2015 to November 2019**.

### **Dataset Details**
- **Source:** [AWS Open Data - Amazon Reviews](https://docs.opendata.aws/amazon-reviews-ml/readme.html)
- **Languages:** English, Spanish, German, French, Japanese, and others.
- **Features:**
  - `review_id`: Unique ID for each review.
  - `product_id`: Anonymized product identifier.
  - `review_title`: Title of the review.
  - `review_body`: Full text of the review.
  - `star_rating`: Target variable (1-5 stars).
  - `language`: Language of the review.
  - `product_category`: High-level product classification.

## 3. Usage Examples (WIP)

## 4. Project Structure
<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── datasets
│   ├── amazon_reviews_train.csv
│   └── amazon_reviews_test.csv
├── images
│   └── Cover.png
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── test
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_model.py
│   └── test_pipeline.py
├── notebooks
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│   ├── Model_Evaluation.ipynb
├── README.md
├── requirements.txt
└── LICENSE
```
</details>

## 5. Requirement
To set up the environment, install the necessary dependencies using:

``` bash
pip install -r requirements.txt
```

Here is the list of required packages:

- Jupyter==1.0.0
- matplotlib==3.6.2
- pandas==1.5.2
- seaborn==0.11.2
- scikit-learn==1.2.1
- nltk==3.8.1
- re =2023.8.8

## 6. Tests

Basic unit tests are included to ensure proper functionality of preprocessing, model training, and evaluation.

Run tests with:

```console
$ pytest tests/
```

## 7. Contributing

I welcome contributions to this project. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## 8. License

By accessing the **Multilingual Amazon Reviews Corpus** ("Reviews Corpus"), you agree to the [Amazon Conditions of Use](https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088).


## 9. Project Origin

This project is based on a [AWS](https://docs.opendata.aws/amazon-reviews-ml/readme.html) dataset.
