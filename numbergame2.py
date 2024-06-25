import random
print('Please enter your name: ')
Name=input()

print('well! ' + Name + ' I`m thinking of a number between 1 to 10')

secretNumber= random.randint(1, 10)

for guesstaken in range(1, 6):
    print('Take a guess')
    guess=int(input())
    
    if guess > secretNumber:
        print('too high')
    elif guess < secretNumber:
        print('too low')
    else:
        break

if guess==secretNumber:
    print('good job, ' +Name+ ' you guessed in ' +str(guesstaken)+ ' attempts')
else:
    print('Betterluck next time number was ' +str(secretNumber))
