from src.base import Base
from src.square import Square
import random

class Food( Base ):
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )

        self.get_square()
    
    def get_square( self ):

        #try randomly picking a spot the snake is not on
        for i in range(0):
            x = random.randint( 0, self.game.screen.settings['LENGTH']-1 )
            y = random.randint( 0, self.game.screen.settings['WIDTH']-1 )
            self.square = Square( x, y )

            good_food = True
            for square in self.game.snake.body:
                if self.square.is_collision( square ):
                    good_food = False
                    break

            if good_food:
                return
        
        # try every possibility
        possibilities = self.game.screen.food_options.copy()
        for square in self.game.snake.body:
            possibilities.remove( [square.x, square.y] )
        
        if len(possibilities) > 0:
            choice = random.choice( possibilities )
            self.square = Square( choice[0], choice[1] )
        
        self.logo_image = random.choice( self.game.logo_images )

    def draw( self ):
        self.square.draw_image( self.logo_image, self.game.screen, self.settings['WIDTH'] )
