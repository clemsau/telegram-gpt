from telegram import BotCommand, Update
from telegram.ext import (
    AIORateLimiter,
    Application,
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
)

from src.config import openai_api_key, telegram_token
from src.openai_utils import OpenAIUtils


async def post_init(application: Application) -> None:  # type: ignore
    await application.bot.set_my_commands(
        [
            BotCommand("/hello", "respond hello"),
        ]
    )


def run_bot() -> None:
    application = (
        ApplicationBuilder()
        .token(telegram_token)
        .concurrent_updates(True)
        .rate_limiter(AIORateLimiter(max_retries=5))
        .post_init(post_init)
        .build()
    )

    openai_instance = OpenAIUtils(openai_api_key)

    async def hello(update: Update, context: CallbackContext) -> None:  # type: ignore
        answer: str = await openai_instance.complete(
            [
                {"role": "system", "content": "You are a joyful assistant."},
                {"role": "user", "content": "Hello world!"},
            ]
        )
        await update.message.reply_text(answer)  # type: ignore

    application.add_handler(CommandHandler("hello", hello))

    application.run_polling()


if __name__ == "__main__":
    run_bot()
