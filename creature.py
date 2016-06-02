class Creature:

	def __init__(self):
		self._health = 100
		self._defense = 6
		self._attack = 6
	
	@property
	def health(self):
		return self._health
	
	@health.setter
	def health(self, value):
		self._health = value
	
	@property
	def defense(self):
		return self._defense
	
	@property
	def attack(self):
		return self._attack
	
	@attack.setter
	def attack(self, value):
		self._attack = value
	
	@defense.setter
	def defense(self, value);
		self._defense = value
	
