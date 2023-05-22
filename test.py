import json
from speaker import TextToSpeech

json_data = '''{
  "content": "2",
  "role": "assistant"
}'''

data = json_data.to_dict()
content_value = data["content"]

content_string = json.dumps(content_value)

TextToSpeech(content_string)