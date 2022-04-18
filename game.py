from player import Player


class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def display_intro_text(self):
        print(
            """
        Welcome to...
         ______   _______ __________________ _        _______  _______          _________ _______ 
        (  ___ \ (  ___  )\__   __/\__   __/( \      (  ____ \(  ____ \|\     /|\__   __/(  ____ )
        | (   ) )| (   ) |   ) (      ) (   | (      | (    \/| (    \/| )   ( |   ) (   | (    )|
        | (__/ / | (___) |   | |      | |   | |      | (__    | (_____ | (___) |   | |   | (____)|
        |  __ (  |  ___  |   | |      | |   | |      |  __)   (_____  )|  ___  |   | |   |  _____)
        | (  \ \ | (   ) |   | |      | |   | |      | (            ) || (   ) |   | |   | (      
        | )___) )| )   ( |   | |      | |   | (____/\| (____/\/\____) || )   ( |___) (___| )      
        |/ \___/ |/     \|   )_(      )_(   (_______/(_______/\_______)|/     \|\_______/|/ 

                                                 Another amazing text-based game by JOE RYBARCZYK"""
        )

    # def player1_turn(self):
    #     target = self.player1.choose_target()
    #     result = self.player2.receive_attack(target)
    #     self.player1.record_attack(result)

    # def player2_turn(self):
    #     target = self.player2.choose_target()
    #     result = self.player1.receive_attack(target)
    #     self.player2.record_attack(result)

    def run_game(self):
        #  Game setup
        self.display_intro_text()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

        # while True:
        #     self.player1_turn()
        #     if not self.player2.has_ships:
        #         print(f'{self.player1.name.upper()} WINS!')
        #         return False
        #     self.player2_turn()
        #     if not self.player1.has_ships:
        #         print(f'{self.player2.name.upper()} WINS!')
        #         return False
