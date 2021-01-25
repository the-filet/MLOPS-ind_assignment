from datetime import date
from datetime import datetime

today = date.today()
print("Today it is: ",today)

time_now = datetime.now()
print("Timestamp: ",time_now.strftime("%H:%M:%S"))

