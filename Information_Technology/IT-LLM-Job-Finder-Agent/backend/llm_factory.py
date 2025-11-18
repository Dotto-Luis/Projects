from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import settings


def get_llm(temperature=0, provider=None, model=None, api_key=None):
    """
    Factory function to get the appropriate LLM based on provider.
    
    Parameters
    ----------
    temperature : float
        The temperature parameter for generating responses.
    provider : str, optional
        Override the default provider from settings ('openai' or 'gemini').
    model : str, optional
        Override the default model from settings.
    api_key : str, optional
        API key (for backward compatibility, prefer env vars).
    
    Returns
    -------
    llm : BaseChatModel
        The appropriate LLM instance.
    """
    provider = provider or settings.LLM_PROVIDER
    
    if provider == "openai":
        return ChatOpenAI(
            model=model or settings.OPENAI_LLM_MODEL,
            api_key=api_key or settings.OPENAI_API_KEY,
            temperature=temperature,
        )
    elif provider == "gemini":
        return ChatGoogleGenerativeAI(
            model=model or settings.GEMINI_LLM_MODEL,
            google_api_key=api_key or settings.GOOGLE_API_KEY,
            temperature=temperature,
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")