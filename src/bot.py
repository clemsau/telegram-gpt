from telegram import BotCommand
from telegram.ext import (
    AIORateLimiter,
    Application,
    ApplicationBuilder,
    MessageHandler,
    filters,
)

import handlers
from src.config import openai_api_key, telegram_token
from src.openai_utils import Chat

openai_instance: Chat = Chat(openai_api_key)


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

    application.add_handler(MessageHandler(filters.TEXT, handlers.message_handler))  # type: ignore

    application.run_polling()


if __name__ == "__main__":
    run_bot()
