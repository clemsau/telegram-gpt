import typing
from enum import Enum


class Author(Enum):
    USER = "user"
    ASSISTANT = "assistant"


class Discussion(object):
    def __init__(self, start_prompt: str):
        self.messages = [{"role": "system", "content": start_prompt}]

    def add_message(self, author: Author, message: str) -> None:
        self.messages.append({"role": author.value, "content": message})

    def get_messages(self) -> typing.List[typing.Dict[str, str]]:
        return self.messages

    def reset_discussion(self, start_prompt: str) -> None:
        self.messages = [{"role": "system", "content": start_prompt}]
