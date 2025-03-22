from ukrainian_tts.tts import TTS, Voices, Stress
import IPython.display as ipd
import playsound
from multiprocessing import Process

tts = TTS(device="cpu")  # can try gpu, mps


def speak(text):
    with open("output.wav", mode="wb") as file:
        print("Start TTS....")
        _, output_text = tts.tts(text, Voices.Lada.value, Stress.Dictionary.value, file)
    print("Accented text:", output_text)
    #p = Process(name="playsound", target=play)
    #p.start()


# ipd.Audio(filename="test.wav")

def play():
    playsound.playsound('output.wav')


if __name__ == '__main__':
    speak("У спальні 24,16 градусів.")
