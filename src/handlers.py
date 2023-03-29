from telegram import Update
from telegram.ext import CallbackContext

from src.bot import openai_instance


async def message_handler(update: Update, context: CallbackContext) -> None:  # type: ignore
    message: str = update.message.text
    await update.message.chat.send_action(action="typing")
    answer: str = await openai_instance.complete(message)
    await update.message.reply_text(answer)  # type: ignore


async def reset_handler(update: Update, context: CallbackContext) -> None:  # type: ignore
    openai_instance.reset()
    await update.message.reply_text("Conversation reset.")
