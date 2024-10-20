import os
import telebot
import random
bot = telebot.TeleBot('7680128280:AAErh1tDaAxxG175WCPS-5Ji2RQagBVtTT0')
@bot.message_handler(commands=['eco'])
def eco(message):
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    with open(f'images/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используй команду eco или eco 2 или eco 3 чтобы получить больше интересных фактов об экологии!")
    
@bot.message_handler(commands=['eco 2'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! не все знаёт об экологии очень много но её нужно всеми силами беречь:сдавать мусор на перероботку, меньше рубить леса,озеленять планету, и не тратить ресурсы природы зря!")
@bot.message_handler(commands=['eco 3'])
def start_command(message):
    bot.send_message(message.chat.id, "зачем нам экология? она нужна чтобы продлить всем нам жизнь, чтобы мы спокойно дышали свежим воздухом!")

bot.polling()
