#534222844:AAGyVhmc054SgxXakpO7QArqoNxsHM98B4w

import telebot
import builtwith


bot = telebot.TeleBot("534222844:AAGyVhmc054SgxXakpO7QArqoNxsHM98B4w")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bw = builtwith.parse('https://'+message.text)
        for key, val in bw.items():
            k = key
            v = val
            msg = (k+str(v))
            bot.reply_to(message, msg)

bot.polling()
