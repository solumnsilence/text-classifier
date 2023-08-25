from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import filters
from telegram.ext import MessageHandler

from services.classifier.service import Classifier
from services.classifier.service import Text
from services.telegram_bot.settings import TelegramBotSettings

classifier = Classifier()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Send me a russian sentence and I will classify it!')


async def classify(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""

    await update.message.reply_text(classifier.classify(Text(update.message.text)))


if __name__ == '__main__':
    settings = TelegramBotSettings()
    app = ApplicationBuilder().token(settings.token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters=filters.TEXT, callback=classify))

    app.run_polling()
