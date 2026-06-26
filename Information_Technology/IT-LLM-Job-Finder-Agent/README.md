# IT LLM Job Finder Agent #AIAgents

![Cover](https://github.com/Dotto-Luis/Projects/blob/main/Information_Technology/IT-LLM-Job-Finder-Agent/assets/cover.png?raw=true)

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

This project builds an LLM-powered job-matching agent that takes a candidate's profile (resume) and automatically finds job opportunities that match their skills, experience, and preferences.

The system uses:
- **RAG (Retrieval-Augmented Generation)** to search a job database semantically.
- **LangChain** for chaining LLM calls (resume summarizer → job finder → cover letter writer).
- **ChromaDB** for vector storage of job embeddings.
- **Chainlit** for an interactive chat interface.
- Supports **OpenAI** and **Google Gemini** as LLM providers.

---

## 2. About the Data

The project uses `dataset/jobs.csv` — a CSV file containing job listings with fields such as title, company, description, requirements, and location. The ETL pipeline processes this file into a ChromaDB vector database for semantic job search.

---

## 3. Usage Examples

**1. Configure your LLM provider in `.env`:**

```bash
LLM_PROVIDER="openai"             # or "gemini"
OPENAI_API_KEY="your-key-here"
OPENAI_LLM_MODEL="gpt-4o-mini"
```

**2. Run the ETL pipeline (build vector DB):**

```bash
python backend/etl.py
```

**3. Launch the Chainlit chat interface:**

```bash
python -m chainlit run -w backend/app.py
```

Then upload your resume and ask: *"Find me jobs that match my profile."*

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── backend/
│   ├── app.py                        # Chainlit app entry point
│   ├── etl.py                        # ETL pipeline: CSV → ChromaDB
│   ├── llm_factory.py                # LLM provider factory (OpenAI/Gemini)
│   ├── utils.py                      # PDF text extraction utilities
│   └── models/
│       ├── chatgpt_clone.py          # General chat assistant
│       ├── jobs_finder.py            # Job matching assistant
│       ├── jobs_finder_agent.py      # Cover letter writer agent
│       └── resume_summarizer_chain.py
├── dataset/
│   └── jobs.csv
├── chroma/                           # ChromaDB vector store
├── tests/
│   ├── test_utils.py
│   ├── test_chatgpt_clone.py
│   └── test_job_finder_agent.py
├── .env.example
├── requirements.txt
└── README.md
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- langchain · openai · google-generativeai
- chromadb · chainlit
- pandas · PyPDF2
- black (code formatting)

---

## 6. Tests

```bash
python -m pytest tests
```

Tests cover: utilities, chat assistant, and job finder agent modules.

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

Final project from an LLM-Powered Apps course by AnyoneAI. Extended with multi-provider support (OpenAI and Google Gemini) via a factory pattern architecture.
