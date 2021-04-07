import pyowm
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('fb586fa657b6d921aabef1596e4e57e7', config_dict)
bot = telebot.TeleBot("1647750345:AAG3GGFhpfPyl223AFsbPanBk_DT_NpN9dM", parse_mode=None)

@bot.message_handler(commands=['погода'])

def echo_all(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place("Владивосток")
    w = observation.weather
    weather_info = "В городе Владивосток сейчас " + w.detailed_status + "\n"
    weather_info += "Температура: " + str(w.temperature('celsius')['temp']) + "\n"
    weather_info += "Скорость ветра: " + str(w.wind()['speed']) + " м/с" + "\n"
    bot.reply_to(message, weather_info)

'''
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    # print(w.wind()['speed'], w.temperature('celsius')['temp'])
    weather_info = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    weather_info += "Температура: " + str(w.temperature('celsius')['temp']) + "\n"
    weather_info += "Скорость ветра: " + str(w.wind()['speed']) + " м/с" + "\n"

    bot.reply_to(message, weather_info)
'''

bot.polling()