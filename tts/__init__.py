import time

import logger
import tts.ttsg as tts

log = logger.get(__name__)


def process(phrase):
    start = time.time()
    tts.speak(phrase)
    end = time.time()
    log.info(f'Synthesised in {end - start} seconds')
