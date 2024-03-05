from datetime import datetime, timedelta

after_month = datetime.today() + timedelta(days=30)
print(f'Date after 1 week: {after_month.strftime("%d/%m/%Y")}')
