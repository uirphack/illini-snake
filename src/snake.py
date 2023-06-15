from src.base import Base
from src.square import Square
import src.utils as utils
import pygame
import os

class Snake( Base ):

    KEY_DIRECTIONS = {
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
        pygame.K_UP: "up",
        pygame.K_DOWN: "down"
    }

    OPPOSITE_DIRECTIONS = {
        "left":"right",
        "right":"left",
        "up":"down",
        "down":"up"
    }
    
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )

        # initialize the snake body with one square
        self.body = [ Square( int(self.game.screen.settings['LENGTH']/2), 
            int(self.game.screen.settings['WIDTH']/2) )
        ]
        
        self.logo_image = utils.load_logo_file(  os.path.abspath( self.settings['HEAD_PATH'] ), self.settings['WIDTH'] )
        self.eating_Sound = pygame.mixer.Sound(self.settings['EATING_SOUND_PATH']) 

        self.nourishment_left = 0

        self.direction = None

    def __len__( self ):

        """overrides len() operator"""
        return len(self.body)

    def process_key_press( self, keys ):
        """process the keys pressed"""

        if keys[pygame.K_z]: #exit entire program
            self.game.running = False

        if keys[pygame.K_r]: #restart game
            self.game.playing = False

        for key in Snake.KEY_DIRECTIONS:
            if keys[ key ]:
                direction = Snake.KEY_DIRECTIONS[ key ]
                opposite_direction = Snake.OPPOSITE_DIRECTIONS[ direction ]
                
                if opposite_direction != self.momentum_direction:
                    self.direction = direction

    def move( self ):
        
        self.momentum_direction = self.direction
        
        self._add_to_head()
        self._check_ate_food()
        self._check_remove_tail()

        if self._hit_boundaries():
            self.game.game_over()
            return
        if self._hit_self():
            self.game.game_over()
            return

    def _add_to_head( self ):

        """add another point to body in whatever direction snake is facing"""
        head = self.body[0]

        if self.direction == 'right':
            new_Sqaure = Square( head.x+1, head.y )
        elif self.direction == 'left':
            new_Sqaure = Square( head.x-1, head.y )
        elif self.direction == 'up':
            new_Sqaure = Square( head.x, head.y-1 ) #y-axis points down
        elif self.direction == 'down':
            new_Sqaure = Square( head.x, head.y+1 )
        else:
            new_Sqaure = Square( head.x, head.y )

        self.body.insert( 0, new_Sqaure )

    def _hit_boundaries( self ) -> bool:

        """check if snake head hits the boundaries"""
        
        head = self.body[0]
        if head.x < 0: 
            print ('You hit the left side!')
            return True
        elif head.x >= self.game.screen.settings['LENGTH']: 
            print ('You hit the right side!')
            return True
        if head.y < 0: 
            print ('You hit the top!')
            return True
        elif head.y >= self.game.screen.settings['WIDTH']:
            print ('You hit the bottom!')
            return True
        return False

    def _hit_self( self ) -> bool:

        """check if snake head hits another part of the body"""
        for i in range(1, len(self.body)):
            if self.body[0].is_collision( self.body[i] ):
                print ('You hit yourself!')
                return True            
            
        return False

    def _check_ate_food( self ):

        if self.body[0].is_collision( self.game.food.square ):
            print ('nom nom nom')
            self.nourishment_left += self.game.food.settings['NOURISHMENT']
            self.game.food.get_square()
            pygame.mixer.Sound.play( self.eating_Sound )

    def _check_remove_tail( self ):
        
        if self.nourishment_left > 0:
            self.nourishment_left -= 1            
        else:
            del self.body[-1]

    def draw( self ):
        
        for square in self.body:
            square.draw( self.game.screen, self.settings['COLOR'], self.settings['WIDTH'] )

        self.body[0].draw_image( self.logo_image, self.game.screen, self.settings['WIDTH'] )
