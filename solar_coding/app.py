import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from solar.eng_latin_tanslator import EngToPiglatinTranslator
from solar.registry import Registry

app = Flask(__name__)
CORS(app)

Registry('eng_piglatin', EngToPiglatinTranslator.factory())


@app.route('/', methods=['POST'])
def translate():
    data = request.data

    if isinstance(data, bytes):
        data = data.decode()
        data = json.loads(data)

    if data is None or data['string'] is None:
        res = 'Invalid Data'
    else:
        eng_piglatin = Registry.get('eng_piglatin')
        res = jsonify(eng_piglatin.translate(data['string']))

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False)
