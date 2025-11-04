import random
def num_rounds():
    try:
        r = int(input("What score do you want to play for?:"))
        if r > 0:
            return r
        else:
            print("enter a positive number.")
            return num_rounds()
    except ValueError:
        print("Please enter a valid number")
        return num_rounds()
def game():
    number_of_rounds = num_rounds()
    items = ('scissors','paper','rock')
    your_points = 0
    bots_points = 0
    while your_points < number_of_rounds and bots_points < number_of_rounds:
        bot = random.choice(items)
        you = input(f'enter your item{items}:').lower()
        if bot == you:
            print(f"Bot chose: {bot}")
            print(f'draw! You:{your_points}/bot:{bots_points}')
        elif bot == 'paper' and you == 'scissors':
            your_points += 1
            print(f"Bot chose: {bot}")
            print(f'You won! You:{your_points}/bot:{bots_points}')
        elif bot == 'paper' and you == 'rock':
            bots_points += 1
            print(f"Bot chose: {bot}")
            print(f'You lost! You:{your_points}/bot:{bots_points}')
        elif bot == 'scissors' and you == 'paper':
            bots_points += 1
            print(f"Bot chose: {bot}")
            print(f'You lost! You:{your_points}/bot:{bots_points}')
        elif bot == 'scissors' and you == 'rock':
            your_points += 1
            print(f"Bot chose: {bot}")
            print(f'You won! You:{your_points}/bot:{bots_points}')
        elif bot == 'rock' and you == 'paper':
            your_points += 1
            print(f"Bot chose: {bot}")
            print(f'You won! You:{your_points}/bot:{bots_points}')
        elif bot == 'rock' and you == 'scissors':
            bots_points += 1
            print(f"Bot chose: {bot}")
            print(f'You lost! You:{your_points}/bot:{bots_points}')
        else:
            print('enter again')
    if your_points > bots_points:
        print(f'you are a champion! you won by a score of: You:{your_points}/bot:{bots_points}')
    elif your_points < bots_points:
        print(f'This time the bot was lucky, try again!')
    else:
        print('You are a draw!')
    if input('Do you want to play again? (yes/no): ').lower() == 'yes':
        game()
if __name__ == '__main__':
    game()
