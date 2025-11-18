from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from backend.config import settings
from backend.llm_factory import get_llm

# TODO: Create a string template for this chain. It must indicate the LLM
# that a resume is being provided to be summarized to extract the candidates skills.
# The template must have one input variables: `resume`.
template = """
"""


def get_resume_summarizer_chain():
    # TODO: Create a prompt template using the string template created above.
    # Hint: Use the `langchain.prompts.PromptTemplate` class.
    # Hint: Don't forget to add the input variables: `resume`.


    # TODO: Create an instance of an LLM using the `get_llm` factory function with the appropriate settings.
    # Hint: You need to pass `temperature` and `provider` parameters.


    # TODO: Create an instance of `langchain.chains.LLMChain` with the appropriate settings.
    # This chain must combine our prompt and an llm. It doesn't need a memory.

    return resume_summarizer_chain


if __name__ == "__main__":
    resume_summarizer_chain = get_resume_summarizer_chain()
    print(
        resume_summarizer_chain.invoke(
            {"resume": "I am a software engineer with 5 years of experience"}
        )
    )