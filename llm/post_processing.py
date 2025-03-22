import re

words_to_replace = [
    'Bedroom', 'Kitchen', 'Living room'
]

reg = re.compile(r'[,.]+(?!\d{2}$)|[^\d.,]+')


def process(i: str):
    output = i.replace('У Bedroom', 'у спальні')
    output = i.replace('unavailable', 'в невідомому стані')
    output = output.replace('on', 'ввімкнено').replace('off', 'вимкнено')
    output = re.sub(r'(\d+)\.(\d+)', r'\1,\2', output)
    return output


if __name__ == "__main__":
    print(process('У Bedroom 23.62 градусів.'))