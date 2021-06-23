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
time = m

while (time > 0):
    print('Time remaining:', time)
    print("study time")
    time = time - 25
    print('Time remaining:', time)
    print("Great Job, you are taking a short break!")
    print('Time remaining:', time)
    time = time - 5
    short_break = short_break + 1 
    if short_break %4 == 0:
      print("You are taking the long break!")
      time = time - 30

print("Time over")
    
