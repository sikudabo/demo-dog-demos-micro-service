from torch.utils.data import TensorDataset 
from healthcare_qa_tokenizer import labels, tokenized_data
from torch import stack

dataset = TensorDataset(
    tokenized_data['input_ids'],
    tokenized_data['attention_mask'],
    stack(labels),
)