from transformers import PreTrainedTokenizer

class HealthcareQATokenizer(PreTrainedTokenizer):
    def __init__(self, vocab_file_path):
        super().__init__(vocab_file=vocab_file_path)

    def _tokenize(self, text):
        # Implement custom tokenization logic
        tokens = text.split()
        return tokens

    def _convert_token_to_id(self, token):
        # Convert token to ID
        return self.vocab.get(token, self.vocab['[UNK]'])

    def _convert_id_to_token(self, idx):
        # Convert ID to token
        return list(self.vocab.keys())[idx]

    def get_vocab_size(self):
        # Return the size of the vocabulary
        return len(self.vocab)
