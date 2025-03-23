import importlib

import logger

log = logger.get(__name__)


class STTEngineFactory:
    @staticmethod
    def get_stt_engine(name):
        try:
            module = importlib.import_module(f'stt.{name}')
            log.info(f'Using STT engine: {name}')
            return module
        except ModuleNotFoundError:
            raise ImportError(f'TTS Engine "{name}" not found')
