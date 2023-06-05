import threading
import time
import random

def timer():
    time.sleep(delay_time)

x = threading.Thread(target=timer)

difficulty = input("chose your difficulty(easy, medium, hard): ")
easy_modules = [ "+","-"]
medium_modules = ["-", "x"]
other_modules = ["x","/"]

if difficulty == "easy":
    x = random.randint(1,20)
    y = random.randint(1,20)
    delay_time = (10)
    module = random.choice(easy_modules)
elif difficulty == "medium":
    y = random.randint(21,100)
    x = random.randint(21,100)
    delay_time = (30)
    module = random.choice(medium_modules)
else:
    x = random.randint(101,200)
    y = random.randint(101,200)
    delay_time = (60)
    module = random.choice(other_modules)

equation = ("{} {} {}")


your_answer = input("type your answer: ")


print (answer)


