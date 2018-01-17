# ---------------------------------------using time
import time
from datetime import datetime
ticktock = time.time()
print("number of ticks:", ticktock)
presentTime = datetime.now()
print("now the time is :", presentTime)
print("Todays date is ", presentTime.strftime('%Y-%m-%d'))
print("month is ", presentTime.month);
print("year is ", presentTime.year);
print("day is ", presentTime.day);
# ______________________________________________get curr time
curtime = time.localtime(time.time())
print("current time is ",curtime);
