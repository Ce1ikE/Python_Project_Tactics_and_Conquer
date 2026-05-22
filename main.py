"""
Entry point for Tactics and Conquer.
Run this module to launch the game.

+==========+========================+===========+
| Project: |  Game                  |           |
| Name:    |  Tactics & Conquer     |           |
| Authors: |  Crollet W.            | Celik E.  |
+==========+========================+===========+

TODO:
[] Add more dataclasses to replace this kind of dictionaries and lists with more structured data
[] Add enums to replace the string literals with more structured data
[] classes subpackage can be more seperated based on the category of the class, for example we can have all UI related classes in a UI subpackage, 
   all game logic related classes in a GameLogic subpackage and so on, 
   this will help us with the organization of the code and make it easier to navigate through the codebase
[] Use Typing to add type hints to all the variables and functions in the game, this will help us with debugging and understanding the code better 


"""

from tactics_and_conquer import Game

TAC = Game()

if __name__ == "__main__":
    TAC.run()
    