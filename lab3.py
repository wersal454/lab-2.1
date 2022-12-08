import datetime
import math
limit=input("укажите лимит на сегодня:")
comment=input("укажите комментарий:")
ammount=input("укажите число:")
date=input("укажите дату:")
record=[]
rates={'RUB': 2.61, 'THB': 1.11, 'USD': 3.3}

class Calculator():
    def __init__(self, limit):
        self.limit = limit

class Record():
    def __init__(self, comment, amount, date):
        self.comment = comment
        self.amount = amount
        try:
            if datetime.datetime.striptime(date, '%d.%m.%Y'):
                self.date=datetime.datetime.striptime(date, '%d.%m.%Y').date()
        except:
            self.date=datetime.date.today()
    def __rec__(self):
        return f"{self.amount}-{self.comment}-{self.date}"

class Calc:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)


    def get_today_stat(self):
        res = 0
        for record in self.records:
            if record.date == datetime.date.today():
                res += record.amount
            return res


    def last_sevendays_stat(self):
        sum = 0
        onlyseven = 0
        for record in self.records:
            if onlyseven < 7:
                onlyseven += 1
                sum += record.amount
            elif onlyseven >= 7:
                break
            return sum


    def curr_date_count(self):
        dates_for_sum = input('Введите интересующие вас даты, через пробел (20.09.2011 13.09.2013) -')
        sum = 0
        sum_dates = dates_for_sum.split(' ')

        for record in self.records:

            if str(datetime.datetime.strptime(record.date, "%d.%m.%Y")) in sum_dates:
                sum += record.amount

            return sum


class CashCL(Calc):

    def __init__(self, currency, limit):
        super().__init__(limit)
        self.currency = currency

    def get_today_cash_remained(self):
        sum_for_limit = 0
        for record in self.records:
            if datetime.date.today() == record.date:
                sum_for_limit += record.amount

        if self.limit > sum_for_limit:
            for key, value in rates.items():
                if self.currency == key:
                    print(f'На сегодня осталось: {math.floor(self.limit - (sum_for_limit / value))} {key}')
        return '----------'


class CaloriesCL(Calc):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        return str(f'Ваш лимит по калориям на сегодня - {self.limit - self.get_today_stat()} ккалл.')


user = CashCL('THB', 1000)
userX = CaloriesCL(1000)
user.add_record(Record('Заправка', 30, '21.10.2021'))


userX.add_record(Record('Пробежа 10км', 300, ''))

print(user.get_today_stat())
print(user.last_sevendays_stat())
print(user.get_today_cash_remained())
print(userX.get_calories_remained())