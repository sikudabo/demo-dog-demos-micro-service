from transformers import BertForQuestionAnswering
from torch.utils.data import DataLoader
import torch
from healthcare_qa_torch_dataset import dataset 
from pathlib import Path

base_path = Path(__file__).parent 
target_path = f'{base_path}/tuned_bert_model.bin'
model_name = 'bert-base-uncased'
model = BertForQuestionAnswering.from_pretrained(model_name)

optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
train_loader = DataLoader(dataset, batch_size=4, shuffle=True)

num_epochs = 3
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

for epoch in range(num_epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids, attention_mask = batch  # No labels in the forward pass
        input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)
        
        outputs = model(input_ids, attention_mask=attention_mask)
        # Extract predicted start and end logits
        start_logits, end_logits = outputs.logits.split(1, dim=-1)
        start_logits, end_logits = start_logits.squeeze(-1), end_logits.squeeze(-1)
        # Calculate loss based on the true start and end positions
        start_positions, end_positions = batch["start_positions"].to(device), batch["end_positions"].to(device)
        loss = torch.nn.functional.cross_entropy(start_logits, start_positions) + torch.nn.functional.cross_entropy(end_logits, end_positions)
        
        loss.backward()
        optimizer.step()
        
# model.save_pretrained(target_path)
