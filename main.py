import telebot
import time
from PIL import Image
import requests
from io import BytesIO


TOKEN = "5439725443:AAHwW8XYKyiJd8wyQQlwbIOozTNxjpecBTI"      #this is the main bot
# TOKEN = "5523662071:AAGhUX6dWh7PSeBz4GfkYbZNMQPlSlAxmxc"        #this is the test bot
bot = telebot.TeleBot(TOKEN)

isStickerToPhoto = False


# @bot.message_handler(commands=["stickertophoto"])                     #fixing this part later
# def stickerToPhoto(message):
#     isStickerToPhoto = True
#     bot.send_message(message.chat.id, "Now send your sticker...")

@bot.message_handler(content_types=["sticker"])
def convertStickerToPhoto(message):
    # print(isStickerToPhoto)
    if True:            #changing this to response activation
        bot.send_message(message.chat.id, "Converting...")
        response = requests.get(bot.get_file_url(message.sticker.file_id))
        img = Image.open(BytesIO(response.content))
        bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)

@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello mother fucker😏🍆")

@bot.message_handler(commands=["img"])
def image(message):
    img = open("picture.png", "rb")
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=["sogand"])
def sogand(message):
    bot.send_message(message.chat.id, "عه سلاممم کونییییی😂🍆🍆🍆🍆")

@bot.message_handler(regexp="mother fucker")
def motherfucker(message):
    bot.send_message(message.chat.id, "no no no you are the mother fucker")

while True:
    try:
        bot.polling()
    except:
        time.sleep(5)