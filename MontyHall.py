import random

class MontyHall:
    options = [1, 2, 4]
    def __init__(self, iterations=10000000):
        self.win_mantain = 0
        self.win_change = 0
        self.iterations = iterations

    def calculate(self):
        for _ in range(self.iterations):
            prize = random.choice(self.options)
            election = random.choice(self.options)
            # this is the problem key: because presenter can only choice a lost option when u dont choose the prize
            presenter_options = [x for x in self.options if x != prize and x != election]
            presenter_choice = random.choice(presenter_options)
            new_reduced_option = [x for x in self.options if x != presenter_choice]
            player_choice_maintain = [x for x in new_reduced_option if x == election]
            player_choice_change = [x for x in new_reduced_option if x != election]
            if player_choice_maintain[0] == prize:
                self.win_mantain += 1
            if player_choice_change[0] == prize:
                self.win_change += 1

        print(f'Win mantain election = {self.win_mantain/self.iterations*100}%')
        print(f'Win change election = {self.win_change/self.iterations*100}%')


def main():
    MontyHall().calculate()


if __name__ == "__main__":
    main()
