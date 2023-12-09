import collections
import tensorflow as tf
from transformers import TFAutoModelForQuestionAnswering
from small_eval_set_example import eval_set 

trained_checkpoint = 'bert-base-uncased'

eval_set_for_model = eval_set.remove_columns(["example_id", "offset_mapping"])
eval_set_for_model.set_format("numpy")

batch = {k: eval_set_for_model[k] for k in eval_set_for_model.column_names}
trained_model = TFAutoModelForQuestionAnswering.from_pretrained(trained_checkpoint)

outputs = trained_model(**batch)

start_logits = outputs.start_logits.numpy()
end_logits = outputs.end_logits.numpy()

import collections

example_to_features = collections.defaultdict(list)
for idx, feature in enumerate(eval_set):
    example_to_features[feature["example_id"]].append(idx)
    
