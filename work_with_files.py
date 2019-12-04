"""
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""
import re

def word_counter(text):
    #знаки препинания заменяем на пробелы
    text = re.sub('\W', ' ', text)
    return len(text.split())

with open('referat.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(len(data))
    print(word_counter(data))
    modified_data = data.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as file:
    file.write(modified_data)
