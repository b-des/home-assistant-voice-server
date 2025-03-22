import time

import logger
import stt.nemostt

log = logger.get(__name__)


def process(file):
    start = time.time()
    result = nemostt.transcribe(file)
    end = time.time()
    log.info(f'Transcribed in {end - start} seconds, result: {result}')
    return result
