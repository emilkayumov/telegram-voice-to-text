import io
import logging

from faster_whisper import WhisperModel
from telegram import Update, Message
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
)
import yaml


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# turn off logging for name httpx level info
logging.getLogger("httpx").setLevel(logging.WARNING)

CONFIG_PATH = "config.yaml"
MODEL_SIZE = "large-v2"
MODEL = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")


async def download_voice(
    message: Message, context: ContextTypes.DEFAULT_TYPE
) -> io.BytesIO:
    # get the file id
    file_id = message.voice.file_id
    audio = await context.bot.get_file(file_id)

    # create a buffer to store the audio file in write mode
    buffer = io.BytesIO()
    await audio.download_to_memory(out=buffer)
    buffer.seek(0)

    return buffer


def transcript_voice_generator(model: WhisperModel, buffer: io.BytesIO):
    segments, _ = model.transcribe(buffer)
    return segments


async def transcript_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"User {update.effective_chat.username} sent an audio file")

    buffer = await download_voice(update.message, context)
    logging.info("Audio file downloaded")

    logging.info("Start transcribing")
    segments = transcript_voice_generator(MODEL, buffer)

    for segment in segments:
        message = f"[{segment.start} -> {segment.end}] {segment.text}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    logging.info("Transcribing finished")
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="The voice message has been transcribed"
    )


if __name__ == "__main__":
    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.safe_load(config_file)

    bot_token = config["bot_token"]
    allowlist_usernames = None
    if "allowlist_usernames" in config:
        allowlist_usernames = config["allowlist_usernames"]

    application = ApplicationBuilder().token(bot_token).build()

    message_filters = filters.VOICE
    if allowlist_usernames:
        message_filters = message_filters & filters.Chat(username=allowlist_usernames)

    application.add_handler(
        MessageHandler(
            filters=message_filters,
            callback=transcript_handler,
        )
    )

    application.run_polling()
