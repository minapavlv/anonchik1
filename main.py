import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = '7893409112:AAFXaQh3JAOkRLHmETmS1eatCORigMQRCrE'
YOUR_CHAT_ID = 6624984494

logging.basicConfig(level=logging.INFO)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message:
            await context.bot.forward_message(
                chat_id=YOUR_CHAT_ID,
                from_chat_id=update.message.chat_id,
                message_id=update.message.message_id
            )
    except Exception as e:
        print(f"Ошибка: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_message))
app.run_polling()
