from base import Base

class Food( Base ):
    def __init__( self, game, settings ):
        Base.__init__( self, game, settings )
        
    def draw( self ):
        pass