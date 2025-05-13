import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

RESPONSES = ["хорошо", "плохо", "понял", "❤", "👍"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  

    if "как дела" in text:
        reply = "нормально"
    elif "что делаешь" in text or "что ты делаешь" in text:
        reply = "сижу на работе"
    elif "привет" in text or "здравствуйте" in text:
        reply = "привет"
    elif "что кушал" in text or "что ты кушал" in text:
        reply = "суп и котлету"
    elif "кого любишь" in text or "кого любит" in text:
        reply = "Викту"
    elif "доброе утро" in text:
        reply = "доброе"
    elif "спокойной ночи" in text or "доброй ночи" in text:
        reply = "спокойной ночи"
    else:
        reply = random.choice(RESPONSES)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token("7932982787:AAG_G7O5PYGSUljTuQz7H-yL3OlJy6_De9I").build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()  # <- БЕЗ await и БЕЗ asyncio.run

if __name__ == "__main__":
    main()   

