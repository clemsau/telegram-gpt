from telegram import BotCommand
from telegram.ext import (
    AIORateLimiter,
    Application,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from handlers import message_handler, reset_handler, mention_handler
from src.config import allowed_telegram_users, openai_api_key, telegram_token
from src.openai_utils import Chat

openai_instance: Chat = Chat(openai_api_key)


async def post_init(application: Application) -> None:  # type: ignore
    await application.bot.set_my_commands(
        [
            BotCommand("/reset", "reset the conversation"),
            BotCommand("/mention", "toggle answer on mention"),
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

    user_filter = filters.ALL
    if len(allowed_telegram_users) > 0:
        user_filter = filters.User(user_id=allowed_telegram_users)

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND & user_filter, message_handler
        )
    )
    application.add_handler(
        CommandHandler("reset", reset_handler, filters=user_filter)
    )
    application.add_handler(
        CommandHandler("mention", mention_handler, filters=user_filter)
    )

    application.run_polling()


if __name__ == "__main__":
    run_bot()
