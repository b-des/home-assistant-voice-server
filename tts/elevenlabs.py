import io
import time

from elevenlabs.client import ElevenLabs
from pydub import AudioSegment

import logger
from tts.config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, ELEVENLABS_VOLUME_GAIN

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
log = logger.get(__name__)


def speak(text):
    start = time.time()
    response = client.text_to_speech.convert(
        voice_id=ELEVENLABS_VOICE_ID,
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings={
            'speed': 1,
            # 'stability': 0.9,
            # 'similarity_boost': 0.9
        }
    )
    save(response)
    end = time.time()
    log.info(f'Synthesised in {end - start} seconds')


def save(iterator):
    # Save ElevenLabs MP3 response to a file-like object
    mp3_bytes_io = io.BytesIO()
    for chunk in iterator:  # response is an iterator[bytes]
        mp3_bytes_io.write(chunk)
    # Seek to the beginning so we can read it
    mp3_bytes_io.seek(0)
    # Load MP3 using pydub
    audio = AudioSegment.from_file(mp3_bytes_io, format="mp3")
    # Convert to Signed 16-bit PCM, 16kHz, Mono
    audio = audio.set_frame_rate(16000).set_sample_width(2).apply_gain(ELEVENLABS_VOLUME_GAIN).set_channels(1)
    # Export the corrected WAV file
    audio.export("output.wav", format="wav")


if __name__ == "__main__":
    speak("світло на кухні вимкнено")
