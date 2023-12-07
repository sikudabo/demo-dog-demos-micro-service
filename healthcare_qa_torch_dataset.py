from torch.utils.data import TensorDataset
from healthcare_qa_tokenizer import labels, tokenized_data
import torch
min_size = min(t.size(0) for t in labels)
# Truncate larger tensors
truncated_labels = [t[:min_size] for t in labels]
dataset = TensorDataset(
    tokenized_data['input_ids'],
    tokenized_data['attention_mask'],
    torch.stack(truncated_labels),
)