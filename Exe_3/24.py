from datetime import datetime, timedelta

today = datetime.now()

first_day_of_month = today.replace(day=1)

print(f"The first day of the current month is: {first_day_of_month.strftime('%Y-%m-%d')}")
