from transformers import BertTokenizer
from diseases_dataset import disease_qa_dataset

contexts = [item['context'] for item in disease_qa_dataset['train']]
questions = [item['question'] for item in disease_qa_dataset['train']]
answers = [item['answer'] for item in disease_qa_dataset['train']]

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenized_data = tokenizer(contexts, questions, truncation=True, padding=True, return_tensors='pt')