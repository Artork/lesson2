#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# Превратите строку "01/01/25 12:10:03.234567" в объект datetime


from datetime import datetime, timedelta
day_now = datetime.now()
print(day_now)
delta_one_day = timedelta(days=1)
delta_30_day = timedelta(days=30)
day_yesterday = day_now - delta_one_day
day_30_days_ago = day_now - delta_30_day
print(day_yesterday)
print(day_30_days_ago)