import openai

from entity import Author, Discussion

OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

GPT3_5 = "gpt-3.5-turbo"
GPT4 = "gpt-4"


class Chat:
    def __init__(self, openai_api_key: str) -> None:
        openai.api_key = openai_api_key
        self.model = GPT3_5
        self.discussions = Discussion()

    async def complete(self, message: str):
        self.discussions.add_message(Author.USER, message)
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self.discussions.get_messages(),
            stream=True,
            **OPENAI_COMPLETION_OPTIONS,
        )
        answer = ""
        async for response_part in response:
            delta = response_part.choices[0].delta
            if "content" in delta:
                answer += delta.content
                yield "waiting", answer
        self.discussions.add_message(Author.ASSISTANT, answer)
        yield "done", answer

    def reset(self) -> None:
        self.discussions.reset_discussion()

    def handle_timeout(self) -> bool:
        return self.discussions.handle_timeout()

    def switch_model(self):
        if self.model == GPT3_5:
            self.model = GPT4
            return
        self.model = GPT3_5

    @staticmethod
    async def transcribe(audio_file) -> str:
        r = await openai.Audio.atranscribe("whisper-1", audio_file)
        return r["text"]
