import os

from dotenv import load_dotenv
from streaming_stt_nemo import Model

load_dotenv()
model = Model(os.getenv("TTS_STT_LANGUAGE"))


def transcribe(audio):
    text = model.stt_file(audio)[0]
    return text


if __name__ == '__main__':
    transcribe('../audio.wav')
