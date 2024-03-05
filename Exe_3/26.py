from datetime import datetime, timedelta

today = datetime.now()

first_day_of_month = today.replace(day=1)

start_day_of_week = (first_day_of_month.weekday() - 1) % 7

start_date = first_day_of_month - timedelta(days=start_day_of_week)

current_month_dates = [start_date + timedelta(days=i) for i in range(7)]

print("Dates of the current month starting from Monday to Sunday:")
for date in current_month_dates:
    print(date.strftime('%Y-%m-%d'))
