from unicode import *

class UniChess:
	
	def __init__(self):
		self._board = [[],[],[],[],[],[],[],[]]
		for row in range(2,6):
			self._board[row] = ['_']*8
	
	def setup_board(self):
		self._board[1] = [uni_chess_pieces['wP']]*8
		self._board[6] = [uni_chess_pieces['bP']]*8
		self._board[0] = [uni_chess_pieces['wR'],
							uni_chess_pieces['wN'],
							uni_chess_pieces['wB'],
							uni_chess_pieces['wQ'],
							uni_chess_pieces['wK'],
							uni_chess_pieces['wB'],
							uni_chess_pieces['wN'],
							uni_chess_pieces['wR']]
		self._board[7] = [uni_chess_pieces['bR'],
							uni_chess_pieces['bN'],
							uni_chess_pieces['bB'],
							uni_chess_pieces['bQ'],
							uni_chess_pieces['bK'],
							uni_chess_pieces['bB'],
							uni_chess_pieces['bN'],
							uni_chess_pieces['bR']]
		for row in range(2,6):
			self._board[row] = ['_']*8
		
	def get_board(self):
		prettyboard = ['|'.join(row) for row in self._board]
		return prettyboard

	def set_board(self, value):
		self._board = value
	
	board = property(get_board, set_board)
