from transformers import MarianMTModel, MarianTokenizer

# Load MarianMT model and tokenizer for English to Spanish translation
model_name = "Helsinki-NLP/opus-mt-en-es"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

