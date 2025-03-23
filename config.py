import os
from dotenv import load_dotenv

from stt import STTEngineFactory
from tts import TTSEngineFactory

load_dotenv()


OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY", "")
HOME_ASSISTANT_URL = os.getenv("HOME_ASSISTANT_URL", "")
HOME_ASSISTANT_NODE_RED_URL = os.getenv("HOME_ASSISTANT_NODE_RED_URL", "")
HOME_ASSISTANT_KEY = os.getenv("HOME_ASSISTANT_KEY", "")
TTS_ENGINE = os.getenv("TTS_ENGINE", "google")
STT_ENGINE = os.getenv("STT_ENGINE", "nemo")

tts_engine = TTSEngineFactory.get_tts_engine(TTS_ENGINE)
stt_engine = STTEngineFactory.get_stt_engine(STT_ENGINE)
