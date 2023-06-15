import json
with open('./src/settings.json') as json_data:
    settings = json.load( json_data )

from src.game import Game
game_inst = Game( settings )
game_inst.play()
