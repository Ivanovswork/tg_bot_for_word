import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=['ret'])
def main(message):
    print(type(message.chat.id))
    bot.send_message(message.chat.id, "Привет")
    doc = open("../data/result_file.docx", 'rb')
    bot.send_document(message.chat.id, doc)


bot.polling(none_stop=True)