from transformers import AutoTokenizer 
from squad_dataset import squad_dataset as raw_datasets
from preprocess_validation_examples import preprocess_validation_examples

small_eval_set = raw_datasets["validation"].select(range(32)) # This range needs to be less than or equal to the size of the dataset
trained_checkpoint = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(trained_checkpoint)
eval_set = small_eval_set.map(
    preprocess_validation_examples,
    batched=True,
    remove_columns=raw_datasets["validation"].column_names,
)