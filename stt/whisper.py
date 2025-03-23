import time

from transformers import pipeline

import logger

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
log = logger.get(__name__)


def transcribe(file):
    start = time.time()
    text = pipe(
        file,
        chunk_length_s=30,
        batch_size=24,
        return_timestamps=True,
    )
    end = time.time()
    log.info(f'Transcribed in {end - start} seconds, result: {text}')
    return text
