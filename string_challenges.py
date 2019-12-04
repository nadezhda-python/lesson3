# Вывести последнюю букву в слове
word = 'Архангельск'
print (word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print (word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

def count_vowel_letter(word):
    vowel_letter = ('а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'е')
    vowel_letter_amount = 0
    for letter in word:
        if letter.lower() in vowel_letter:
            vowel_letter_amount += 1
    return vowel_letter_amount

print(count_vowel_letter(word))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

def first_letter(word):
    return word[0]

print(' '.join(list(map(first_letter, sentence.split()))))


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
len_list = list(map(len, sentence.split()))
print(sum(len_list)/len(len_list))
