"""
Hilo Game
by: Caleb Hatch
"""
import random


class Player:
    def __init__(self, points):
        self.points = points


player = Player(300)

game_loop = True
player_turn = True
player_input_loop = False


def game_over():
    global game_loop
    print("Game over!\nGoodbye.")
    quit()


while game_loop:
    game_first_card = random.randint(1, 13)
    print("The card is: " + str(game_first_card) + ".")

    player_guess = input("Higher or Lower? [h/l]: ")

    game_second_card = random.randint(2, 12)

    if game_first_card > game_second_card:
        if player_guess == str("l"):
            print("The card was " + str(game_second_card) + ", and you guessed " + str(player_guess) + ". You got it!")
            player.points = (player.points + 100)
        elif player_guess == str("h"):
            print("The card was " + str(game_second_card) + ", and you guessed " + str(player_guess) +
                  ". Better luck next time!")
            player.points = (player.points - 75)
    elif game_first_card < game_second_card:
        if player_guess == str("h"):
            print("The card was " + str(game_second_card) + ", and you guessed " + str(player_guess) + ". You got it!")
            player.points = (player.points + 100)
        elif player_guess == str("l"):
            print("The card was " + str(game_second_card) + ", and you guessed " + str(player_guess) +
                  ". Better luck next time!")
            player.points = (player.points - 75)

    print("Your score is: " + str(player.points) + ".")
    user_retry = input("Play again? [y/n]: ")

    if player.points < 0:
        print("Your score reached below zero!")
        game_over()

    if user_retry == str("y"):
        game_loop = True
        continue
    else:
        game_over()
