import openai
from speaker import TextToSpeech
import json


openai.api_key = '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'

def RunGpt(text):
  try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "assistant", "content": text}
        ]
      )
    response = completion.choices[0].message.content
    TextToSpeech(response)
  except Exception as e :
        print(e)