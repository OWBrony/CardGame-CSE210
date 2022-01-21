import random
# create template for cards to run on
class Card:
    # hold the value of a card
    def __init__(self):
        self.value = 0

    def draw_Card(self):
        self.value = random.randint(1,13)
        return self.value
    