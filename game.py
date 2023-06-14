from food import Food
from snake import Snake
from screen import Screen
import os

import pygame
pygame.init()
pygame.font.init()

class Game:
    def __init__( self, all_settings ):

        self.all_settings = all_settings
        self.settings = all_settings['game']
        self.running = True
        self.playing = False
        self.clock = pygame.time.Clock()

        self.screen = Screen( self, self.all_settings['screen'] )
        self.load_logo_files()

    def get_score( self ):
        return len(self.snake)

    def load_logo_files( self ):
        
        filenames = os.listdir( './' + self.settings['LOGOS_FOLDER'] )
        self.logo_files = []
        for filename in filenames:
            self.logo_files.append( os.path.abspath( os.path.join('.', self.settings['LOGOS_FOLDER'], filename ) ) )

    def play( self ):

        while self.running:

            # See if user clicked "X" on the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                
            # see if the user pressed a key            
            if pygame.key.get_focused():
                keys = pygame.key.get_pressed()

                if self.playing:                
                    self.snake.process_key_press( keys )
                
                if not self.playing: # See if user pressed enter to start game
                    if keys[pygame.K_RETURN]:
                        self.playing = True
                        self.loop_start_time = pygame.time.get_ticks()

                        # initialize a new start!
                        self.snake = Snake( self, self.all_settings['snake'] )
                        self.food = Food( self, self.all_settings['food'] )

            self.screen.fill()
            self.screen.draw()

            # if we are past the main menu
            if self.playing:
                
                # if enough time has passed for the snake to move
                current_time = pygame.time.get_ticks()
                if (current_time - self.loop_start_time) > (1000/self.snake.settings['SPEED']):
                    self.loop_start_time = current_time
                
                    # move the snake
                    self.snake.move()

                # draw 
                self.snake.draw()
                self.food.draw()
           
            self.screen.draw_score()
           
            # update the screen's display to show the changes
            self.screen.flip()
            self.clock.tick( self.settings['FPS'] )
            
        pygame.quit()  