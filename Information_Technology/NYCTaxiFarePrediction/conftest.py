"""Make the model/ and webapp/api/ modules importable in tests,
regardless of how pytest is invoked."""

import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "webapp" / "api"))
