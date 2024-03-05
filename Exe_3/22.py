from datetime import datetime, timedelta


def is_leap_year(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    return leap


def get_days():
    if is_leap_year(datetime.today().year - 1):
        return 366
    return 365


after_year = datetime.today() + timedelta(days=get_days())
print(f'Date after 1 week: {after_year.strftime("%d/%m/%Y")}')
