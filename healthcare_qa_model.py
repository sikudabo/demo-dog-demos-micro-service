import torch.nn as nn
from transformers import PreTrainedModel

class HealthcareQAModel(PreTrainedModel):
    def __init__(self, config):
        super(HealthcareQAModel, self).__init__(config)

        self.embedding_layer = nn.Embedding(config.vocab_size, config.hidden_size)
        self.linear_layer = nn.Linear(config.hidden_size, 2)  # 2 for start and end positions

        self.init_weights()

    def forward(self, input_ids, attention_mask=None):
        embeddings = self.embedding_layer(input_ids)
        logits = self.linear_layer(embeddings)

        return logits
    
