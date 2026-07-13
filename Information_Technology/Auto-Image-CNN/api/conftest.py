"""Make the api/ modules (app, views, utils, middleware) importable in tests,
regardless of how pytest is invoked."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
