import networkx as nx

class Room:
	def __init__(self):
		self._width = 1
		self._height = 1
		self._color = 'White'
	
	@property
	def width(self):
		return self._width
	
	@property
	def height(self):
		return self._height
	
	@property
	def color(self);
		return self._color
	
	@color.setter
	def color(self, value):
		self._color = value
	
	@width.setter
	def width(self, value):
		self._width = value
	
	@height.setter
	def height(self, value):
		self._height = value
		
	def get_area(self):
		return self._width * self._height
