import networkx as nx

class Map:
	def __init__(self):
		self._map = nx.Graph()
		self._position = None
	
	def gen_rand_map(self, size = 20):
transition_matrix = {
					"VertHallway": {"VertHallway": 0.5, "HorzHallway": 0.5, "Room": 0.2},
					"HorzHallway": {"Room": 0.2}
					}
#for key_1 in transition_matrix:
	#for key_2 in transition_matrix[key_1]:
		#if key_2 not in transition_matrix.keys():
			
			#transition_matrix[key_2][key_1] = transition_matrix[key_1][key_2]
		self._map.add_node("Room")
		for e in range(size):
			
	@property
	def map(self):
		return self._map
	
	@map.setter
	def map(self, value):
		self._map = value
