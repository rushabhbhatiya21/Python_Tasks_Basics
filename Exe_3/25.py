from datetime import datetime

today = datetime.now()
first_day_of_year = today.replace(month=1, day=1)

print(f"The first day of the first month of the current year is: {first_day_of_year.strftime('%Y-%m-%d')}")
