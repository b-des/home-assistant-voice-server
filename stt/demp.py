from streaming_stt_nemo import Model, available_languages

import gradio as gr

LANGUAGES = available_languages
default_lang = "en"

engines = {
    default_lang: Model(default_lang)
}


def transcribe(audio, language: str):
    if language not in engines:
        engines[language] = Model(language)

    model = engines[language]
    text = model.stt_file(audio)[0]
    return text


gr.Interface(
    fn=transcribe,
    inputs=[
        gr.Audio(source="microphone", type="filepath"),
        gr.Radio(
            label="Language",
            choices=LANGUAGES,
            value=default_lang
        )
    ],
    outputs=[
        "textbox"
    ],
    cache_examples=True,
    live=True).launch()