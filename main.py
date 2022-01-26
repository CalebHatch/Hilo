"""
Hilo Game
by: Caleb Hatch
"""
import random


# Keeps track of the amount of the player's points.
class Player:
    def __init__(self, points):
        self.points = points


# Contains the results for the three different end states of the game.
class GameEndResults:
    global game_second_card, player_guess

    # Should be used when the player guesses the card correctly. Adds 100 to score and outputs a "win" message to the
    # user.
    @staticmethod
    def win_result():
        print("Next card was " + str(game_second_card) + ", and you guessed \"" + str(
            player_guess) + "\". You got it!")
        print("")
        player.points = (player.points + 100)

    # Should be used when the player guesses the card incorrectly. Subtracts 75 from the user's score and outputs a
    # "loss" message to the user.
    @staticmethod
    def loss_result():
        print("Next card was " + str(game_second_card) + ", and you guessed \"" + str(player_guess) +
              "\". Better luck next time!")
        print("")
        player.points = (player.points - 75)

    # Should be used whenever the game should be ended. Outputs a "game over" message to the user and uses the "quit()"
    # command to end the program.
    @staticmethod
    def player_end_state():
        global game_loop
        print("Game over!\nGoodbye.")
        quit()


player = Player(300)

game_loop = True


def main():
    global player, game_loop, game_second_card, player_guess
    player = Player(300)

    game_loop = True

    while game_loop:
        game_first_card = random.randint(1, 13)
        print("The card is: " + str(game_first_card) + ".")

        player_guess = input("Higher or Lower? [h/l]: ")

        game_second_card = random.randint(2, 12)

        if game_first_card > game_second_card:
            if player_guess == str("l"):
                GameEndResults.win_result()
            elif player_guess == str("h"):
                GameEndResults.loss_result()
        elif game_first_card < game_second_card:
            if player_guess == str("h"):
                GameEndResults.win_result()
            elif player_guess == str("l"):
                GameEndResults.loss_result()

        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")

        if player.points <= 0:
            print("Your score reached below zero!")
            GameEndResults.player_end_state()

        if user_retry == str("y"):
            game_loop = True
            continue
        else:
            GameEndResults.player_end_state()


if __name__ == "__main__":
    global game_second_card, player_guess
    main()
