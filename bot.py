import telebot 
from log import get_location, weather
from Tocen import tocen

bot = telebot.TeleBot(tocen)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "/weather":
        bot.send_message(message.from_user.id, "Введите названия запрашиваемого города")
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, "Введите команду: /weather")

def get_weather(message):
    citys = message.text
    try: 
        wc = weather(citys)
        bot.send_message(message.from_user.id, f'В городе {citys} в данный момент {round(ws[0]["temp"])} градусов,'f'чувствуется как {round(ws[0]["feels_like"])} градусов')
        bot.send_message(message.from_user.id, wс[1])
        bot.send_message(message.from_user.id, "Введите названия запрашиваемого города")
        bot.register_next_step_handler(message, get_weather)
    except Exception:
        bot.send_message(message.from_user.id, "Такого города нет в базе данных")
        bot.send_message(message.from_user.id, "Введите снова название города")
        bot.register_next_step_handler(message, get_weather)

bot.polling(none_stop=True, interval=0)


