from random import randint

class Casino:
    def play(self, bet):
        print(f"Ваша ставка = {bet}.")
        dice1 = randint(1,6)
        print(f"Число на першому кубику = {dice1}.")
        dice2 = randint(1,6)
        print(f"Число на другому кубику = {dice2}.")
        total = dice1 + dice2

        if dice1 == dice2:
            if dice1 == 5:
                return bet*6
            else:
                return bet*2
        elif total == 10 or total == 11:
            return bet*3
        elif total == 6 or total == 7:
            return bet
        else:
            return 0