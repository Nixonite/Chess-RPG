class Weapon:
	def __init__(self):
		self._attack = 1
		self._size = 1
	
	@property
	def attack(self):
		return self._attack
	
	@attack.setter
	def attack(self, value):
		self._attack = value
	
	@property
	def size(self);
		return self._size
	
	@size.setter
	def size(self, value):
		self._size = value
