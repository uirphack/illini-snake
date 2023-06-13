from base import Base
import pygame

class Screen( Base ):
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )
        
        self.pixel_length = self.settings['LENGTH'] * self.settings['SQUARE_WIDTH']
        self.pixel_width = self.settings['WIDTH'] * self.settings['SQUARE_WIDTH']
        
        self.screen = pygame.display.set_mode(
            (self.pixel_length, self.pixel_width)
        )
        
        self.main_menu_Font = pygame.font.SysFont( 
            self.settings['START_MENU']['FONT'],
            self.settings['START_MENU']['FONT_SIZE'] 
        )
        
    def fill( self ):
        self.screen.fill( self.settings['COLOR'] )

    def draw( self ):
        
        if not self.game.playing:
            Surface = self.main_menu_Font.render( 
                'Press Enter to play', 
                None, 
                self.settings['START_MENU']['FONT_COLOR']
            )

            self.screen.blit( Surface, ( int(self.pixel_length/2), int(self.pixel_width/2) ) ) 

    def flip( self ):
        pygame.display.flip()