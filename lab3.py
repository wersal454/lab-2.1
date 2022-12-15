import datetime
import math

limit=input("укажите лимит на сегодня:")
comment=input(str("укажите комментарий:"))
ammount=input("укажите число:")
date=input(str("укажите дату:"))
record=[]
rates={'RUB': 1, 'THB': 1.11, 'USD': 3.3}

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

    def __init__(self, limit,date):
        self.limit = limit
        self.date = date
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
        amount_summ_of_current_date = 0

        for record in self.records:

            if str(record.date) == str(self.date):
                amount_summ_of_current_date += record.amount

            return amount_summ_of_current_date


class CashCL(Calc):

    def __init__(self, currency, limit,date):
        super().__init__(limit,date)
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
    def __init__(self, limit,date):
        super().__init__(limit,date)

    def get_calories_remained(self):
        return str(f'Ваш лимит по калориям на сегодня - {self.limit - self.get_today_stat()} ккалл.')


user = CashCL('THB', 1000,'11.15.2022')
userX = CaloriesCL(1000,'12.12.2022')
user.add_record(Record('Заправка', 30, '21.10.2021'))
userX.add_record(Record('Пробежа 10км', 0, '10.19.2022'))


print(user.get_today_stat())
print(user.last_sevendays_stat())
print(user.get_today_cash_remained())
print(userX.get_calories_remained())