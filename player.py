from weapon import Weapon

class Player:
	def __init__(self):
		self._health = 100
		self._strength = 10
		self._accuracy = 10
		self._defense = 10
		self._magic = 10
		self._ranging = 10
		self._right_equip = Weapon()
		self._left_equip = Weapon()
		
	def get_right_equip(self):
		return self._right_equip
	
	def set_right_equip(self, value):
		self._right_equip = value
	
	
	def get_left_equip(self):
		return self._left_equip
	
	
	def set_left_equip(self, value):
		self._left_equip = value
		
	
	def get_health(self):
		return self._health
	
	
	def get_strength(self):
		return self._strength
		
	
	def get_accuracy(self):
		return self._accuracy
		
	
	def get_defense(self):
		return self._defense
	
	
	def get_magic(self):
		return self._magic
	
	
	def get_ranging(self):
		return self._ranging
		
	
	def set_ranging(self, value):
		self._ranging = value
	
	
	def set_magic(self, value);
		self._magic = value
	
	
	def set_defense(self, value):
		self._defense = value
	
	
	def set_strength(self, value);
		self._strength = value
	
	
	def set_health(self, value);
		self._health = value
	
	
	def set_accuracy(self, value):
		self._accuracy = value
	
	accuracy = property(get_accuracy, set_accuracy)
	magic = property(get_magic, set_magic)
	ranging = property(get_ranging, set_ranging)
	defense = property(get_defense, set_defense)
	health = property(get_health, set_health)
	right_equip = property(get_right_equip, set_right_equip)
	left_equip = property(get_left_equip, set_left_equip)
