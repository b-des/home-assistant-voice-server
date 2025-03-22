import time

import db
import logger
import stt
import tts
from api import ha, llm
from llm import post_processing

log = logger.get(__name__)


def process():
    log.info('Start processing input request')
    start_total = time.time()
    utterance = stt.process('audio.wav')
    if not len(utterance):
        log.info('No speech detected in the request')
        pass
    prompt = prepare_prompt(utterance)
    speech, ha_payload = llm.infer(prompt)
    # parse json and call HA service
    ha.call_service(ha_payload)
    # save question and answer to history DB
    db.save(utterance, f'{speech}##{ha_payload}')
    response = post_processing.process(speech)
    tts.process(response)
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
