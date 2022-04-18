"""
This module contains a Battleship object for creating and running a game of Battleship.
"""
from display_tools import clear_screen, close_window, set_window_size
from player import Player


class Battleship:
    """
    Contains game logic and functionality for running a text-based version of Battleship in console.
    """

    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.winner = None
        self.loser = None

    def run_game(self):
        """Launch game main menu"""
        set_window_size(108, 60)
        print(TITLE)
        start_options = {
            "play": self._play,
            "rules": self._display_rules,
            "quit": close_window,
        }
        option_prompt(start_options)

    def _play(self):
        """Start Battlship game"""
        player_setup(self.player1)
        player_setup(self.player2)

        # Game loop
        while True:
            play_turn(self.player1, self.player2)
            if all(ship.sunk for ship in self.player2.ships):
                print(f"{self.player1.name.upper()} WINS!")
                return False
            play_turn(self.player2, self.player1)
            if all(ship.sunk for ship in self.player1.ships):
                print(f"{self.player2.name.upper()} WINS!")
                return False

    def _display_rules(self):
        """Create window displaying game rules"""
        print(RULES)
        input("Press any key to continue")
        clear_screen()
        self.run_game()


def player_setup(player: Player):
    """Run player setup functions"""
    clear_screen()
    player.set_name()
    player.place_ships()


def play_turn(current_player: Player, opponent: Player):
    """Run all steps for a player's turn"""
    target = current_player.choose_target()
    result = opponent.receive_attack(target)
    current_player.record_attack(target, result)


def option_prompt(options: dict):
    """Display a list of options and execute based on user input

    options: a dictionary where each key is the option name, and each value
    is the callback function to be executed
    """
    print("OPTIONS:\t" + "\t".join(options.keys()).upper())
    option_choice = input(">>> ").lower().strip()
    if option_choice in options.keys():
        options[option_choice]()
    else:
        print("Invalid option")
        option_prompt(options)


# GAME TEXT

TITLE = r"""
        Welcome to...
         ______   _______ __________________ _        _______  _______          _________ _______ 
        (  ___ \ (  ___  )\__   __/\__   __/( \      (  ____ \(  ____ \|\     /|\__   __/(  ____ )
        | (   ) )| (   ) |   ) (      ) (   | (      | (    \/| (    \/| )   ( |   ) (   | (    )|
        | (__/ / | (___) |   | |      | |   | |      | (__    | (_____ | (___) |   | |   | (____)|
        |  __ (  |  ___  |   | |      | |   | |      |  __)   (_____  )|  ___  |   | |   |  _____)
        | (  \ \ | (   ) |   | |      | |   | |      | (            ) || (   ) |   | |   | (
        | )___) )| )   ( |   | |      | |   | (____/\| (____/\/\____) || )   ( |___) (___| )
        |/ \___/ |/     \|   )_(      )_(   (_______/(_______/\_______)|/     \|\_______/|/

                                                 Another amazing text-based game by JOE RYBARCZYK
        
Ready to play?
        """

RULES = """
        OBJECT:
        Be the first to sink all 5 of your opponent's ships.
        
        SETUP:
        At the start of the game, each player will secretly place their 5 ships on their ship grid.
        Each ship must be placed such that:
            - The ship is aligned horizontally or vertically, not diagonally
            - The ship does not overlap the area of the grid, or any other ship.

        HOW TO PLAY:
        On your turn, pick a coordinate on your opponent's grid. If it's a "hit", an "X" will be 
        markedon your guess grid and your opponent's ship grid. If it's a "miss", a "O" will be marked on
        each grid.

        Once all the coordinates of any ship are hit, the ship has been sunk. Sink all 5 of your
        opponent's ships to win the game!
        """
