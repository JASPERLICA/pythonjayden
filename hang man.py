import random
import sys


print(""" Welcome to "word guesser". You have have 15 turns to guess the unknow word.
Every turn you cans guess a letter and you will get a response. You can ask for
a hint but that will take up 5 turns, good luck! """)


transporation = ["truck","aircraft","cab"]
city = ["uberization","condo","park"]
nature = ["trees","earth", "deforestation"]       
turn = 10
words = ["truck","uberization","deforestation","aircraft",
         "condo", "earth","cab", "trees"]
difficulty = input("choose your difficulty (easy, medium, hard): ")
invaild_answer = "invaild answer"
tempwords = []

if difficulty == "hard":
    for word in words:
        if len (str(word)) >= 6:
            tempwords.append(word)
        else:
            pass
elif difficulty == "medium":
    for word in words:
        if len (str(word)) == 5:
            tempwords.append(word)
        else:
            pass
elif difficulty == "easy":
    for word in words:
        if len (str(word)) <= 4:
            tempwords.append(word)
        else:
            pass
else:
    print (invaild_answer)
    difficulty = input("choose your difficulty (easy, medium, hard): ")
    turn = turn - 1
    if turn == 0:
        sys.exit()


vowels = 0
consonants = 0
turns = 15

the_word = random.choice(tempwords)

for letter in the_word:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter =="":
        pass
    else:
        consonants = consonants + 1

your_input = input("enter your letter/guess or ask for a hint: ")


while turns !=0:
    if your_input == the_word:
        print ("you got the word. you win the game!!!!!")
        break
    elif your_input in the_word:
        turns = turns-1
        print ("the letter is in the word")
        your_input = input("enter your letter/guess or ask for a hint: ")
    elif your_input == "hint":
        turns = turns - 5
        print ("There are {} vowels".format(vowels))
        print ("There are {} consonants".format(consonants))
        if the_word in transporation:
            print ("The word has to do with transporation")
        elif the_word in nature:
            print ("the word has to do with nature or could be found in nature")
        else:
            print ("the word has to do with cities or could be found in cities")
        your_input = input("enter your letter/guess or ask for a hint: ")
    elif your_input == "hack":
        password = input("what is th password: ")
        if password == "harrison has a wife":
            print ("password accpeted. Here is the word:",the_word)
            your_input = input("enter your letter/guess or ask for a hint: ")
        else:
            while True:
                print ("hackers are not allowed")
    elif your_input not in the_word:
        turns = turns-1
        print ("the letter is not in the word")
        your_input = input("enter your letter/guess or ask for a hint: ")

if turns == 0:
    print ("Game over. Reasoning: you run out of turns")
    print ("the word was ", the_word)
