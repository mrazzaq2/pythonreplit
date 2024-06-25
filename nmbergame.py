#This is a guess number game!
import random

Name=input('what is your name?\n')

print('Well!', Name, 'I`m thinking of a number between 1 to 10')

SecretNumber = random.randint(1, 10)

for guesses in range(5):
    print('Take a guess.')
    guess = int(input())


    if guess < SecretNumber:
        print('number is too low')
    elif guess > SecretNumber:
        print('number is high')
    else:
        break # this is for correct guess

if guess == SecretNumber:
    print('good job,' + Name + ' you guessed the number in ' + str(guesses) + ' guess' )
else:
    print('nope! the guessed number was,' + str(SecretNumber))
