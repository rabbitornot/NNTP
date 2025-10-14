import re
from ollama import chat
from ollama import ChatResponse
from dataclasses import dataclass

generate_plan_prompt = lambda topic: "You are a math teatcher. Create a course outline on the given topic :" + topic + """The course should be divided into chapters, each with a title and a brief description. Ensure the content is clear, concise, and suitable for beginners.
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

@dataclass
class Chapter:
    title:str
    description:str

@dataclass
class Course:
    title:str
    chapters: list[Chapter]


def call_model(request: str):
    response: ChatResponse = chat(model='qwen3:0.6b', messages=[
    {
        'role': 'user',
        'content': request,
    },
    ])

    re.sub(r'<think>.*?</think>', '', response['message']['content'], flags=re.DOTALL)


print(call_model(call_model(generate_plan_prompt)))
