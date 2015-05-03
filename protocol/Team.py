from AutoDict import AutoDict

class Team(AutoDict):
	def __init__(self, id, leader, users=[]):
		self._root = root
		self.id = id
		self.leader = leader
		self.users = users

		self.__AutoDictInit__()