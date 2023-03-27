from telegram import BotCommand
from telegram.ext import AIORateLimiter, Application, ApplicationBuilder, CommandHandler

from src.config import telegram_token


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

    application.add_handler(
        CommandHandler(
            "hello", lambda update, context: update.message.reply_text("Hello!")
        )
    )

    application.run_polling()


if __name__ == "__main__":
    run_bot()
