# Fintech-Advisor-Chatbot #NLP
 

![finance-chatbot](https://github.com/Dotto-Luis/Projects/assets/93018629/f0e76fac-972a-4505-bbaa-c883bdb9d6cb)


## Business Goal

The main goal of this project is to provide users a platform in which they can interact with a Chatbot assistant and make questions about finance over NASDAQ companies. 

For developing this kind of solution I will need first to extract all the text data from the provided dataset and store them in some platform that will allow you later to perform text searches to retrieve the most similar results from the user question. Then I will need to connect some Generative Models like GPT to take the retrieved text chunks and create a final answer for the user.



## About the data

The provided dataset is a subset of the ones listed on the website www.annualreports.com. More specifically, our dataset is composed of public documents (Annual reports and 10-K statements) from the last 5 years from all the companies listed in the NASDAQ stock market (around 2600 companies).

The dataset can be found in AWS S3. To access the dataset you will have to use the boto3 library and here are the key and secret keys that you can use for read-only access.

- Dataset: s3://anyoneai-datasets/nasdaq_annual_reports/
- Key: AKIA2JHUK4EGBAMYAYFY

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```console
fchat/
│
├── api/                     # Code for the API that interacts with the chatbot
│   ├── Dockerfile            # Dockerfile for the API
│   ├── app.py                # Main API code
│   ├── middleware.py         # Middleware for the API
│   ├── views.py              # Views or routes for the API
│   ├── settings.py           # Configuration settings for the API
│   ├── utils.py              # Utility functions for the API
│   ├── templates/            # HTML templates for the UI
│   │   └── index.html        # Main template
│   └── tests/                # Unit tests for the API
│       ├── test_api.py       # API tests
│       └── test_utils.py     # Utility tests
│
├── model/                   # Code for the Natural Language Processing (NLP) model
│   ├── Dockerfile            # Dockerfile for the model
│   ├── ml_service.py         # Machine learning service code
│   ├── settings.py           # Configuration settings for the model
│   └── tests/                # Unit tests for the model
│       └── test_model.py     # Model tests
│
├── data/                    # Data related to the project
│   ├── raw/                 # Raw data (downloaded from S3)
│   └── processed/           # Processed data
│
├── notebooks/               # Jupyter notebooks for exploratory data analysis (EDA) and prototypes
│   └── exploratory_analysis.ipynb  # EDA notebook
│
├── scripts/                 # Utility scripts for data processing, training, etc.
│   ├── download_data.py      # Script for downloading data from AWS S3
│   ├── preprocess_data.py    # Script for preprocessing data
│   └── other_scripts.py      # Other useful scripts
│
├── stress_test/             # Stress tests for the API
│   └── locustfile.py         # Locust configuration file for load testing
│
├── ui/                      # Code for the user interface
│   ├── Dockerfile            # Dockerfile for the UI
│   ├── app.py                # Main UI code
│   └── templates/            # HTML/CSS/JS templates for the UI
│       └── index.html        # Main UI page
│
├── docker-compose.yml       # Docker Compose file for orchestrating containers
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies for the project

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

