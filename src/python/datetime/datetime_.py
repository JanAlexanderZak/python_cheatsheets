from datetime import datetime, timedelta
import locale

# Format
d = datetime(year=2020, month=11, day=17, hour=8, minute=30, second=00)
print(d.strftime("%A, der %d. %B %Y"))
print(d.strftime("%d.%m.%Y %H:%M"))

# Local time
locale.setlocale(locale.LC_ALL, "de_DE")
print(d.strftime("%A, der %d. %B %Y"))

# Time difference
print(d + timedelta(hours=4, days=2))

# Time
dt = datetime.now()


