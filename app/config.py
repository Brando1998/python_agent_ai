import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env vars
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/chat/completions")
USE_OPENAI_MOCK = os.getenv("USE_OPENAI_MOCK", "false").lower() == "true"

# Validate API KEY
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no está definido en .env")
