from datasets import Dataset 
from pathlib import Path 
import json 

base_path = Path(__file__).parent 
full_path = f'{base_path}/question_answers.json'
path = Path(full_path)
contents = path.read_text()
save_to_disk_path = f'{base_path}/saved_dataset.json'
disease_question_answers = json.loads(contents)
disease_qa_dataset = Dataset.from_list(disease_question_answers)

disease_qa_dataset.save_to_disk(save_to_disk_path, storage_options={"format": "json"})
print('Saved dataset to disk')