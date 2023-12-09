from transformers import AutoTokenizer 
from diseases_dataset import disease_qa_dataset as raw_datasets

context = raw_datasets['train'][0:30]['context']
question = raw_datasets['train'][0:30]['question']

model_checkpoint = 'bert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

inputs = tokenizer(
    raw_datasets['train'][0:500]['context'],
    raw_datasets['train'][0:500]['question'],
    raw_datasets['train'][0:500]['answer'],
    max_length=100,
    truncation=True,
    padding=True,
    stride=50,
    return_overflowing_tokens=True,
    return_offsets_mapping=True
)

