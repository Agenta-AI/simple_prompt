import openai
import agenta as ag

ag.init()
ag.config.default(
    temperature=ag.FloatParam(0.9),
    prompt_template=ag.TextParam("Summarize the following text: {text}"),
)


@ag.entrypoint
def generate(text: str) -> str:
    prompt = ag.config.prompt_template.format(text=text)
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=ag.config.temperature,
    )

    result = chat_completion.choices[0].message.content
    return result
