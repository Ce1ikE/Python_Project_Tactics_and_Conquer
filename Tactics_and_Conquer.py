from classes.ClassGame import Game

# here starts the game / ici le jeu commence / hier begint het spel

# so comments in this game files are in dutch or either english 
# because this a personal project. YES, i am aware that it's not a good practise but 
# this is my game.

# if you are not familiar with tile based game, sprites or gamboy games
# i recommend this video: at 09:50 is exactly the same concept how i "blit" my pygame.Surfaces to the screen
# https://www.youtube.com/watch?v=BKm45Az02YE
# if you watched the video you might have noticed that the gameboy uses 8x8 sprites, well being in the 21th century allows my to use any size 
# of sprites and scale it up or down the way i want to.

TAC = Game()
# zie python les 
if __name__ == "__main__":
    TAC.run()
    