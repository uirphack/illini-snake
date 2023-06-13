from food import Food
from snake import Snake
from screen import Screen

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

                        # initialize a new start!
                        self.snake = Snake( self, self.all_settings['snake'] )
                        self.food = Food( self, self.all_settings['food'] )

            # fill the screen with a background color 
            self.screen.fill()
            
            # Draw the baseline of the screen
            self.screen.draw()

            if self.playing:

                # move the snake
                self.snake.move()

                # draw 
                self.snake.draw()
                self.food.draw()
           
            # update the screen's display to show the changes
            self.screen.flip()
            self.clock.tick( self.settings['FPS'] )
            
        pygame.quit()  