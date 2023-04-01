from transformers import pipeline, set_seed
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# t5-small, t5-base, t5-large, t5-3b
model_name = "t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name) #can include cache dir

try:
    n_positions = model.config.n_positions
except AttributeError:
    n_positions = 512

tokenizer = AutoTokenizer.from_pretrained(model_name, model_max_length=n_positions)

# generally you would do mask filling, but this is a base working example
tokens = tokenizer("Studies show that ", return_tensors = "pt", padding = True)
outputs = model.generate(**tokens, max_length=150, do_sample=True, top_p=0.96, num_return_sequences=1)
text = tokenizer.batch_decode(outputs, skip_special_tokens = False)
print(outputs)
