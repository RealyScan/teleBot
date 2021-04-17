# coding utf8

import random
import pyowm
import telebot
from pyowm.utils.config import get_default_config
from telebot import types

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('fb586fa657b6d921aabef1596e4e57e7', config_dict)
bot = telebot.TeleBot("1647750345:AAG3GGFhpfPyl223AFsbPanBk_DT_NpN9dM", parse_mode=None)
while True:
    @bot.message_handler(commands=['погода'])

    def echo_all(message):
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Владивосток")
        w = observation.weather
        weather_info = "В городе Владивосток сейчас " + w.detailed_status + "\n"
        weather_info += "Температура: " + str(w.temperature('celsius')['temp']) + "\n"
        weather_info += "Скорость ветра: " + str(w.wind()['speed']) + " м/с" + "\n"
        bot.reply_to(message, weather_info)







    @bot.message_handler(commands=['подскажи'])

    def echo_all(message):
        adjectives = {}
        i=0
        for line in open('adjectives.txt'):
            line = line.split('\n')  # из строки получаем список
            #adjectives[line[0]] = line[1:]  # добавляем в словарь
            #adjectives[line[0]] = i  # добавляем в словарь
            adjectives[i] = line[0]
            i+=1
            # первый элемент списак - как ключ
            # остальные - значение
        adjnum=len(adjectives)
        adjran=int(random.uniform(0,adjnum))


        substantives = {}
        j=0
        for line in open('substantives.txt'):
            line = line.split('\n')  # из строки получаем список
           # substantives[line[0]] = line[1:]  # добавляем в словарь
            substantives[j] = line[0]
            # первый элемент списак - как ключ
            # остальные - значение
            j+=1
        subnum=len(substantives)
        subran=int(random.uniform(0,subnum))

        print(substantives.get(subran))
        print(str(adjectives.get(adjran)) + " " + str(substantives.get(subran)))

        answer=str(adjectives.get(adjran)) + " " + str(substantives.get(subran))
        bot.reply_to(message, answer)


    '''
    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message == "Ананас":
            bot.reply_to(message, " обормот")




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
