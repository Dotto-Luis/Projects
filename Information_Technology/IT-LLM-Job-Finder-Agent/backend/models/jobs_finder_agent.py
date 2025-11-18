from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_openai_functions_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

from backend.config import settings
from backend.models.jobs_finder import JobsFinderAssistant
from backend.llm_factory import get_llm


def build_job_finder(job_finder_assistant):
    def job_finder(human_input: str):
        return job_finder_assistant.predict(human_input)

    return job_finder


def build_cover_letter_writing(llm, resume):
    def cover_letter_writing(job_description: str):
        # TODO: Create a string template for this chain. It must indicate the LLM
        # that a resume and a job description is being provided, it must write a
        # cover letter for the job description using the applicant skills.
        # The template must have two input variables: `resume` and `job_description`.
        

        # TODO: Create a prompt template using the string template created above.
        # Hint: Use the `langchain.prompts.PromptTemplate` class.
        # Hint: Don't forget to add the input variables: `resume` and `job_description`.
        prompt = 
        

        # TODO: Create an instance of `langchain.chains.LLMChain` with the appropriate settings.
        # This chain must combine our prompt and an llm. It doesn't need a memory.
        cover_letter_writing_chain = 

    return cover_letter_writing


class JobsFinderAgent:
    def __init__(
        self, resume, llm_model, api_key, temperature=0, history_length=3
    ):
        """
        Initialize the JobsFinderAgent class.

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
        """

        self.resume = resume

        # TODO: Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
        # Hint: You need to pass `model`, `api_key`, `temperature`, and `provider` parameters.
        self.llm = 

        # Create the Job finder tool
        self.job_finder = JobsFinderAssistant(
            resume=resume,
            llm_model=llm_model,
            api_key=api_key,
            temperature=temperature,
        )

        self.agent_executor = self.create_agent()
        self.agent_memory = []
        self.history_length = history_length

    def create_agent(self):
        job_finder = build_job_finder(self.job_finder)
        cover_letter_writing = build_cover_letter_writing(
            self.llm, self.resume
        )
        tools = [
            Tool(
                name="jobs_finder",
                func=job_finder,
                description="Look up for jobs based on user preferences.",
                handle_tool_error=True,
            ),
            Tool(
                name="cover_letter_writing",
                func=cover_letter_writing,
                description="Write a cover letter based on a job description, extract as much information you can about the job from the user input and from the chat history.",
                handle_tool_error=True,
            ),
        ]

        prompt = hub.pull("hwchase17/openai-functions-agent")
        print(f"Prompt pulled from hub: {prompt}")

        # Construct the OpenAI Tools agent
        # agent = create_react_agent(self.llm, tools, prompt)
        agent = create_openai_functions_agent(self.llm, tools, prompt)

        # Create an agent executor by passing in the agent and tools
        return AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            early_stopping_method="force",
            return_intermediate_steps=True,
            handle_parsing_errors=True,
        )

    def predict(self, human_input: str) -> str:
        agent_reseponse = self.agent_executor.invoke(
            {"input": human_input, "chat_memory": self.agent_memory}
        )

        self.agent_memory.extend(
            [
                HumanMessage(content=human_input),
                AIMessage(content=agent_reseponse["output"]),
            ]
        )

        self.agent_memory = self.agent_memory[-self.history_length :]

        return agent_reseponse