from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

from backend.config import settings
from backend.llm_factory import get_llm


class ChatAssistant:
    def __init__(self, llm_model, api_key, temperature=0, history_length=3):
        """
        Initialize the ChatAssistant class.

        Parameters
        ----------
        llm_model : str
            The model name.

        api_key : str
            The API key for accessing the LLM model.

        temperature : float
            The temperature parameter for generating responses.

        history_length : int, optional
            The length of the conversation history to be stored in memory. Default is 3.
        """
        # String template for the chat assistant.

        template = (
            "I'm here to help you with your dream job!\n"
            "I will verify all the messages to find the right match for you.\n"
            "Use the history for context when generating your response.\n\n"
            "Conversation history:\n"
            "{history}\n\n"
            "User: {human_input}\n"
            "Assistant:"
        )        

        # Prompt template using the string template created above.
        self.prompt = PromptTemplate(
            template=template,
            input_variables=["history", "human_input"],
        )

        # Instance of an LLM using the `get_llm`.

        self.llm = get_llm(
            model=llm_model,
            api_key=api_key,
            temperature=temperature,
            provider=settings.LLM_PROVIDER,
        )


        # Instance of `langchain.chains.LLMChain` and memory.
        memory = ConversationBufferWindowMemory(
            k=history_length,
            memory_key="history",
            input_key="human_input",
            return_messages=False,
        )

        self.model = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=memory,
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
        response = self.model.invoke(human_input)

        return response


if __name__ == "__main__":
    # Determine which model and API key to use based on provider
    llm_model = settings.OPENAI_LLM_MODEL if settings.LLM_PROVIDER == "openai" else settings.GEMINI_LLM_MODEL
    api_key = settings.OPENAI_API_KEY if settings.LLM_PROVIDER == "openai" else settings.GOOGLE_API_KEY
    
    # Create an instance of ChatAssistant with appropriate settings
    chat_assistant = ChatAssistant(
        llm_model=llm_model,
        api_key=api_key,
        temperature=0,
        history_length=2,
    )

    # Use the instance to generate a response
    output = chat_assistant.predict(
        human_input="what is the answer to life the universe and everything?"
    )

    print(output)