from base import Base
import pygame
import numpy as np

class Snake( Base ):
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )

        self.direction = None
        self.body = np.array( 
            [[ int(self.game.screen.settings['LENGTH']/2),  int(self.game.screen.settings['WIDTH']/2)]] 
        )
        
        self.border = (self.game.screen.settings['SQUARE_WIDTH'] - self.settings['WIDTH'])/2
        self.square_offset = np.array([
            [self.border, self.border],
            [self.border, self.game.screen.settings['SQUARE_WIDTH']-self.border],
            [self.game.screen.settings['SQUARE_WIDTH']-self.border, self.game.screen.settings['SQUARE_WIDTH']-self.border],
            [self.game.screen.settings['SQUARE_WIDTH']-self.border, self.border]
        ])
        
        
    def process_key_press( self, keys ):
        """process the keys pressed"""

        if keys[pygame.K_LEFT]:
            if self.direction != 'right':
                self.direction = 'left'
        
        if keys[pygame.K_RIGHT]:
            if self.direction != 'left':
                self.direction = 'right'

        if keys[pygame.K_DOWN]:
            if self.direction != 'up':
                self.direction = 'down'
        
        if keys[pygame.K_UP]:
            if self.direction != 'down':
                self.direction = 'up'

        if keys[pygame.K_z]:
            self.game.running = False
        if keys[pygame.K_r]:
            self.game.playing = False
        

    def move( self ):
        
        #add another square to the head, remove the tail
        head = self.body[0]

        if self.direction == 'right':
            np.insert( self.body, 0, np.array([ head[0]+1, head[0] ]) )
            print (self.body)
        
        elif self.direction == 'left':
            pass
            
        elif self.direction == 'up':
            pass
            
        elif self.direction == 'down':
            pass
        

    def draw( self ):
        
        for square in self.body:
            
            x = square[0]
            y = square[1]

            base_coordinates = np.array( [
                self.game.screen.settings['SQUARE_WIDTH'] * x,
                self.game.screen.settings['SQUARE_WIDTH'] * y,
            ] )

            coordinates = self.square_offset + base_coordinates
            
            pygame.draw.polygon( 
                self.game.screen.screen,
                self.settings['COLOR'],
                coordinates
            )
        