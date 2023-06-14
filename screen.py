from base import Base
import pygame

class Screen( Base ):
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )
        
        self.pixel_length = self.settings['LENGTH'] * self.settings['SQUARE_WIDTH']
        self.pixel_width = self.settings['WIDTH'] * self.settings['SQUARE_WIDTH']
        
        self.pygame_screen = pygame.display.set_mode( (self.pixel_length, self.pixel_width) )
        
        self.main_menu_Font = pygame.font.SysFont( 
            self.settings['START_MENU']['FONT'],
            self.settings['START_MENU']['FONT_SIZE'] 
        )
        self.score_display_Font = pygame.font.SysFont( 
            self.settings['SCORE_DISPLAY']['FONT'],
            self.settings['SCORE_DISPLAY']['FONT_SIZE'] 
        )
        
        self.food_options = []
        for i in range(self.settings['LENGTH']):
            for j in range(self.settings['WIDTH']):
                self.food_options.append( [i,j] )
        
    def fill( self ):
        
        """fill the entire screen with a background color"""
        self.pygame_screen.fill( self.settings['COLOR'] )

    def draw( self ):
        
        if not self.game.playing:        
            Surface = self.main_menu_Font.render( 
                'Press Enter to play', 
                None, 
                self.settings['START_MENU']['FONT_COLOR']
            )
            x_centered = (self.pixel_length - Surface.get_rect().width)/2
            self.pygame_screen.blit( Surface, ( int(x_centered), int(self.pixel_width/2) ) ) 

    def draw_score( self ):
        if self.game.playing:
            Surface = self.score_display_Font.render( 'Score: ' + str(self.game.get_score() ),None, self.settings['SCORE_DISPLAY']['FONT_COLOR'] )
            self.pygame_screen.blit( Surface, (5,5) ) 

    def flip( self ):
        pygame.display.flip()