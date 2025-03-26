import os

from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "")
ELEVENLABS_VOLUME_GAIN = os.getenv("ELEVENLABS_VOLUME_GAIN", "")
TTS_STT_LANGUAGE = os.getenv("TTS_STT_LANGUAGE", "")
