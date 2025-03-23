import os

from flask import Flask
from flask import send_file, request

from processor import process

app = Flask(__name__)


@app.route('/handshake', methods=['GET'])
def entry():
    return {'allowed': True}


@app.route('/', methods=['GET', 'POST'])
def process_assistant_request():
    audio = request.files['audio']
    audio.save(os.path.join('input.wav'))
    process()
    return send_file(
        'output.wav',
        mimetype="audio/wav",
        as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
