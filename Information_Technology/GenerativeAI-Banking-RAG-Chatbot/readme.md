# GenerativeAI-Banking-RAG-Chatbot

![image](https://raw.githubusercontent.com/Dotto-Luis/Projects/refs/heads/main/Information_Technology/HuggingFace-LangChain-Chatbot/images/cover.png)

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

### 1. Business Goal

The goal of this project is to build a smart **banking assistant** that can answer questions in natural language about banking documents (PDFs), such as account terms or fee policies.  
The system leverages:

- **Local Generative AI model (StableLM)**
- **RAG (Retrieval-Augmented Generation) technique**
- **Semantic embeddings via Hugging Face**

This assistant can be integrated into internal tools or customer-facing applications to enhance operational efficiency in the financial sector.

---

## 2. About the Data

This project uses **publicly available banking documents**, such as:

- Account terms and conditions
- Product manuals
- Legal documents (PDFs from real bank websites like BBVA or Santander)

### Dataset Details:

- Format: PDF
- Processing: text is extracted and chunked into 500-character blocks
- Embeddings generated using Hugging Face models

---

## 3. Usage Examples (WIP)

### 🧠 Example Question:  
**"What are the requirements to open a commission-free account?"**

### ⚙️ Example Model Response (StableLM + RAG):  
> “To avoid commissions, the customer must direct deposit income and meet basic requirements such as maintaining a monthly average balance.”

*The model retrieves relevant document chunks and generates a human-like response.*

---

## 4. Project Structure
<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── data
│   └── Spain_unicaja_Fixed_Mortage.pdf
├── images
│   └── cover.png
├── src
│   ├── loader.py            # PDF loading and chunking
│   ├── embeddings.py        # Vectorization using Hugging Face
│   ├── rag_chain.py         # RAG pipeline
│   ├── prompts.py           # Custom prompt templates
├── app
│   └── chatbot_interface.py # Streamlit or API interface
├── notebooks
│   └── Exploratory_Testing.ipynb
├── readme.md
├── requirements.txt
└── LICENSE
```
</details>

---

## 5. Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt

```

- Jupyter==1.0.0
- matplotlib==3.6.2
- pandas==1.5.2
- seaborn==0.11.2
- scikit-learn==1.2.1
- nltk==3.8.1
- re =2023.8.8

## 6. Tests

Basic unit tests are included to verify:

- PDF loading and splitting

- Chunk structure and vectorization

- Response quality from the RAG pipeline

```
pytest tests/
```

## 7. Contributing

Contributions are welcome. To contribute:

1. Fork the repository

2. Create a new branch: feature/your-feature

3. Commit your changes: git commit -am 'Add new feature'

4. Push to GitHub: git push origin feature/your-feature

5. Open a Pull Request with a clear description

## 8. License
This project is licensed under the MIT License. See LICENSE for details.

## 9. Project Origin

This project was inspired by Real-world applications of Generative AI in banking