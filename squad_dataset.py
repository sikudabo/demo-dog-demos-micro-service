from datasets import load_dataset 
from pathlib import Path 

base_path = Path(__file__).parent
full_path = f'{base_path}/SQuAD.json'
squad_dataset = load_dataset('json', data_files={'train': full_path, 'validation': full_path})
