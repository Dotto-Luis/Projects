#  LLM-Powered Apps Final Project

## The Business problem

This project is related to LLMs. You want to create an app that is able to take a person's profile and look for job oportunities that would match it.

## About the data

In this project, we will work exclusively with a file `jobs.csv`.

You don't have to worry about downloading the data, it is already present in the dataset folder.

This is a dataset for **creating a job-searching app**.

## Technical aspects

To develop this Machine Learning model you can use the README.md. This file will guide you through all the steps you have to follow and the code you have to complete in the different parts of the project, also marked with a `TODO` comment.

## Install

A `requirements.txt` file is provided with all the needed Python libraries for running this project. For installing the dependencies just run:
```bash
$ pip install -r requirements.txt
```

*Note:* We encourage you to install those inside a virtual environment.

## Configuration

This project supports both OpenAI and Google Gemini as LLM providers. Configure your preferred provider in the `.env` file:
```bash
# Choose provider: "openai" or "gemini"
LLM_PROVIDER="openai"

# OpenAI settings
OPENAI_LLM_MODEL="gpt-4o-mini"
OPENAI_API_KEY="your-openai-api-key-here"

# Gemini settings
GEMINI_LLM_MODEL="gemini-2.5-flash"
GOOGLE_API_KEY="your-google-api-key-here"

LANGCHAIN_VERBOSE=true
```

You can switch between providers by changing the `LLM_PROVIDER` value in your `.env` file.

## Run Project

To run the ETL pipeline and create a chroma vector database once you finish completing the code, run:
```bash
$ python backend/etl.py
```

## Run Project

In order to execute the project you need to launch a Chainlit server running:
```bash
$ python -m chainlit run -w backend/app.py
```

## Code Style

Following a style guide keeps the code's aesthetics clean and improves readability, making contributions and code reviews easier. Automated Python code formatters make sure your codebase stays in a consistent style without any manual work on your end. If adhering to a specific style of coding is important to you, employing an automated to do that job is the obvious thing to do. This avoids bike-shedding on nitpicks during code reviews, saving you an enormous amount of time overall.

We use [Black](https://black.readthedocs.io/) for automated code formatting in this project, you can run it with:
```console
$ black --line-length=88 .
```

Wanna read more about Python code style and good practices? Please see:
- [The Hitchhiker's Guide to Python: Code Style](https://docs.python-guide.org/writing/style/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Tests

We've added some basic tests for the backend service:

- test_utils.py for utils.py.
- test_chatgpt_clone.py for chatgpt_clone.py.
- test_job_finder_agent.py for job_finder_agent.py.

To run just execute:
```bash
$ python -m pytest tests
```

If you want to learn more about testing Python code, please read:
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [The Hitchhiker's Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)


## Structure to be completed

WEEK 1:

DAY 1:

- Get all the requirements installed in a virtual env and the chainlit app running.
- Complete the function extract_text_from_pdf() at backend/utils.py.
    - Use PyPDF2.PdfReader to open the input `pdf_bytes` and extract the text from each page appended to `pdf_text`.

DAY 2:

- Complete the code for the class ChatAssistant() at backend/models/chatgpt_clone.py:
    - Create a string template for the chat assistant.
    - Create a prompt template using the string template created above.
    - Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
    - Create an instance of `langchain.chains.LLMChain` with the appropriate settings.

WEEK 2:

DAY 1:

- Complete the code for the ETLProcessor() class at backend/etl.py.
    - Create a text splitter using the `langchain.text_splitter.RecursiveCharacterTextSplitter` class.
    - Load the dataset from the `dataset_path` using the `pandas.read_csv()` function.
- Run ingestion/etl.py to create the initial dataset with vector embeddings.

DAY 2:

- Complete the code for the JobsFinderAssistant() class at backend/models/jobs_finder.py.
    - Create a string template for the chat assistant.
    - Create a prompt template using the string template created above.
    - Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
    - Create an instance of `langchain.chains.LLMChain` with the appropriate settings.
    - Use the human input and the user resume summary to search for jobs.

WEEK 3:

DAY 1:
- Complete the missing elements in backend/models/resume_summarizer_chain.py. This creates a summarized resume chain for backend/models/jobs_finder.py.
    - Create a string template for this chain.
    - Create a prompt template using the string template created above.
    - Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
    - Create an instance of `langchain.chains.LLMChain` with the appropriate settings.


DAY 2:
- Complete the function build_cover_letter_writing() at backend/models/jobs_finder_agent.py.
    - Create a string template for this chain.
    - Create a prompt template using the string template created above.
    - Create an instance of `langchain.chains.LLMChain` with the appropriate settings.
- Take the profile + job found and make a personalized message to the recruiter.

## LLM Provider Support

This project uses a factory pattern (`backend/llm_factory.py`) to support multiple LLM providers. The `get_llm()` function automatically selects the appropriate provider based on your `.env` configuration, allowing you to seamlessly switch between OpenAI and Google Gemini without changing your code.