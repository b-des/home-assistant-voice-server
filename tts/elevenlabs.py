import time
from typing import Iterator

from elevenlabs.client import ElevenLabs

import logger
from tts.config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
log = logger.get(__name__)


def speak(text):
    start = time.time()
    response = client.text_to_speech.convert(
        voice_id=ELEVENLABS_VOICE_ID,
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_turbo_v2_5"
    )
    save_iterator_to_mp3(response)
    end = time.time()
    log.info(f'Synthesised in {end - start} seconds')


def save_iterator_to_mp3(iterator: Iterator[bytes]) -> None:
    with open("output.wav", 'wb') as file:
        for chunk in iterator:
            file.write(chunk)


if __name__ == "__main__":
    speak("світло на кухні вимкнено")
