import openai

from entity import Author
from src.entity import Discussion

OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


class Chat:
    def __init__(self, openai_api_key: str) -> None:
        openai.api_key = openai_api_key
        self.model = "gpt-3.5-turbo"
        self.discussions = Discussion()

    async def complete(self, message: str) -> str:
        self.discussions.add_message(Author.USER, message)
        response = await openai.ChatCompletion.acreate(  # type: ignore
            model=self.model,
            messages=self.discussions.get_messages(),
            **OPENAI_COMPLETION_OPTIONS,
        )
        answer: str = response.choices[0].message["content"]
        self.discussions.add_message(Author.ASSISTANT, answer)
        return answer

    def reset(self) -> None:
        self.discussions.reset_discussion()

    def handle_timeout(self) -> bool:
        return self.discussions.handle_timeout()
