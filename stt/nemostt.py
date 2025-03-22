from streaming_stt_nemo import Model, available_languages

model = Model('uk')


def transcribe(audio):
    text = model.stt_file(audio)[0]
    return text


if __name__ == '__main__':
    transcribe('../audio.wav')
