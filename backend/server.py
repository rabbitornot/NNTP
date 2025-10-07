from ollama import chat
from ollama import ChatResponse
from dataclasses import dataclass

@dataclass
class Chapter:
    title:str
    description:str

@dataclass
class Course:
    title:str
    chapters: list[Chapter]


def call_model(request: str):
    response: ChatResponse = chat(model='qwen3', messages=[
    {
        'role': 'user',
        'content': request,
    },
    ])
    return response['message']['content']



