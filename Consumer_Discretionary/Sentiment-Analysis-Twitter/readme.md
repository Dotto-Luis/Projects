# SentimentAnalysis-Twitter #NLP

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

This project focuses on **sentiment analysis of Twitter posts** to classify tweets as **positive, negative, or neutral**. The goal is to extract valuable insights from social media, helping businesses, researchers, and policymakers understand public sentiment.  

### **Key Objectives:**
- Preprocess and clean Twitter data (handling emojis, hashtags, and user mentions).
- Vectorize text data using **TF-IDF** or **word embeddings**.
- Train a **machine learning model** to classify tweet sentiments.
- Evaluate performance and visualize sentiment trends.

---

## 2. About the Data

The dataset consists of **labeled tweets** used for sentiment analysis. Each tweet is classified into one of three categories:

- **Positive (1)**: The tweet expresses a positive sentiment.
- **Negative (0)**: The tweet expresses a negative sentiment.
- **Neutral (2)**: The tweet does not express a strong opinion.

### **Dataset Details:**
- **Source**: [Kaggle - Twitter Sentiment Analysis](https://www.kaggle.com/code/paoloripamonti/twitter-sentiment-analysis)
- **Features**:
  - `tweet_id`: Unique identifier for each tweet.
  - `text`: The tweet's content.
  - `sentiment`: The sentiment label (positive, negative, neutral).
  - `date`: The date the tweet was posted.
  - `hashtags`: List of hashtags used in the tweet.

  ---

## 3. Usage Examples

### 1️⃣ Load and Preprocess Tweets
```python
from src.preprocessing import clean_tweet

tweet = "I love #AI and #MachineLearning! 😃🔥 @user123"
cleaned_tweet = clean_tweet(tweet)
print(cleaned_tweet)  # Output: "i love ai and machinelearning"
```

### 2️⃣ Convert Tweets to Features (TF-IDF)

```python
from src.vectorization import vectorize_text

sample_tweets = ["Great service! Will buy again!", "This product is terrible..."]
features = vectorize_text(sample_tweets)
print(features.shape)  # Output: (2, N) where N is the number of features

```

### 3️⃣ Predict Tweet Sentiment

```python
from src.model import load_model, predict_sentiment

# Load trained model
model = load_model("models/twitter_sentiment_model.pkl")

# Predict sentiment
prediction = predict_sentiment(model, ["Worst experience ever!"])
print(prediction)  # Output: ["negative"]

```

## 4. Project Structure
<details>
  <summary>📂 Expand for Project Structure</summary>

  Here's a detailed overview of the project structure and each module inside:

```console
├── datasets
│   ├── twitter_train.csv
│   └── twitter_test.csv
├── images
│   └── Cover.png
├── src
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── vectorization.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── test
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_model.py
│   ├── test_pipeline.py
├── notebooks
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│   ├── Model_Evaluation.ipynb
├── Readme.md
├── Requirements.txt
└── License
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
- tweepy==4.10.1
- regex==2023.8.8


## 6. Tests

Basic unit tests are included to validate preprocessing, model training, and predictions.

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 9. Project Origin

This project is based on a [Kagle](https://www.kaggle.com/code/paoloripamonti/twitter-sentiment-analysis) project.