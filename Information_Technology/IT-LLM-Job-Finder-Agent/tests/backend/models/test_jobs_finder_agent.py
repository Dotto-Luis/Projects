from unittest.mock import MagicMock, patch

from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from backend.config import settings
from backend.models.jobs_finder import JobsFinderAssistant
from backend.models.jobs_finder_agent import JobsFinderAgent


@patch("backend.models.jobs_finder.resume_summarizer")
def test_jobs_finder_agent(resume_summarizer_chain_mock):
    resume_summarizer_chain_mock.return_value = MagicMock()

    job_finder_agent = JobsFinderAgent(
        resume="resume",
        llm_model="gpt-3.5-turbo",
        api_key=settings.OPENAI_API_KEY,
        temperature=0,
        history_length=2,
    )

    # JobsFinderAgent attributes
    assert hasattr(job_finder_agent, "resume")
    assert hasattr(job_finder_agent, "llm")
    assert hasattr(job_finder_agent, "job_finder")
    assert hasattr(job_finder_agent, "agent_executor")
    assert hasattr(job_finder_agent, "agent_memory")
    assert hasattr(job_finder_agent, "history_length")
    assert callable(job_finder_agent.predict)

    # JobsFinderAgent attribute types - support both providers
    assert isinstance(job_finder_agent.llm, (ChatOpenAI, ChatGoogleGenerativeAI))
    assert isinstance(job_finder_agent.job_finder, JobsFinderAssistant)
    assert isinstance(job_finder_agent.agent_executor, AgentExecutor)
    assert isinstance(job_finder_agent.agent_memory, list)
    assert isinstance(job_finder_agent.history_length, int)

    # JobsFinderAssistant attribute types
    # Check code is not making a call to openai to summarize the resume
    assert isinstance(job_finder_agent.job_finder.resume_summary, MagicMock)

    # AgentExecutor attributes tools
    assert len(job_finder_agent.agent_executor.tools) == 2
    assert job_finder_agent.agent_executor.tools[0].name == "jobs_finder"
    assert (
        job_finder_agent.agent_executor.tools[1].name == "cover_letter_writing"
    )