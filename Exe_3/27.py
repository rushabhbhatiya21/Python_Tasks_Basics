from datetime import datetime, timedelta

today = datetime.now()

first_day_of_month = today.replace(day=1)

last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1) - timedelta(days=1))

print(f"The first day of the current month is: {first_day_of_month.strftime('%Y-%m-%d')}")
print(f"The last day of the current month is: {last_day_of_month.strftime('%Y-%m-%d')}")
