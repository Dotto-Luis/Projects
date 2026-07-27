"""Make `src/` importable in tests (the package uses `from scrapers... import`).

`scoring.py` imports `ollama` at module level; the test suite stubs it so the
pure scoring helpers can be tested without a running Ollama server.
"""

import sys
import types
from pathlib import Path

SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(SRC))

# Stub `ollama` if it is not installed: tests only exercise pure helpers
# (JSON cleaning, normalization, clamping), never a real LLM call.
if "ollama" not in sys.modules:
    try:
        import ollama  # noqa: F401
    except ModuleNotFoundError:
        stub = types.ModuleType("ollama")
        stub.chat = lambda *a, **k: (_ for _ in ()).throw(
            RuntimeError("ollama stub: no real inference in tests")
        )
        sys.modules["ollama"] = stub
