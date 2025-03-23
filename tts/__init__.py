import importlib

import logger

log = logger.get(__name__)


class TTSEngineFactory:
    @staticmethod
    def get_tts_engine(name):
        try:
            module = importlib.import_module(f'tts.{name}')
            log.info(f'Using TTS engine: {name}')
            return module
        except ModuleNotFoundError:
            raise ImportError(f'TTS Engine "{name}" not found')
