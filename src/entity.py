import datetime
import typing
from enum import Enum

DEFAULT_TIMEOUT = datetime.timedelta(minutes=20)
DEFAULT_PROMPT = "You are a general assistant."
ON_MENTION_ACTIVATE = "The bot will now answer only when mentioned with @{}"
ON_MENTION_DEACTIVATE = "The bot will now answer to every message"
SWITCH_MODEL = "Switched to model {}"


class Author(Enum):
    USER = "user"
    ASSISTANT = "assistant"


class Discussion(object):
    def __init__(self, start_prompt: str = DEFAULT_PROMPT):
        self.messages = [{"role": "system", "content": start_prompt}]
        self.start_time = datetime.datetime.now()

    def add_message(self, author: Author, message: str) -> None:
        self.messages.append({"role": author.value, "content": message})

    def get_messages(self) -> typing.List[typing.Dict[str, str]]:
        return self.messages

    def reset_discussion(self, start_prompt: str = DEFAULT_PROMPT) -> None:
        self.messages = [{"role": "system", "content": start_prompt}]

    def handle_timeout(self, start_prompt: str = DEFAULT_PROMPT) -> bool:
        if datetime.datetime.now() - self.start_time > DEFAULT_TIMEOUT:
            self.reset_discussion(start_prompt)
            return True
        return False
