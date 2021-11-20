'''DONE**Alarm Clock** - A simple clock where it plays a sound after \
X number of minutes/seconds or at a particular time.'''


import datetime
from time import sleep
import pygame

pygame.init()

def ask_time():
    try:
        time = int(input("select amount of time for alarm: "))
    except:
        print("Wrong data type provided for time!")
    return time

Time = ask_time()

while True:
    unit = input("Select unit of time [H/M/S]: ").lower()

    time_now = datetime.datetime.now()

    print("The alarm was set: ", time_now.strftime("On %d %B %Y at %I:%M:%S %p"))

    if unit == 'h':
        time_ = datetime.timedelta(hours=Time)
        alarm_time = time_now+time_
        print("The alarm will remind you: ",alarm_time.strftime("On %d %B %Y at %I:%M:%S %p"))
        sleep(Time*60*60)   
        
    elif unit == 'm':
        time_ = datetime.timedelta(minutes=Time)
        alarm_time = time_now+time_
        print("The alarm will remind you: ",alarm_time.strftime("On %d %B %Y at %I:%M:%S %p"))
        sleep(Time*60)

    elif unit == 's':
        time_ = datetime.timedelta(seconds=Time)
        alarm_time = time_now+time_
        print("The alarm will remind you: ",alarm_time.strftime("On %d %B %Y at %I:%M:%S %p"))
        sleep(time_.seconds)
    
    else:
        print("Wrong Unit")
        continue

    pygame.mixer.music.load("----Enter filename for your path to a music file instead of this string---")
    pygame.mixer.music.play()
    print("ALARM RINGING!!  "*3)
    sleep(10)
    pygame.mixer.music.stop()
    break
