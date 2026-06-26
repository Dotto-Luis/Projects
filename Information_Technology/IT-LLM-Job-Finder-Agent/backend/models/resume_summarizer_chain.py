from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from backend.config import settings
from backend.llm_factory import get_llm

# Template for this chain. It must indicate the LLM
# that a resume is being provided to be summarized to extract the candidates skills.
# The template must have one input variables: `resume`.
template = (
    "Act as the best expert technical recruiter in the world. "
    "You will receive a candidate's resume as an input and your task is to summarize it, "
    "focusing on their main skills, technologies, tools, and relevant experience.\n\n"
    "Resume:\n{resume}\n\n"
    "Summarized skills and profile:"
)

def get_resume_summarizer_chain():
    #Pompt template using the string template created above.
    prompt = PromptTemplate(
    input_variables=["resume"],
    template=template,
    )

    # LLM with temperature and provider
    llm = get_llm(
        temperature=0,
        provider=settings.LLM_PROVIDER,
    )

    # LLMChain without memory
    resume_summarizer_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=settings.LANGCHAIN_VERBOSE,
    )

    return resume_summarizer_chain


if __name__ == "__main__":
    resume_summarizer_chain = get_resume_summarizer_chain()
    print(
        resume_summarizer_chain.invoke(
            {"resume": "I am a software engineer with 5 years of experience"}
        )
    )