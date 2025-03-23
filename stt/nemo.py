import time

from streaming_stt_nemo import Model

import logger
from stt.config import TTS_STT_LANGUAGE

log = logger.get(__name__)
model = Model(TTS_STT_LANGUAGE)


def transcribe(audio):
    start = time.time()
    text = model.stt_file(audio)[0]
    end = time.time()
    log.info(f'Transcribed in {end - start} seconds, result: {text}')
    return text


if __name__ == '__main__':
    transcribe('../input.wav')
