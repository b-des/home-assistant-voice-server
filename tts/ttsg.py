from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
import playsound
import time


def speak(text):
    tts = gTTS(text=text, lang='uk', slow=False)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    sound = speedup(sound, 1.1)
    sound.export("output.wav", format="wav")
    # p = Process(name="playsound", target=play)
    # p.start()


def play():
    playsound.playsound('test.wav')


if __name__ == '__main__':
    start = time.time()
    speak("")
    end = time.time()
    print(f"===Synthesised in {end - start} seconds===")