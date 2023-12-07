from transformers import BertTokenizer
from diseases_dataset import disease_qa_dataset

contexts = [item['context'] for item in disease_qa_dataset['train']]
questions = [item['question'] for item in disease_qa_dataset['train']]
answers = [item['answer'] for item in disease_qa_dataset['train']]

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenized_data = tokenizer(contexts, questions, max_length=512, truncation=True, padding=True, return_tensors='pt')
labels = [tokenizer(item[0:512], return_tensors='pt')['input_ids'].squeeze() for item in answers]
