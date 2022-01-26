"""
Hilo Game
by: Caleb Hatch
"""
import random


class Player:
    def __init__(self, points):
        self.points = points


class GameEndConditions:
    global game_second_card, player_guess

    @staticmethod
    def win_condition():
        print("The card was " + str(game_second_card) + ", and you guessed " + str(
            player_guess) + ". You got it!")
        print("")
        player.points = (player.points + 100)

    @staticmethod
    def loss_condition():
        print("The card was " + str(game_second_card) + ", and you guessed " + str(player_guess) +
              ". Better luck next time!")
        print("")
        player.points = (player.points - 75)

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
                GameEndConditions.win_condition()
            elif player_guess == str("h"):
                GameEndConditions.loss_condition()
        elif game_first_card < game_second_card:
            if player_guess == str("h"):
                GameEndConditions.win_condition()
            elif player_guess == str("l"):
                GameEndConditions.loss_condition()

        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")

        if player.points <= 0:
            print("Your score reached below zero!")
            GameEndConditions.player_end_state()

        if user_retry == str("y"):
            game_loop = True
            continue
        else:
            GameEndConditions.player_end_state()


if __name__ == "__main__":
    global game_second_card, player_guess
    main()
