from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_react_code(prompt, model_name="gpt2", max_length=300, temperature=0.7):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate code
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the generated code
    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_code

if __name__ == "__main__":
    # Example prompt to generate a React component
    prompt = "Create a material UI application bar"

    # Generate React code using GPT-2
    generated_code = generate_react_code(prompt)

    # Print the generated code
    print(generated_code)
