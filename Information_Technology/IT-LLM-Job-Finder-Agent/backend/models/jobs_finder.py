from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

from backend.config import settings
from backend.models.resume_summarizer_chain import get_resume_summarizer_chain
from backend.retriever import Retriever
from backend.llm_factory import get_llm

resume_summarizer = get_resume_summarizer_chain()


class JobsFinderAssistant:
    def __init__(
        self, resume, llm_model, api_key, temperature=0, history_length=3
    ):
        """
        Initialize the JobsFinderAssistant class.

        Parameters
        ----------
        resume : str
            The resume of the user.

        llm_model : str
            The model name.

        api_key : str
            The API key for accessing the LLM model.

        temperature : float
            The temperature parameter for generating responses.

        history_length : int, optional
            The length of the conversation history to be stored in memory. Default is 3.
        """
        # Make a summary of the resume for the queries
        # Use resume_summarizer_chain.
        self.resume_summary = resume_summarizer.invoke(resume)

        # Initialize the jobs retriever
        self.retriever = Retriever()

        # Template for the chat assistant. This assistant indicates the LLM that a chat history is being provided,
        # a new question is being asked and also there are some articles found on a database for answering the question.
        template = (
        "You are an AI job search assistant.\n\n"
        "Inputs:\n"
        "- Conversation history: {history}\n"
        "- Relevant job postings: {search_results}\n"
        "- User question: {human_input}\n\n"
        "Task:\n"
        "1) Use the job postings and the conversation history to understand what the user is looking for.\n"
        "2) Suggest the most relevant roles.\n"
        "3) Explain briefly why each suggestion is a good fit.\n\n"
        "Answer:\n"
        "- Start by summarizing what the user seems to be looking for.\n"
        "- Then list 2–5 suggested roles from the job postings.\n"
        "- For each role, add a one-line explanation of the fit.\n"

        )

        # Prompt template using the string template created above.
        self.prompt = PromptTemplate(
            input_variables=["history", "search_results", "human_input"],
            template=template,
        )

        # Instance of an LLM using the `get_llm` factory function with the appropriate settings.
        self.llm = get_llm(
            model=llm_model,
            api_key=api_key,
            temperature=temperature,
            provider=settings.LLM_PROVIDER,
        )

        # Create a memory for the chat assistant.
        _memory = ConversationBufferWindowMemory(
            input_key="human_input", k=history_length
        )

        # Instance of `langchain.chains.LLMChain` with the appropriate settings.
        self.model = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=_memory,
            verbose=settings.LANGCHAIN_VERBOSE,
        )
        

    def predict(self, human_input: str) -> str:
        """
        Generate a response to a human input.

        Parameters
        ----------
        human_input : str
            The human input to the chat assistant.

        Returns
        -------
        response : str
            The response from the chat assistant.
        """
        query = (
            f"Job search query: {human_input}\n\n"
            f"Candidate profile summary: {self.resume_summary}"
        )
        jobs = self.retriever.search(query)

        # Human input and the user resume summary to search for jobs.
        model_answer = self.model.invoke(
        {"search_results": jobs, "human_input": human_input}
        )

        return model_answer


if __name__ == "__main__":
    # Determine which model and API key to use based on provider
    llm_model = settings.OPENAI_LLM_MODEL if settings.LLM_PROVIDER == "openai" else settings.GEMINI_LLM_MODEL
    api_key = settings.OPENAI_API_KEY if settings.LLM_PROVIDER == "openai" else settings.GOOGLE_API_KEY
    
    # Create an instance of JobFinderAssistant with appropriate settings
    resume = """
John Doe
john.doe@email.com

Objective:

Results-driven and highly skilled Software Engineer with 5 years of experience designing, developing, and maintaining cutting-edge software solutions. Adept at collaborating with cross-functional teams to drive project success.

Education:

Bachelor of Science in Computer Science
ABC University, Anytown, USA
Graduation Date: May 2020

Technical Skills:

Programming Languages: Java, Python, JavaScript
Web Technologies: HTML5, CSS3, React.js
Database Management: MySQL, MongoDB
Frameworks and Libraries: Spring Boot, Node.js
Version Control: Git
Operating Systems: Windows, Linux
Other Tools: JIRA, Docker

Professional Experience:

Software Engineer | XYZ Tech, Anytown, USA | June 2020 - Present

Developed and maintained scalable web applications using Java and Spring Boot, resulting in a 15% improvement in application performance.
Conducted code reviews and provided constructive feedback to team members, resulting in improved code quality and adherence to coding standards.
Participated in agile development processes, including daily stand-ups, sprint planning, and retrospective meetings.

Projects:

E-commerce Platform Redesign | March 2022 - June 2022

Led the redesign of the e-commerce platform using React.js, resulting in a 20% increase in user engagement and a 15% improvement in page load times.
Inventory Management System | September 2019 - December 2019

Developed a robust inventory management system using Java and Spring Boot, streamlining the tracking of product stock and reducing errors by 30%.

Certifications:

Oracle Certified Professional, Java SE Programmer

Professional Memberships:

Member, Association for Computing Machinery (ACM)
"""
    chat_assistant = JobsFinderAssistant(
        resume=resume,
        llm_model=llm_model,
        api_key=api_key,
        temperature=0,
    )

    # Use the instance to generate a response
    output = chat_assistant.predict(
        human_input="I'm looking for a job as a software engineer."
    )

    print(output["text"])