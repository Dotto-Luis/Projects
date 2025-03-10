# Ecommerce Performance Insights-Olist #EDA

![alt text](image.png)


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

This project is related to NLP. As you may already know, the most important and hardest part of an NLP project is pre-processing, which is why we are going to focus on that.

Basically this is a basic sentiment analysis problem, as in this case, consists of a classification problem, where the possible output labels are: `positive` and `negative`. Which indicates, if the review of a movie speaks positively or negatively. In our case it is a binary problem, but one could have many more "feelings" tagged and thus allow a more granular analysis.

## 2. About the data

In this project, we will work exclusively with two files: `movies_review_train_aai.csv` and `movies_review_test_aai.csv`.


This is a dataset for **binary sentiment classification**.

## 3. Usage Examples (wip)

## 4. Project Structure
<details>
  <summary>📂 Expand for Project Structure</summary>

  Here's a detailed overview of the project structure and each module inside:

```console
├── datasets
│   ├── movies_review_train_aai.csv
│   └── movies_review_test_aai.csv
├── images
│   └── Cover.png
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── plots.py
│   └── transform.py
└── test
│   ├── __init__.py
│   ├── query_results/
│   ├── test_extract.py
│   └── test_transform.py
├── Assigment.md
├── SentimentClassifier-MovieReviews.ipynb
├── Readme.md
└── Requirements.txt
```
</details>

## 5. Requirement
To set up the environment, install the necessary dependencies using:

``` bash
pip install -r requirements.txt
```

Here is the list of required packages:

- beautifulsoup4==4.12.2
- black[jupyter]==23.3.0
- flake8==6.0.0
- gdown==4.7.1
- gensim==4.3.1
- isort==5.12.0
- matplotlib==3.7.1
- nltk==3.8.1
- numpy==1.24.2
- pandas==2.0.0
- pytest==7.3.0
- scikit_learn==1.2.2
- spacy==3.5.2




## 6. Tests

We've added some basic tests to `AnyoneAI - Sprint Project 05.ipynb` that you must be able to run without errors in order to approve the project. If you encounter some issues in the path, make sure to be following these requirements in your code:

- Every time you need to run a tokenizer on your sentences, use `nltk.tokenize.toktok.ToktokTokenizer`.
- When removing stopwords, always use `nltk.corpus.stopwords.words('english')`.
- For Stemming, use `nltk.porter.PorterStemmer`.
- For Lematizer, use `Spacy` pre-trained model `en_core_web_sm`.

We provide unit tests along with the project that you can run and check from your side the code meets the minimum requirements of correctness needed to approve. To run just execute:

```console
$ pytest tests/
```

## 7. Contributing

We welcome contributions to this project. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## 8. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 9. Project Origin

This project is based on a [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) project.

I'd like to thank AnyoneAI for their contribution and inspiration in the development of this project.