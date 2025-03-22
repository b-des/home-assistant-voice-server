import logging
import os
import time

import requests

from processor import prepare_prompt

logger = logging.getLogger(__name__)
headers = {
    'Authorization': f'Bearer {os.getenv("OPEN_AI_API_KEY")}'
}


def infer(data):
    start = time.time()
    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)
    end = time.time()
    logger.info(f"LLM inference finished in {end - start} seconds")
    logger.info(f'Raw LLM response: {response.json()}')
    # extract LLM response
    content_ = response.json()['choices'][0]['message']['content']
    # split human-readable part and json part(in case if such is present)
    logger.info(f'Payload: {content_}')
    parts = content_.split("##")
    # get parsed answer and return to TTS
    speech = parts[0].replace('\n', '')
    payload = parts[1] if len(parts) > 1 else ''
    return speech, payload


if __name__ == '__main__':
    # infer('скільки секунд залишилось до пятнадцятої години')
    infer(prepare_prompt('вимкни світло на кухні'))
