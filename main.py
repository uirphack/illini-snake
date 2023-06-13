import json
with open('settings.json') as json_data:
    settings = json.load( json_data )

from game import Game
game_inst = Game( settings )
game_inst.play()
