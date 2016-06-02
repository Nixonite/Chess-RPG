class UniChess:
	
	def __init__(self):
		self._board = [[],[],[],[],[],[],[],[]]
		for row in range(3,7):
			self._board[row] = ['__']*8
	
	def get_board(self):
		prettyboard = '\n'.join(['|'.join(row) for row in self._board])
		return prettyboard

	def set_board(self, value):
		self._board = value
	
	board = property(get_board, set_board)
