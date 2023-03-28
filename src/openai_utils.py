import typing

import openai

OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


class OpenAIUtils:
    def __init__(self, openai_api_key: str) -> None:
        openai.api_key = openai_api_key
        self.model = "gpt-3.5-turbo"

    async def complete(self, messages: typing.List[typing.Dict[str, str]]) -> str:
        response = await openai.ChatCompletion.acreate(  # type: ignore
            model=self.model, messages=messages, **OPENAI_COMPLETION_OPTIONS
        )
        return response.choices[0].message["content"]  # type: ignore
