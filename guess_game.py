'''
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number,
tell them they've guessed correctly and how many guesses it took!
'''
import random

print('WELCOME TO THE GUESSING GAME!')
print('Read your instructions below and have fun!')
print('THe computer will select a number between 1 and 100, how fast can you guess the number?!')


N = random.randint(1, 100)
# print('+++++++++++++++++ {} ++++++++++++++++++'.format(n))
NUM = int(input('Guess a number between 1 and 100: '))
GUESS = 1

if N == NUM:
    print('Correct!!! you took {} guesses'.format(GUESS))
elif NUM <= 0 or NUM > 100:
    print("Out of bounds")
elif NUM in range(N-10, N+10):
    print('WARM!')
else:
    print('COLD!')
PREV = NUM
while True:
    NUM = int(input('Guess again: '))
    GUESS = GUESS + 1
    if N == NUM:
        print('Correct!!! you took {} guesses'.format(GUESS))
        break
    elif NUM < 0 or NUM > 100:
        print("Out of bounds")
    elif abs(NUM - N) < abs(PREV - N):
        print('WARMER!')
        PREV = NUM
    else:
        print('COLDER!')
        PREV = NUM
