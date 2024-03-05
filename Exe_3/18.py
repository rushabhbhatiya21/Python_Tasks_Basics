from datetime import date, datetime

print(f'Using datetime: {datetime.now().date().strftime("%d/%m/%Y")}')
print(f'Using date:     {str(date.today())}')
