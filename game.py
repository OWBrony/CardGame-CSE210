from card import Card
class Game:
    def __init__(self):
        self.score = 300
        self.turns = 0

    def play(self):
        first_Card = Card
        second_Card = Card
        # Need to generate a random card (handled by Card)
        first_Card.value = Card.draw_Card(self)
        print(f"The card is: {first_Card.value}")
        hold_First = first_Card.value
        # Need to ask the user for a guess of high or low
        player_Guess = input("Next card higher or lower (h/l)? ")
        # Generate a new card
        second_Card.value = Card.draw_Card(self)
        print(f"The card is: {second_Card.value}")
        hold_Second = second_Card.value
        # Compare new card to old card AND player's guess
        # award or penalize points according to correctness of guess
        if player_Guess.lower()[0] == "h" and hold_Second > hold_First:
            self.score += 100
        elif player_Guess.lower()[0] == "l" and hold_Second < hold_First:
            self.score += 100
        else:
            self.score -= 75
        # Show the player their score
        print(f"Your score is: {self.score}")
        pass
