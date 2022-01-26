import random


class Player:
    def __init__(self, points):
        self.points = points


player_1 = Player(300)
player_2 = Player(300)

player_1_turn = True

while player_1_turn:
    print("Player 1 has " + str(player_1.points) + " points.")
    print("Player 2 has " + str(player_2.points) + " points.")
    print("")

    random_number = random.randint(1, 9)

    player_1_num = input("Guess a number (1-9): ")
    player_1_num = int(str(player_1_num))

    if player_1_num < random_number:
        player_1.points = (player_1.points - 75)
        print("")
        print("The card was " + str(random_number) + ", and you guessed " + str(player_1_num) +
              ". Better luck next time!")

    if player_1_num > random_number:
        player_1.points = (player_1.points + 100)
        print("")
        print("The card was " + str(random_number) + ", and you guessed" + str(player_1_num) + ". You got it!")

    if player_1.points >= 400:
        print("")
        print("Your score was " + str(player_1.points) + ". You win!")
        print("")
        player_1_turn = False
        break
