# Sprint Planning

## Week 01

During the first week you will get a general overview of the main concepts and tools you will need to kickstart the Sprint project from day 1.

### Lesson 01

- Theory: 20.1 - Basics of Large Language Models (LLMs)
- Practice: 20.1 - Basic LLM.ipynb
- Sprint project:
    - Get all the requirements installed in a virtual env and the chainlit app running.
    - Complete function extract_text_from_pdf() at backend/utils.py.

### Lesson 02

- Theory: 20.2 - Prompt Engineering
- Practice: 20.2 - Prompt Engineering.ipynb
- Sprint project:
    - Complete the code for the class ChatAssistant() at backend/models/chatgpt_clone.py (We should modify the code for app.py so we can let the user load different assistant models).

## Week 02

In the second week we will introduce only a new concept, `Information Retrieval`, and then focus on the Sprint project.

### Lesson 01

- Theory: 20.3 - Information Retrieval, Embeddings, Chunking
- Practice: 20.3.a - Vector Databases, Retrieval, Embeddings.ipynb
- Sprint project:
    - Complete the code for the ETLProcessor class at backend/etl.py.
    - Run ingestion/etl.py to create the initial dataset with vector embeddings.

### Lesson 02

- Theory: 20.3 - Information Retrieval, Embeddings, Chunking
- Practice: 20.3.b - Chunking.ipynb
- Sprint project:
    - Complete the code for the JobsFinderAssistant() class at backend/models/jobs_finder.py. This class should consume the jobs from the database we've created in the previous lesson.

## Week 03

In the third week we will introduce the last concept, `Tools, Agents and Chat Memory`, and then focus on the Sprint project.

### Lesson 01

- Theory: 20.4 - Tools, Agents and Chat Memory
- Practice: 20.4.a - Tools and Agents.ipynb
- Sprint project:
    - Complete the missing elements in backend/models/resume_summarizer_chain.py. This creates a summarized rsume chain for backend/models/jobs_finder.py.
      
### Lesson 02

- Theory: -
- Practice: 20.4.b - Memory.ipynb
- Sprint project:
    - Complete the function build_cover_letter_writing() at backend/models/jobs_finder_agent.py. This class should consume the jobs from the database we've created in the previous lesson but also have some extra tools.
    - Take the profile + job found and make a personalized message to the recruiter.
