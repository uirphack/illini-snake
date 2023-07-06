from illini_snake import Base, Food, Snake, Screen, utils, settings
import os

import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

class Game(Base):
    def __init__( self ):
        Base.__init__( self )
        self.running = True
        self.loading_screen = True
        self.clock = pygame.time.Clock()

        self.screen = Screen()
        self.load_logo_images()

    @property
    def score( self ):
        pass

    @score.getter
    def score( self ) -> int:
        """returns the length of the snake, calling `game.score` runs this method"""
        return len(self.snake)

    def load_logo_images( self ):
        """preload all logo iamges"""

        filenames = os.listdir( self.settings['LOGOS_PATH'] )
        self.logo_images = []
        for filename in filenames:
            self.logo_images.append(utils.load_logo_file( os.path.abspath( os.path.join(self.settings['LOGOS_PATH'],filename)), self.all_settings['food']['WIDTH'] )) 

    def run( self ):
        """the main loop of the game"""

        while self.running:

            # See if user clicked "X" on the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                
            # see if the user pressed a key            
            if pygame.key.get_focused():
                keys = pygame.key.get_pressed()

                if keys[pygame.K_z]: #exit entire program
                    self.running = False

                if keys[pygame.K_r]: #restart game
                    self.loading_screen = True

                if self.loading_screen: 

                    # user wants to start the game
                    if keys[pygame.K_RETURN]:
                        self.loading_screen = False
                        self.loop_start_time = pygame.time.get_ticks()

                        # initialize a new game!
                        self.snake = Snake()
                        self.food = Food()

                if not self.loading_screen:                
                    self.snake.process_key_press( keys )
                
            self.screen.fill()
            self.screen.draw()

            if not self.loading_screen:
                
                # if enough time has passed for the snake to move
                current_time = pygame.time.get_ticks()
                if (current_time - self.loop_start_time) > (1000/self.snake.settings['SPEED']):
                    self.loop_start_time = current_time
                
                    # move the snake
                    self.snake.move()

                self.snake.draw()
                self.food.draw()
                self.screen.draw_score()
           
            # update the screen's display to show the changes
            self.screen.flip()
            self.clock.tick( self.settings['FPS'] )
            
        pygame.quit()  
    
    def game_over( self ):
        self.loading_screen = True
        print ('Final score: ' + str(self.score))