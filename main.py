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
Board.setup_board()

for line in story['Introduction']:
	glb.printc(uni_chess_pieces['wN']+' '+line)

glb.print_str(3, 1, uni_chess_pieces['wN']+" This is a fucking chess board")
glb.print_rows(Board.board)

glb.quit()
