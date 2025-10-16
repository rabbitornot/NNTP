import json
import re
from typing import List

from ollama import chat
from ollama import ChatResponse
from dataclasses import dataclass

generate_plan_prompt = lambda topic: """You are a math teacher. You can use LaTeX. Create a course outline on the given topic: " + topic + ". The course should be divided into chapters, each with a title, a brief introduction, and a full course content. The content should be clear, concise, and suitable for beginners.

⚠️ Important formatting instructions:
- The "content" field must contain the **entire course content** for the chapter.
- If you need to make line breaks, you MUST use the HTML <br> tag (do not use newline characters).
- The final output will be rendered in HTML by a Flask server, so format accordingly.

Respond ONLY with a valid JSON that matches the **exact** schema below. Do not include any explanations, comments, markdown, or extra formatting:

{
  "title": "string",
  "chapters": [
    {
      "title": "string",
      "introduction": "string",
      "content": "string"
    }
  ]
}

Make sure the JSON is syntactically valid and can be parsed directly.

"""

def call_model(request: str) -> str:
    response: ChatResponse = chat(model='qwen3:0.6b', messages=[
    {
        'role': 'user',
        'content': request,
    },
    ])

    return re.sub(r'<think>.*?</think>', '', response['message']['content'], flags=re.DOTALL)

def generate_plan(topic:str):
    return call_model(generate_plan_prompt(topic))