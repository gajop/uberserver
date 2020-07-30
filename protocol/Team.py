class Team():
	def __init__(self, root, id, leader, users=[]):
		self._root = root
		self.id = id
		self.leader = leader
		self.users = users