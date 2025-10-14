import json
import re
from typing import List

from ollama import chat
from ollama import ChatResponse
from dataclasses import dataclass

generate_plan_prompt = lambda topic: "You are a math teatcher. You can use latex. Create a course outline on the given topic :" + topic + """The course should be divided into chapters, each with a title and a brief description. Ensure the content is clear, concise, and suitable for beginners.
Please respond ONLY with a JSON matching exactly the following schema (no explanation, no extra text, no formatting tags):

{
  "title": "string",
  "chapters": [
    {
      "title": "string",
      "description": "string"
    }
  ]
}

Make sure the JSON is valid and parsable.
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