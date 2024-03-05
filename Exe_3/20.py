from datetime import datetime


def calculate_age(birthdate):
    birthdate_obj = datetime.strptime(birthdate, '%d/%m/%Y')
    today = datetime.today()

    age = today - birthdate_obj
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    return f'You are {days} days, {months} months and {years} years old as of today.'


print(calculate_age('4/7/2003'))
