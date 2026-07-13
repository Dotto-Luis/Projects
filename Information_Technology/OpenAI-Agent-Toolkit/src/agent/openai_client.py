# src/agent/openai_client.py

import os
from functools import lru_cache

from dotenv import load_dotenv
from openai import OpenAI


@lru_cache(maxsize=1)
def get_client() -> OpenAI:
    """Lazily create the OpenAI client.

    Deferred until first use so importing the package never requires an
    API key (keeps tests and tooling independent of credentials).
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy env.example to .env and add your key."
        )
    return OpenAI(api_key=api_key)
