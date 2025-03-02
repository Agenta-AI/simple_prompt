from openai import OpenAI
from pydantic import BaseModel, Field
from agenta.sdk.types import PromptTemplate

import agenta as ag
import litellm

litellm.drop_params = True
litellm.callbacks = [ag.callbacks.litellm_handler()]

ag.init()

class MyConfig(BaseModel):
    prompt: PromptTemplate = Field(
        default=PromptTemplate(
            system_prompt="You are a very good summarizer. Create summary from the following article:",
            user_prompt="{article}"
        )
    )


@ag.route("/", config_schema=MyConfig)
@ag.instrument()
async def generate(article: str) -> str:
    config = ag.ConfigManager.get_from_route(schema=MyConfig)
    response = await litellm.acompletion(
        **{
            **config.prompt.format(article=article).to_openai_kwargs(),
        }
    )
    result = response.choices[0].message.content
    return result
