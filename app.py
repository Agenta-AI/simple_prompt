import os

import openai
from agenta import FloatParam, TextParam, post
from fastapi import Body

default_prompt = "Summarize the following text: {text}"


@post
def generate(
    text: str,
    temperature: FloatParam = FloatParam(0.9),
    prompt_template: TextParam = default_prompt,
) -> str:
    prompt = prompt_template.format(text=text)
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    result = chat_completion.choices[0].message.content
    return result
