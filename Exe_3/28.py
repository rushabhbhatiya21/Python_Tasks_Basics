from datetime import datetime, timedelta

today = datetime.now()

first_day_of_month = today.replace(day=1)

last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1) - timedelta(days=1))


def format_date(date):
    suffix = "th" if 11 <= date.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(date.day % 10, "th")
    formatted_date = date.strftime(f"%d{suffix} %B %Y %A %I:%M:%S %p")
    return formatted_date


# Print the formatted first and last date of the current month
print("Formatted first day of the current month:", format_date(first_day_of_month))
print("Formatted last day of the current month:", format_date(last_day_of_month))
