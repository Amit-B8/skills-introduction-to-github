# Fishing Simulator
 
import random
import time

class Player:
    def __init__(self):
        self.money = 0
        self.name = "Player"
    
    def updateMoney(self, amount):
        self.money += amount

    def decreaseMoney(self , amount):
        self.money -= amount       

class Game:
    def __init__(self, player):
        self.player = player
    
    def startGame(self):
        keepFishing = input("Click Any button to fish again or 'S' to shop: ")
        while (keepFishing.lower() != 's'):
            seconds = random.randint(1, 20)
            print("Wait for the fish to appear and click 'f' or 'F' to catch fish")
            #Pause the game for how ever many random seconds
            time.sleep(seconds)
            print(f'Fish appeared! Press "F" within 2 seconds to catch it!')
            # Keep track of how long is seconds it takes player to catch
            startTime = time.time()
            playerInput = input("Press 'F' to catch the fish: ")

            if (playerInput == "F" or playerInput == "f") and time.time() - startTime <= 2:
                print("You caught the fish!")
                keepFishing = input("Click Any button to fish again or 'S' to shop: ")
                if seconds < 5:
                    self.player.updateMoney(5)
                    print(f"Your current money: {self.player.money}")
                elif seconds < 10:
                    self.player.updateMoney(10)
                    print(f"Your current money: {self.player.money}")
                else:
                    self.player.updateMoney(15)
                    print(f"Your current money: {self.player.money}")
            else:
                print("You missed the fish!")
                print(f"Your current money: {self.player.money}")

class Shop:
    def __init__(self, player):
        self.player = player
        self.minigames = Minigames(player)
    
    def visit_shop(self):
        option = input("Press 'S' to go to the shop or 'E' to leave: ")
        if option.lower() == "s":
            print("Welcome to the shop!")
            choice = input("click 1 for mini-game which cost $20: ")
            if choice == "1" and self.player.money >= 20:
                self.player.decreaseMoney(20)
                print ("You bought a mini-game")
                self.minigames.miniGame1()
            elif self.player.money < 20:
                print("You don't have enough money for the mini-game pass.")
            else:
                print("Invalid choice. Please try again.")
        elif option.lower() == "e":
            print("Leaving the shop.")
        else:
            print("Invalid option. Please try again.")

class Minigames:
    def __init__(self,player):
        self.player = player 

    def miniGame1(self):
        print ("This is a game where you can guess the randomly generated number out of 10 to earn money")
        number = random.randint(1,10)
        play = input("Click P to play if you guess right earn $60: ")
        if play.lower() == "p":
            guess = input ("Type the random number generated from 1 - 10:  ")
            if int(guess) == number:  # Ensure the guess is converted to an integer for comparison
                print(f"You guessed correctly! The number was: {number}")
                self.player.updateMoney(60)
                print(f"Your current money: {self.player.money}")
            else:
                print(f"You guessed wrong. The random number was: {number}")
                print(f"Your current money: {self.player.money}")


def main():
    player = Player()
    game = Game(player)
    shop = Shop(player)

    print("This is a fishing simulator where you will catch fish to earn money.")
    start = input("Click 'Y' to start the game: ")

    if start == "y" or start == "Y":
        while True:
            game.startGame()
            shop.visit_shop()
            quitGame = input("Press 'Q' to quit or any other key to continue playing: ")
            if quitGame.lower() == 'q':
                print(f"Game Over! You earned {player.money} money.")
                break

if __name__ == "__main__":
    main()
