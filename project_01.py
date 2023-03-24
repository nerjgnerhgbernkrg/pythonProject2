import telebot
import config
ask = "6093798510:AAGIAoq6rjRDq5HKAYH4UwY_fNqwXZhZYRw"
bot = telebot.TeleBot(ask)
@bot.message_handler(content_types=['text'])
def la(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)
