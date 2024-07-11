# Fintech-Advisor-Chatbot #NLP
 

![finance-chatbot](https://github.com/Dotto-Luis/Projects/assets/93018629/f0e76fac-972a-4505-bbaa-c883bdb9d6cb)


## Business Goal

The main goal of this project is to provide users a platform in which they can interact with a Chatbot assistant and make questions about finance over NASDAQ companies. 

For developing this kind of solution I will need first to extract all the text data from the provided dataset and store them in some platform that will allow you later to perform text searches to retrieve the most similar results from the user question. Then I will need to connect some Generative Models like GPT to take the retrieved text chunks and create a final answer for the user.



## About the data

The original dataset is composed of multiple files with different information about loans taken. In this project, we will work exclusively with the primary files: application_train_aai.csv and application_test_aai.csv.

You don't have to worry about downloading the data, it will be automatically downloaded from the AnyoneAI - Sprint Project 02.ipynb notebook in Section 1 - Getting the data.

These data comes from a project in [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/overview), and a Home Credit Compay calle [Home Credit](https://www.homecredit.net/)

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```console
├── dataset
│   ├── application_test_aai.csv
│   ├── application_train_aai.csv
│   ├── HomeCredit_columns_description.csv
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── data_utils.py
│   ├── preprocessing.py
└── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_data_utils.py
│   └── test_preprocessing.py
├── ASSIGNMENT.md
├── Home_credit_default_risk.ipynb
├── README.md
└── requirements.txt
```

## Requirement

- black==23.1.0
- flake8==6.0.0
- gdown==4.6.0
- isort==5.12.0
- Jupyter==1.0.0
- matplotlib==3.6.3
- numpy==1.24.2
- pandas==1.5.3
- pytest==7.2.1
- scikit-learn==1.2.1
- seaborn==0.12.2

```pip install -r requirements.txt```


## Project Origin

This project is based on a [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data) project.

I'd like to thank AnyoneAI for their contribution and inspiration in the development of this project.

