from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")


def transcribe(file):
    outputs = pipe(
        file,
        chunk_length_s=30,
        batch_size=24,
        return_timestamps=True,
    )
    print(outputs)
    return outputs
