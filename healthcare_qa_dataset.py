import json
from torch.utils.data import Dataset
import torch

class HealthcareQADataset(Dataset):
    def __init__(self, json_file_path, tokenizer, max_length=512):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        self.questions = [item['question'] for item in data]
        self.answers = [item['answer'] for item in data]
        self.labels = [item['label'] for item in data]  # Add 'label' to your dataset structure
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, idx):
        encoding = self.tokenizer(
            self.questions[idx],
            self.answers[idx],
            padding='max_length',
            truncation=True,
            max_length=self.max_length,
            return_labels=True,
            return_tensors='pt'
        )
        
        
        # Manually set the 'labels' field
        encoding['labels'] = torch.tensor(self.labels, dtype=torch.long)
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(self.labels[idx], dtype=torch.long)  # Convert to tensor as needed
        }
