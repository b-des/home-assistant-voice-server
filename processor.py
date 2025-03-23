import time

import db
import logger
from api import ha, llm
from config import tts_engine, stt_engine
from llm import post_processing

log = logger.get(__name__)


def process():
    log.info('Start processing input request')
    start_total = time.time()
    utterance = stt_engine.transcribe('input.wav')
    if not len(utterance):
        log.info('No speech detected in the request')
        pass
    prompt = prepare_prompt(utterance)
    speech, ha_payload, raw = llm.infer(prompt)
    # parse json and call HA service
    ha.call_service(ha_payload)
    # save question and answer to history DB
    db.save(utterance, raw)
    response = post_processing.process(speech)
    tts_engine.speak(response)
    log.info(f'Total time processing {time.time() - start_total} seconds')


def prepare_prompt(utterance):
    ha.set_ai_input_state(utterance)
    data = {
        # "model": "command-r",
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": f'{ha.get_prompt()}'
            }
        ]
    }
    history = db.get_history(3)
    if history:
        data['messages'].extend(history)

    data['messages'].append({
        "role": "user",
        "content": utterance
    })
    log.info(f'LLM prompt history: {history}')
    return data


if __name__ == "__main__":
    process()
