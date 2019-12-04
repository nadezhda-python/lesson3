import secret
import logging
import ephem
import re
from datetime import datetime
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
"""

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def planet_constellation(planet):
    if planet == 'Mercury':
        return ephem.constellation(ephem.Mercury(datetime.today()))
    elif planet ==  'Venus':
        return ephem.constellation(ephem.Venus(datetime.today()))
    elif planet ==  'Earth':
        return ephem.constellation(ephem.Earth(datetime.today()))
    elif planet ==  'Mars':
        return ephem.constellation(ephem.Mars(datetime.today()))
    elif planet ==  'Jupiter':
        return ephem.constellation(ephem.Jupiter(datetime.today()))
    elif planet ==  'Saturn':
        return ephem.constellation(ephem.Saturn(datetime.today()))
    elif planet ==  'Uranus':
        return ephem.constellation(ephem.Uranus(datetime.today()))
    elif planet ==  'Neptune':
        return ephem.constellation(ephem.Neptune(datetime.today()))
    elif planet ==  'Pluto':
        return ephem.constellation(ephem.Pluto(datetime.today()))
    else:
        return 'Incorrect planet name, try again please'


def planet_location(bot, update):
    planet = update.message.text.split()[-1].capitalize()
    print(planet)
    result = planet_constellation(planet)
    print(result)
    update.message.reply_text(result)


def get_next_full_moon(user_text):
    try:
        return ephem.next_full_moon(user_text)
    except ValueError:
        return 'Wrong date, try again please in format 1970-01-01 or 1970/01/01'


def next_full_moon(bot, update):
    user_date = update.message.text.split()[-1]
    print(user_date)
    result = get_next_full_moon(user_date)
    print(result)
    update.message.reply_text(result)


def word_count_function(text):
    if text == '':
        return 'It is empty string!'
    else:
        text = re.sub('\W', ' ', text)
        return len(text.split())


def word_count(bot, update):
    text = update.message.text
    text = re.sub('^/wordcount', '', text)
    result = word_count_function(text)
    print(text, result)
    update.message.reply_text(result)


#берем список городов из файла
virgin_city_list = []
with open('city.txt', encoding='utf-8') as file:
    for city in file:
        virgin_city_list.append(city.strip())
#сохраняем нетронутый список городов и создаем список для игры
city_list = virgin_city_list.copy()
#чтобы города выдаваемые ботом шли не в алфавитном порядке
random.shuffle(city_list)
output_city = ''


#проверяем что новый город начинается с последней буквы последнего
def valid_city_for_game_step(input_city, last_output_city):
    input_first_letter = input_city.replace('ё', 'е').replace('й', 'и').replace('ь', '').lower()[0]
    last_output_last_letter = last_output_city.replace('ё', 'е').replace('й', 'и').replace('ь', '').lower()[-1]
    if input_first_letter == last_output_last_letter:
        return True
    else:
        return False


def city_game(input_city):
    global output_city
    global city_list
    global virgin_city_list
    #дали на вход не город
    if input_city.capitalize() not in virgin_city_list:
        return ('Я не знаю такого города, попробуйте еще :)')
    #такой город уже был
    if input_city.capitalize() not in city_list:
        return ('У нас уже был этот город! Давай что-то другое')
    #проверяем что город пользователя начинается с нашей последней буквы
    if output_city != '' and not valid_city_for_game_step(input_city, output_city):
        return (f'Первая буква не {output_city.replace("ё", "е").replace("й", "и").replace("ь", "").lower()[-1]}, давай что-то другое.')
    city_list.remove(input_city.capitalize())
    #если слово оканчивается на мягкий знак берем предпоследнюю букву
    for city in city_list:
        if valid_city_for_game_step(city, input_city):
            output_city = city
            break 
        else:
            output_city = 'Я не могу больше ничего придумать, ты победил!'
    city_list.remove(output_city)
    return output_city


def cities(bot, update):
    global output_city
    global city_list
    global virgin_city_list
    text = update.message.text
    input_city = re.sub('^/cities', '', text).strip()
    if input_city == 'стоп':
        message = 'Ок, конец так конец.'
        print (message)
        update.message.reply_text(message)
        output_city = ''
        city_list = virgin_city_list.copy()        
    else:
        print(input_city)
        output_city_for_user = city_game(input_city)
        print (output_city_for_user)
        update.message.reply_text(output_city_for_user)


def main():
    mybot = Updater(secret.key)
    #, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_location))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       
if __name__ == "__main__":
    main()
