import os
from typing import Iterator

from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def save_iterator_to_mp3(iterator: Iterator[bytes]) -> None:
    """
    Converts an iterator of bytes to an MP3 file.

    :param iterator: An iterator yielding chunks of bytes.
    :param output_file: The path to the output MP3 file.
    """
    with open("output.mp3", 'wb') as file:
        for chunk in iterator:
            file.write(chunk)


def speak(text):
    response = client.text_to_speech.convert(
        voice_id=os.getenv("ELEVENLABS_VOICE_ID"),
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_turbo_v2_5"
    )
    play(response)
    # save_iterator_to_mp3(response)
    # sound = AudioSegment.from_mp3("output.mp3")
    # # sound = speedup(sound, 1.1)
    # sound = sound + 3
    # sound.export("output.wav", format="wav")


if __name__ == "__main__":
    speak("світло на кухні вимкнено")
