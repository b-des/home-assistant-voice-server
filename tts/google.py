import time

from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup

import logger
from tts.config import TTS_STT_LANGUAGE
log = logger.get(__name__)


def speak(text):
    start = time.time()
    tts = gTTS(text=text, lang=TTS_STT_LANGUAGE, slow=False)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    sound = speedup(sound, 1.1)
    sound.export("output.wav", format="wav")
    end = time.time()
    log.info(f'Synthesised in {end - start} seconds')
    # p = Process(name="playsound", target=play)
    # p.start()


if __name__ == '__main__':
    speak("Чим можу допомогти?")
