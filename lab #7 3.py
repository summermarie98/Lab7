import random
rand = random.randint(0,50)
guessing = True
while (guessing == True):
    print "Please, guess the number?"
    userInput = int(raw_input())
    if userInput > rand:
        print "I'm sorry, but your answer is too high!"
    elif userInput < rand:
        print "I'm sorry, but your answer is too low!"
    elif userInput == rand:
        print "Yay! You answered correctly!"
        userInput = rand
        guessing = False