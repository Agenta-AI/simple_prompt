import os

import openai
from agenta import FloatParam, TextParam, post
import agenta as ag
from fastapi import Body

agenta.init()
ag.config.default(
    temperature=FloatParam(0.9),
    prompt_template=TextParam("Summarize the following text: {text}")
)

@post
def generate(
    text: str
) -> str:
    prompt = ag.config.prompt_template.format(text=text)
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}, temperature=ag.config.temperature]
    )

    result = chat_completion.choices[0].message.content
    return result
