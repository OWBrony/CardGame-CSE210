from game import Game

def main():
    print("Welcome to CardGame!")
    print()
    while True:
        game = Game()
        game.play()
        print()
        # TODO: y/n utility function
        newgame = input("The game is over. Play again? (y/n): ")
        if len(newgame) > 0 and newgame.lower()[0] == "y":
            continue
        break
    print()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
