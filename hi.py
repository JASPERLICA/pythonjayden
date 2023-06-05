import math
import time
import random


Wrong_answer = "incorrect"

invaild_answer = 1

player1 = input ("enter player one's name: ")
player2 = input ("enter player two's name: ")


num =random.randint(-100,100)


if num >=0:
    print ("Postive or Zero")
else:
    print ("Negtive Number")
if num >=75:
    print ("-greater than or equal to 75")
else:
    print ("-less than 75")
if num >=50:
    print ("-greater than or equal to 50")
else:
    print ("-less than 50")
if num >=25:
    print ("-great than or equal to 25")
else:
    print ("-less than 25")
if num >=-25:
    print ("-greater than or equal to  -25")
else:
    print ("-less than -25")
if num >=-50:
    print ("-greater than or equal to -50")
else:
    print ("-less than -50")
if num >=-75:
    print ("-greater than or equal to -75")
else:
    print ("-less than -75")

print ("    instructions: writing your guessing number below acording to hints given above the range of the random number is from -100 to 100. Whoever guesses the number cloest to the random number, wins.")

guessing_number1 = input("Enter player 1 number (between -100 to 100): ")
guessing_number2 = input("Enter player 2 number (between -100 to 100): ")

player_one_wins = (num - int(guessing_number1)) < (num - int(guessing_number2))
player_two_wins = (num - int(guessing_number1)) > (num - int(guessing_number2))

if player_one_wins:
    print (player1 + " wins")
    print ("The random number is: "+ str (num))
elif player_two_wins:
    print (player2 + " wins")
    print ("The random number is: "+ str (num))

