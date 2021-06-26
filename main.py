print("Hello, welcome to the pomodoro timer.")

t = str(input("Do you want to enter your working time in minutes or hours?"))
print("Great,:)")

if t == "minutes":
  m = int(input("How many minutes do you want to work for?"))
  print(m, "This is how many minutes you'll be working today.")
    
elif t == "hours":
  hours = int(input("How many hours do you want to work for?"))
  m = hours * 60
  print(m, "This is how many minutes you'll be working today.")

short_break = 0
long_break = 1
Ctime = m 

import time

while (Ctime > 0):
    print('Time remaining:', Ctime)
    print("Starts to work now!")
    Ctime = Ctime - 25
    m = 25 * 60
    while m:
     mins = m // 60 
     secs = m % 60
     timer = '{:02d}:{:02d}'.format(mins,secs)
     print("Working Time Countdown:", timer, end = "\r")
     time.sleep(1)
     m -= 1
    print('Time remaining:', Ctime)
    print("Great Job, you are taking a short break!")
    Ctime = Ctime - 5
    m = 5 * 60
    while m:
      mins = m // 60 
      secs = m % 60
      timer = '{:02d}:{:02d}'.format(mins,secs)
      print("Short Break Countdown:", timer, end = "\r")
      time.sleep(1)
      m -= 1
    print('Time remaining:', Ctime)
    short_break = short_break + 1 
    if short_break %4 == 0:
      print("You are taking the long break!")
      Ctime = Ctime - 30
      m = 30 * 60
      while m:
        mins = m // 60 
        secs = m % 60
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print("Long Break Countdown:", timer, end = "\r")
        time.sleep(1)
        m -= 1

print("Time over")