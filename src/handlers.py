import tempfile
from pathlib import Path

import pydub
from telegram import Update, User
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

import config
from bot import openai_instance
from entity import ON_MENTION_ACTIVATE, ON_MENTION_DEACTIVATE


async def message_handler(
    update: Update, context: CallbackContext, message=None
) -> None:
    if not message:
        message: str = update.message.text
    bot: User = await context.bot.get_me()
    bot_username = bot.username
    if config.answer_on_mention and "@" + bot_username not in message:
        return

    if openai_instance.handle_timeout():
        await update.message.reply_text("⚠ Conversation reset due to timeout.")

    await update.message.chat.send_action(action="typing")
    answer: str = await openai_instance.complete(message)
    await update.message.reply_text(answer)


async def voice_handler(update: Update, context: CallbackContext) -> None:
    if config.answer_on_mention:
        return

    if openai_instance.handle_timeout():
        await update.message.reply_text("⚠ Conversation reset due to timeout.")

    voice = update.message.voice
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        voice_ogg_path = tmp_dir / "voice.ogg"

        voice_file = await context.bot.get_file(voice.file_id)
        await voice_file.download_to_drive(voice_ogg_path)

        voice_mp3_path = tmp_dir / "voice.mp3"
        pydub.AudioSegment.from_file(voice_ogg_path).export(
            voice_mp3_path, format="mp3"
        )

        with open(voice_mp3_path, "rb") as f:
            message = await openai_instance.transcribe(f)

    text = f"🎤: <i>{message}</i>"
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)

    await message_handler(update, context, message)


async def reset_handler(update: Update, context: CallbackContext) -> None:
    openai_instance.reset()
    await update.message.reply_text("Conversation reset.")


async def mention_handler(update: Update, context: CallbackContext) -> None:
    config.answer_on_mention = not config.answer_on_mention
    if config.answer_on_mention:
        bot: User = await context.bot.get_me()
        bot_username = bot.username
        await update.message.reply_text(ON_MENTION_ACTIVATE.format(bot_username))
        return
    await update.message.reply_text(ON_MENTION_DEACTIVATE)
