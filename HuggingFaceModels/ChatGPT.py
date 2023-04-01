import openai

with open("apikey.secret") as f:
    openai.api_key = f.readline().strip()

prompt = "Tell me a story about a fat rabbit. "

responses = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
    max_tokens = 500,
    presence_penalty = 0.0,
    frequency_penalty = 0.0,
    temperature= 0.0,
    top_p=0.0,
)

response = responses['choices'][0]['message']['content']
token_usage = responses['usage']['total_tokens']
print(response) #prompt is NOT included
