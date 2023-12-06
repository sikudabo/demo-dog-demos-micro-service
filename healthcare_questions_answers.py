from transformers import AutoTokenizer, DataCollatorForTokenClassification
from healthcare_qa_dataset import HealthcareQADataset
from pathlib import Path 
import torch

base_path = Path(__file__).parent 
full_path = f'{base_path}/healthcare_qa_dataset.json'

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
data_collator = DataCollatorForTokenClassification(tokenizer, padding=True)

healthcare_dataset = HealthcareQADataset(full_path, tokenizer)
tokenized_dataset = tokenizer(
    healthcare_dataset.questions,
    healthcare_dataset.answers,
    padding=True,
    truncation=True,
    return_tensors='pt'
)

# Manually add labels to the tokenized dataset
tokenized_dataset['labels'] = torch.tensor(healthcare_dataset.labels, dtype=torch.long)

# Convert the tokenized dataset to a list of dictionaries
examples = [{"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels} for input_ids, attention_mask, labels in zip(tokenized_dataset["input_ids"], tokenized_dataset["attention_mask"], tokenized_dataset["labels"])]

# Use data_collator on the list of dictionaries
batched_dataset = data_collator([examples])

print(batched_dataset)
