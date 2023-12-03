from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

@app.route('/generate-code', methods=['POST'])
def generate_code():
    try:
        user_input = request.json['input']
        input_ids = tokenizer.encode(user_input, return_tensors='pt')

        # Generate code
        output = model.generate(input_ids, max_length=150, temperature=0.7, num_beams=5, no_repeat_ngram_size=2)
        generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({'generatedCode': generated_code})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
