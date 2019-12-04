from datetime import datetime, timedelta

#Напечатайте в консоль даты: вчера, сегодня, месяц назад

today_datetime = datetime.now()
today = today_datetime.strftime('%Y-%m-%d')
yesterday = (today_datetime - timedelta(days=1)).strftime('%Y-%m-%d')
month_ago = (today_datetime - timedelta(days=30)).strftime('%Y-%m-%d')

print(f'сегодня {today}, вчера было {yesterday}, месяц назад было {month_ago}')

#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

date_string = '01/01/17 12:10:03.234567'
print (datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f').strftime('%Y-%m-%d'))