import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess!= random_num:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess > random_num:
            print("Sorry!, guess again. Too high!!")
        elif guess < random_num:
            print("Sorry! guess again. Too low!!")
    
    print(f'Yay! You guess the number {random_num} correctly.')

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high(h), too low(l) or correct(c)?')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f'Yay! Computer guessed the number {guess} correctly.')

guess(10)
print("")
print("Now let the computer guess your number")
print("Think a number between 1 and 15")
print("")
comp_guess(15)