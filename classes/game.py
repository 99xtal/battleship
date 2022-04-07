from .player import Player

class Game():
    def __init__(self):
        self.players = [Player('Player 1'), Player('Player 2')]

    def display_intro_text(self):
        print('''
        Welcome to...
         ______   _______ __________________ _        _______  _______          _________ _______ 
        (  ___ \ (  ___  )\__   __/\__   __/( \      (  ____ \(  ____ \|\     /|\__   __/(  ____ )
        | (   ) )| (   ) |   ) (      ) (   | (      | (    \/| (    \/| )   ( |   ) (   | (    )|
        | (__/ / | (___) |   | |      | |   | |      | (__    | (_____ | (___) |   | |   | (____)|
        |  __ (  |  ___  |   | |      | |   | |      |  __)   (_____  )|  ___  |   | |   |  _____)
        | (  \ \ | (   ) |   | |      | |   | |      | (            ) || (   ) |   | |   | (      
        | )___) )| )   ( |   | |      | |   | (____/\| (____/\/\____) || )   ( |___) (___| )      
        |/ \___/ |/     \|   )_(      )_(   (_______/(_______/\_______)|/     \|\_______/|/ 

                                                 Another terrible text-based game by JOE RYBARCZYK''')
    
    def run_player_setup(self):
        for player in self.players:
            player.run_setup()

    def run_game(self):
        self.display_intro_text()
        self.run_player_setup()


game = Game()
game.run_game()
