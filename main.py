import telebot
import time

TOKEN = "5439725443:AAHwW8XYKyiJd8wyQQlwbIOozTNxjpecBTI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)

@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello mother fucker😏🍆")

@bot.message_handler(commands=["img"])
def image(message):
    img = open("Images\\NoBitches.png", "rb")
    bot.send_photo(message.chat.id, img)

while True:
    try:
        bot.polling()
    except:
        time.sleep(5)