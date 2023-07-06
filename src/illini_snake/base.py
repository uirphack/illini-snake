from illini_snake import settings

class Base:
    def __init__( self ):
        key = self.__class__.__name__   #Food, Game, Screen, etc.
        self.settings = settings[ key ]
        self._set_settings()

    def _set_settings( self ):
        for key in self.settings:
            setattr( self, key, self.settings[key]) #food.key = value
