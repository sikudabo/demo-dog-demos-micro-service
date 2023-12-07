from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Specify the model and tokenizer
model_name = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Example usage
text = "Hugging Face is a great resource for natural language processing."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
input_ids = tokenizer.encode(text, return_tensors="pt")
translation = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)
translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

print(translated_text)
