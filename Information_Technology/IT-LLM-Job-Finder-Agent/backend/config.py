from pathlib import Path
from typing import Optional, Literal

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv(".env"))

root = Path(__file__).parent.parent
print("root", root)


class Settings(BaseSettings):
    # LLM Provider settings
    LLM_PROVIDER: Literal["openai", "gemini"] = "openai"
    
    # OpenAI settings
    OPENAI_API_KEY: Optional[str] = "fill-with-your-api-key"
    OPENAI_LLM_MODEL: Optional[str] = "gpt-4o-mini"
    
    # Gemini settings
    GOOGLE_API_KEY: Optional[str] = ""
    GEMINI_LLM_MODEL: Optional[str] = "gemini-2.5-flash"  # Updated to 2.5
    
    LANGCHAIN_VERBOSE: bool = False

    # Document Ingestion
    DATASET_PATH: Optional[str] = f"{root}/dataset/jobs.csv"
    CHROMA_DB_PATH: Optional[str] = f"{root}/chroma"
    CHROMA_COLLECTION: Optional[str] = "jobs"
    EMBEDDINGS_MODEL: Optional[str] = "paraphrase-MiniLM-L6-v2"

    # Email settings
    SENDER_EMAIL_ADDRESS: Optional[str] = ""
    SENDER_EMAIL_PASSWORD: Optional[str] = ""


settings = Settings()