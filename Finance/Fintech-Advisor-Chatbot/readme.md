# Fintech Advisor Chatbot #NLP

![Cover](https://github.com/Dotto-Luis/Projects/assets/93018629/f0e76fac-972a-4505-bbaa-c883bdb9d6cb)

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

The goal of this project is to provide users a platform to interact with a chatbot assistant and ask questions about NASDAQ-listed companies using their public financial documents.

The system:
1. Extracts text from annual reports and 10-K filings.
2. Stores chunks in a vector database for semantic search.
3. Connects to a Generative Model (GPT) to retrieve relevant context and generate accurate answers.

---

## 2. About the Data

The dataset is a subset of documents from [annualreports.com](https://www.annualreports.com), composed of public Annual Reports and 10-K statements from the last 5 years across all ~2,600 NASDAQ-listed companies.

Dataset location: `s3://anyoneai-datasets/nasdaq_annual_reports/`

---

## 3. Usage Examples

Launch the chatbot UI:

```bash
docker-compose up --build
```

Then navigate to `http://localhost` and start asking questions like:

> "What was NVIDIA's revenue growth in 2023?"

> "What are the main risk factors disclosed by Apple?"

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
fchat/
├── api/                          # Chatbot API
│   ├── Dockerfile
│   ├── app.py
│   ├── middleware.py
│   ├── views.py
│   ├── settings.py
│   ├── utils.py
│   ├── templates/
│   │   └── index.html
│   └── tests/
│       ├── test_api.py
│       └── test_utils.py
├── model/                        # NLP model service
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── settings.py
│   └── tests/
│       └── test_model.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   ├── download_data.py
│   └── preprocess_data.py
├── stress_test/
│   └── locustfile.py
├── ui/
│   ├── Dockerfile
│   ├── app.py
│   └── templates/
│       └── index.html
├── docker-compose.yml
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

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

---

## 6. Tests

```bash
pytest api/tests/
pytest model/tests/
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

Inspired by real-world RAG applications in financial services. Thanks to AnyoneAI for their contribution and inspiration.
