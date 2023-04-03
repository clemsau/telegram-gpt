from telegram import Update, User
from telegram.ext import CallbackContext

import config
from src.entity import ON_MENTION_ACTIVATE, ON_MENTION_DEACTIVATE
from src.bot import openai_instance


async def message_handler(update: Update, context: CallbackContext) -> None:  # type: ignore
    message: str = update.message.text
    bot: User = await context.bot.get_me()
    bot_username = bot.username
    if config.answer_on_mention and "@" + bot_username not in message:
        return

    if openai_instance.handle_timeout():
        await update.message.reply_text("⚠ Conversation reset due to timeout.")

    await update.message.chat.send_action(action="typing")
    answer: str = await openai_instance.complete(message)
    await update.message.reply_text(answer)  # type: ignore


async def reset_handler(update: Update, context: CallbackContext) -> None:  # type: ignore
    openai_instance.reset()
    await update.message.reply_text("Conversation reset.")


async def mention_handler(update: Update, context: CallbackContext) -> None:  # type: ignore
    config.answer_on_mention = not config.answer_on_mention
    if config.answer_on_mention:
        bot: User = await context.bot.get_me()
        bot_username = bot.username
        await update.message.reply_text(ON_MENTION_ACTIVATE.format(bot_username))
        return
    await update.message.reply_text(ON_MENTION_DEACTIVATE)
