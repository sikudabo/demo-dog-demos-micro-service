from datasets import load_dataset 
from pathlib import Path 

base_path = Path(__file__).parent 
full_path = f'{base_path}/saved_dataset.json/data-00000-of-00001.arrow'
dataset = load_dataset('arrow', data_files=full_path)
print(len(dataset))
