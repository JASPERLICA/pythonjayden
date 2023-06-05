import random

num = random.randint(-100, 100)

wrong_answer = "Invaild answer"
Invaild_answer = 1


if num >= 0:
    print("Postive or Zero")
else:
    print("Negtive Number")
if num >= 75:
    print("greater than or equal to 75")
else:
    print("less than 75")
if num >= 50:
    print("greater than or equal to 50")
else:
    print("less than 50")
if num >= 25:
    print("great than or equal to 25")
else:
    print("less than 25")
if num >= -25:
    print("greater than or equal to  -25")
else:
    print("less than -25")
if num >= -50:
    print("greater than or equal to -50")
else:
    print("less than -50")
if num >= -75:
    print("greater than or equal to -75")
else:
    print("less than -75")

guessing_number = input("Enter your number (between -100 to 100):")

if guessing_number == num:
    print("correct")
elif guessing_number !=num:
    print("incorrect")
else:
    print(wrong_answer)

while wrong_answer:
    Invaild_answer+1
    print(wrong_answer)
    if Invaild_answer >=10:
        break

print("The random number is: " + str(num))
