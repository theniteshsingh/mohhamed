from datetime import datetime

seatcapacity= 100
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

if current_time=="00:00:00":
    seatcapacity= 80

print(seatcapacity)

