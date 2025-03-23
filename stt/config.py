import os

from dotenv import load_dotenv

load_dotenv()

TTS_STT_LANGUAGE = os.getenv("TTS_STT_LANGUAGE", "")
