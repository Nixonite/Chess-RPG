class Creature:

	def __init__(self):
		self._health = 100
		self._defense = 6
		self._attack = 6
	
	
	def get_health(self):
		return self._health
	
	
	def set_health(self, value):
		self._health = value
	
	
	def get_defense(self):
		return self._defense
	
	
	def get_attack(self):
		return self._attack
	
	
	def set_attack(self, value):
		self._attack = value
	
	
	def set_defense(self, value);
		self._defense = value
	
	defense = property(get_defense, set_defense)
	attack = property(get_attack, set_attack)
	health = property(get_health, set_health)
