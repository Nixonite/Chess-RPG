class Weapon:
	def __init__(self):
		self._attack = 1
		self._size = 1
	
	
	def get_attack(self):
		return self._attack
	
	
	def set_attack(self, value):
		self._attack = value
	
	
	def get_size(self);
		return self._size
	
	
	def set_size(self, value):
		self._size = value

	size = property(get_size, set_size)
	attack = property(get_attack, set_attack)
