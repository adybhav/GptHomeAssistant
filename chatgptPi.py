import openai

openai.api_key = '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'


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "assistant", "content": "who started it?"}
  ]
)

print(completion.choices[0].message)