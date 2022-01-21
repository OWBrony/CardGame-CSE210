from game import Game

def start_Game():
    play = True
    game = Game()
    while play is True:
        game.play()
        print()
        # TODO: y/n utility function
        newgame = input("The game is over. Play again? (y/n): ")
        if len(newgame) > 0 and newgame.lower()[0] == "y":
            continue
        elif len(newgame) > 0 and newgame.lower()[0] == "n":
            play = False
        else:
            print("We're going to run it again anyway.")

def main():
    print("Welcome to CardGame!")
    print()
    start_Game()
    print()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
