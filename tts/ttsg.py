import os
import time

from dotenv import load_dotenv
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup

load_dotenv()


def speak(text):
    tts = gTTS(text=text, lang=os.getenv("TTS_STT_LANGUAGE"), slow=False)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    sound = speedup(sound, 1.1)
    sound.export("output.wav", format="wav")
    # p = Process(name="playsound", target=play)
    # p.start()


if __name__ == '__main__':
    start = time.time()
    speak("Чим можу допомогти?")
    end = time.time()
    print(f"===Synthesised in {end - start} seconds===")