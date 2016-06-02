import networkx as nx

class Room:
	def __init__(self):
		self._width = 1
		self._height = 1
		self._color = 'White'
	
	def get_width(self):
		return self._width
	
	
	def get_height(self):
		return self._height
	
	
	def get_color(self);
		return self._color
	
	
	def set_color(self, value):
		self._color = value
	
	
	def set_width(self, value):
		self._width = value
	
	
	def set_height(self, value):
		self._height = value
		
	def get_area(self):
		return self._width * self._height
	
	color = property(get_color, set_color)
	height = property(get_height, set_height)
	width = property(get_width, set_width)
