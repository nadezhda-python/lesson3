import ephem
import logging
import random
import re
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import secret

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

def get_next_full_moon(user_date):
    try:
        return ephem.next_full_moon(user_date)
    except ValueError:
        return 'Wrong date, try again please in format 1970-01-01 or 1970/01/01'


def get_next_full_moon_bot(bot, update):
    user_date = update.message.text.split()[-1]
    print(user_date)
    result = get_next_full_moon(user_date)
    print(result)
    update.message.reply_text(result)


def count_the_words(text):
    if text == '':
        return 'It is empty string!'
    else:
        text = re.sub('\W', ' ', text)
        return len(text.split())


def count_the_words_bot(bot, update):
    text = update.message.text
    text = re.sub('^/wordcount', '', text)
    result = count_the_words(text)
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
last_output_city = ''

def city_name_normalize(city):
    return city.replace('ё', 'е').replace('й', 'и').replace('ь', '').lower()


def validate_city_for_game_step(input_city, last_output_city):
    """проверяем что новый город начинается с последней буквы последнего"""
    input_first_letter = city_name_normalize(input_city)[0]
    last_output_last_letter = city_name_normalize(last_output_city)[-1]
    if input_first_letter == last_output_last_letter:
        return True
    else:
        return False


def play_cities(input_city):
    global last_output_city
    global city_list
    global virgin_city_list
    #дали на вход не город
    if input_city.capitalize() not in virgin_city_list:
        return ('Я не знаю такого города, попробуйте еще :)')
    #такой город уже был
    if input_city.capitalize() not in city_list:
        return ('У нас уже был этот город! Давай что-то другое')
    #проверяем что город пользователя начинается с нашей последней буквы
    if last_output_city != '' and not validate_city_for_game_step(input_city, last_output_city):
        return (f'Первая буква не {city_name_normalize(last_output_city)[-1]}, давай что-то другое.')
    city_list.remove(input_city.capitalize())
    #если слово оканчивается на мягкий знак берем предпоследнюю букву
    for city in city_list:
        if validate_city_for_game_step(city, input_city):
            last_output_city = city
            break 
        else:
            last_output_city = 'Я не могу больше ничего придумать, ты победил!'
    city_list.remove(last_output_city)
    return last_output_city


def play_cities_bot(bot, update):
    global last_output_city
    global city_list
    global virgin_city_list
    text = update.message.text
    input_city = re.sub('^/cities', '', text).strip()
    if input_city == 'стоп':
        message = 'Ок, конец так конец.'
        print (message)
        update.message.reply_text(message)
        last_output_city = ''
        city_list = virgin_city_list.copy()        
    else:
        print(input_city)
        output_city = play_cities(input_city)
        print (output_city)
        update.message.reply_text(output_city)


def main():
    mybot = Updater(secret.key)
    #, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("wordcount", count_the_words_bot))
    dp.add_handler(CommandHandler("next_full_moon", get_next_full_moon_bot))
    dp.add_handler(CommandHandler("cities", play_cities_bot))
    
    mybot.start_polling()
    mybot.idle()
       
if __name__ == "__main__":
    main()
