from flask import Flask, request, jsonify
from flask_cors import CORS
from model_tokenizer import model, tokenizer

app = Flask(__name__)
CORS(app)

def translate_to_spanish(text, model, tokenizer):
    # Tokenize the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate translation
    translation = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)

    # Decode the generated translation
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

    return translated_text

@app.get('/')
def home_page():
    return "<h1>Hello, world!</h1>"

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        english_text = data['english_text']

        # Translate English to Spanish
        spanish_translation = translate_to_spanish(english_text, model, tokenizer)

        return jsonify({'spanish_translation': spanish_translation})

    except Exception as e:
        return jsonify({'error': str(e)})
