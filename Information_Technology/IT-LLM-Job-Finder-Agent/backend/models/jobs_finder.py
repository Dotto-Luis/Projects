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

        # TODO: Create a string template for the chat assistant. It must indicate the LLM
        # that a chat history is being provided and that a new question is being asked
        # and also there are some articles found on a database for answering the question.
        # The template must have three input variables: `history`, `search_results` and `human_input`.
        
    

        # TODO: Create a prompt template using the string template created above.
        # Hint: Use the `langchain.prompts.PromptTemplate` class.
        # Hint: Don't forget to add the input variables: `history`, `search_results` and `human_input`.
        self.prompt =
        

        # TODO: Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
        # Remember some settings are being provided in the __init__ function for this class.
        # Hint: You need to pass `model`, `api_key`, `temperature`, and `provider` parameters.
        self.llm = 
        

        # Create a memory for the chat assistant.
        _memory = ConversationBufferWindowMemory(
            input_key="human_input", k=history_length
        )

        # TODO: Create an instance of `langchain.chains.LLMChain` with the appropriate settings.
        # This chain must combine our prompt, llm and also have a memory.
        self.model = 
        

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

        # TODO: Use the human input and the user resume summary to search for jobs.
        # Hint 1: Use the `self.retriever` instance.
        # Hint 2: You can combine the human input with the resume summary just concatenating strings.
        

        # Call the model to generate a response.
        # We will pass the original human_input on this step, the resume should
        # be used only for the retrieval of jobs (`search_results`).
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