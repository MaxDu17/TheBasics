from transformers import pipeline, set_seed
from transformers import AutoModelForCausalLM, AutoTokenizer

set_seed(42)


## SIMPLE DEMONSTRATION OF GENERATION ##
# generator = pipeline('text-generation', model='gpt2-large') #gpt2, gpt2-medium, gpt2-large, gpt2-xl
# print(generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5))

## MORE IN-DEPTH INTERACTION ##
model = AutoModelForCausalLM.from_pretrained('gpt2-large') #should also work for other models
tokenizer = AutoTokenizer.from_pretrained('gpt2-large')

text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt') #tokenizes the input

output = model(**encoded_input) #runs the tokens through the model
# logits, past_key_values # allows you to get logits directly, which can be very helpful
