# OpenAI-Agent-Toolkit

![Cover](https://github.com/Dotto-Luis/Projects/blob/main/Information_Technology/OpenAI-Agent-Toolkit/assets/OpenAI-Agent-Toolkit.png?raw=true)

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

The goal of this project is to build an **autonomous AI agent** using the **OpenAI API**, capable of planning and executing tasks based on natural language goals.

This project showcases a modular, extensible agent architecture that demonstrates:

* Task decomposition and planning
* Memory management
* Iterative reasoning via a reasoning loop
* Tool use and function calling

The toolkit is designed for experimentation, education, and as a starting point for real-world autonomous agent applications.

---

## 2. About the Data

This project does not rely on traditional datasets. Instead, it simulates task inputs and goals defined by the user, which the agent must deconstruct and act upon.

Examples of goals given to the agent:

* "Find the 3 most recent AI papers on arXiv and summarize them."
* "Generate a 3-day travel itinerary for Tokyo."
* "Get the weather forecast and suggest a suitable outfit."

The agent interacts with mock or real tools/APIs to fulfill the tasks.

---

## 3. Usage Examples

Run the agent with a goal:

```bash
pip install -r requirements.txt
python main.py --goal "Research the top 3 Python libraries for data visualization and explain their pros and cons."
```

### Example Goal

**"Research the top 3 Python libraries for data visualization and explain their pros and cons."**

### Example Agent Output

> "After researching, here are the top 3 libraries: 1. Matplotlib (most flexible, but verbose), 2. Seaborn (simplifies statistical plotting), 3. Plotly (interactive, great for dashboards)."

The agent completed this via web search, summarization, and multi-step reasoning.

Other example goals you can try:

```
"Find the 3 most recent AI papers on arXiv and summarize them."
"Generate a 3-day travel itinerary for Tokyo."
"Get the weather forecast for Buenos Aires and suggest a suitable outfit."
```

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── data/
├── notebooks/
├── src/
│   ├── agent/                 # Core agent logic and loop
│   └── utils/                 # Helper functions and utilities
├── tests/                    # Unit tests
├── assets/                   # Diagrams, supporting visuals
├── README.md
├── requirements.txt
├── .gitignore
├── cover.png
```

</details>

---

## 5. Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

Dependencies include:

* openai
* python-dotenv
* tiktoken
* requests
* pytest (for testing)

---

## 6. Tests

Basic unit tests verify:

* Agent initialization
* Task planning logic
* Tool execution flow

Run tests using:

```bash
pytest tests/
```

---

## 7. Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a new branch: `feature/your-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to GitHub: `git push origin feature/your-feature`
5. Open a Pull Request with a clear description

---

## 8. License

This project is licensed under the MIT License. See LICENSE for details.

---

## 9. Project Origin

This project was inspired by the guide: [Building an AI Agent using OpenAI API](https://amanxai.com/2025/04/29/building-an-ai-agent-using-openai-api/), which outlines a simple autonomous agent capable of executing multi-step tasks.
