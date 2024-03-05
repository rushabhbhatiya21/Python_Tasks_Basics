from datetime import date, timedelta

today = date.today()
tomorrow = date.today() + timedelta(days=1)
print(f'Difference between tomorrow and today: {tomorrow - today}')
