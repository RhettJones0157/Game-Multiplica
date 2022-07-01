print("This is a multiplication game! Answer as many multiplication problems you can correctly, choosing size and choice.")
print()
import time
import random
answers = 0
seconds = int(input("How many seconds would you like to give yourself? "))
numbar = int(input("What is the largest possible number you would like to use? "))
print()
count = 1
while count < seconds:
  time.sleep(1)
  count += 1

  digit1 = random.randint(1, numbar)
  digit2 = random.randint(1, numbar)
  product = digit1 * digit2
  question = int(input("What is " + str(digit1) + " times " + str(digit2) + "? "))
  if question == product:
    answers += 1
    print("Nice job!")
  else:
    print("Moving on...")

print("You got " + answers + "answers in " + seconds + "seconds!")
  
