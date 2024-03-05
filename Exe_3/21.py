from datetime import datetime, timedelta

after_week = datetime.today() + timedelta(weeks=1)
print(f'Date after 1 week: {after_week.strftime("%d/%m/%Y")}')
