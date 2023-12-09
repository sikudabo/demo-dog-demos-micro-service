from eval_set_for_model import end_logits, start_logits
from small_eval_set_example import eval_set, small_eval_set
from compute_metrics import compute_metrics

compute_metrics(start_logits, end_logits, eval_set, small_eval_set)