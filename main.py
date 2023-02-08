import os
import telebot
import tempfile
import webbrowser as wb
import ctypes
import keyboard
from PIL import ImageGrab


API_TOKEN = '6162186995:AAEK2PL1NGoYzKhIhx-IliRGZMnuC8e9Q0A'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Управление ПК')
    markup.add("Браузер")
    markup.add('Sound')
    bot.send_message(message.chat.id, '👋', reply_markup=markup)

@bot.message_handler(regexp='Управление ПК')
def man(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот")
    markup.add("Блокировка")
    markup.add("Выключить")
    markup.add("Перезагрузить")
    markup.add('/start')
    bot.send_message(message.chat.id, 'sound menu', reply_markup=markup)

def send_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('volume up')
    markup.add('volume down')
    markup.add('/start')
    bot.send_message(message.chat.id, 'sound menu', reply_markup=markup)

@bot.message_handler(regexp='Sound')
def send_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('volume up')
    markup.add('volume down')
    markup.add('/start')
    bot.send_message(message.chat.id, 'sound menu', reply_markup=markup)

@bot.message_handler(regexp='Браузер')
def send_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("YouTube")
    markup.add("Вконтакте")
    markup.add("Яндекс")
    markup.add('/start')
    bot.send_message(message.chat.id, 'хуй', reply_markup=markup)

@bot.message_handler(regexp='volume up')
def echo_message(message):
    keyboard.send("volume up")
    bot.send_message(message.chat.id, 'Повысил громкость')

@bot.message_handler(regexp='volume down')
def echo_message(message):
    keyboard.send("volume down")
    bot.send_message(message.chat.id, 'Убавил громность')

@bot.message_handler(regexp='Блокировка')
def echo_message(message):
    bot.send_message(message.chat.id, 'Блокирую Windows...')
    ctypes.windll.user32.LockWorkStation()
    print('lock')

@bot.message_handler(regexp='Вконтакте')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю Вконтакте...')
    wb.open('https://vk.com/')

@bot.message_handler(regexp='YouTube')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю YouTube...')
    wb.open('https://youtube.com/')

@bot.message_handler(regexp='Яндекс')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю браузер...')
    wb.open('http://ya.ru')

@bot.message_handler(regexp='Перезагрузить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Перезагружаю...')
    os.system("shutdown -r -t 0")

@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("shutdown -s -t 0")

@bot.message_handler(regexp='Получить скриншот')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))

bot.infinity_polling()