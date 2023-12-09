import tensorflow as tf
from transformers import TFAutoModelForQuestionAnswering
from small_eval_set_example import eval_set 

trained_checkpoint = 'bert-base-uncased'

eval_set_for_model = eval_set.remove_columns(["example_id", "offset_mapping"])
eval_set_for_model.set_format("numpy")

batch = {k: eval_set_for_model[k] for k in eval_set_for_model.column_names}
trained_model = TFAutoModelForQuestionAnswering.from_pretrained(trained_checkpoint)

outputs = trained_model(**batch)
print(outputs)