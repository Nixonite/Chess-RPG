from controller import Controller
import time
import json
from unichess import UniChess
from unicode import *
import locale
from color import color
locale.setlocale(locale.LC_ALL,"")

with open("story.json") as story_file:
	story = json.load(story_file)

glb = Controller()
Board = UniChess()

for line in story['Introduction']:
	glb.printc((uni_chess_pieces['wN']+' '+line).encode('utf_8'))

glb.printc(Board.board)

glb.quit()
