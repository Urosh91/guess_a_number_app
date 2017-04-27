import random


def game():
    secret_number = random.randint(1, 10)
    guesses  = []

    while len(guesses) < 5:
        try:
            guess = int(input('Guess a number between 1 and 10: '))
        except ValueError:
            print(f'{guess} is not a number')
        else:
            if guess == secret_number:
                print(f'You got it. My number was {secret_number}')
                break
            elif guess < secret_number and 4 - len(guesses) > 0:
                print('Try again, my number is higher than that')
                print(f'You have {4 - len(guesses)} tries left')
            elif guess > secret_number and 4 - len(guesses) > 0:
                print('Try again, my number is lower than that')
                print(f'You have {4 - len(guesses)} tries left')
            guesses.append(guess)
    else:
        print(f"You didn't get it. My number was {secret_number}.")
    play_again = input('Do you want to play again? Y/n ')
    if play_again.lower() != 'n':
        game()
    else:
        print('Thank you for playing')

game()

