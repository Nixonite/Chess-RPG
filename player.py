from weapon import Weapon

class Player:
	def __init__(self):
		self._health = 100
		self._strength = 10
		self._accuracy = 10
		self._defense = 10
		self._magic = 10
		self._range = 10
		self._right_equip = Weapon()
		self._left_equip = Weapon()
		
	@property
	def right_equip(self):
		return self._right_equip
	
	@right_equip.setter
	def right_equip(self, value):
		self._right_equip = value
	
	@property
	def left_equip(self):
		return self._left_equip
	
	@left_equip.setter
	def left_equip(self, value):
		self._left_equip = value
		
	@property
	def health(self):
		return self._health
	
	@property
	def strength(self):
		return self._strength
		
	@property
	def accuracy(self):
		return self._accuracy
		
	@property
	def defense(self):
		return self._defense
	
	@property
	def magic(self):
		return self._magic
	
	@property
	def range(self):
		return self._range
		
	@range.setter
	def range(self, value):
		self._range = value
	
	@magic.setter
	def magic(self, value);
		self._magic = value
	
	@defense.setter
	def defense(self, value):
		self._defense = value
	
	@strength.setter
	def strength(self, value);
		self._strength = value
	
	@health.setter
	def health(self, value);
		self._health = value
	
	@accuracy.setter
	def accuracy(self, value):
		self._accuracy = value
