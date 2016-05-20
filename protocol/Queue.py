from AutoDict import AutoDict

class Queue(AutoDict):
	def __init__(self, root, name, title, description, minPlayers, maxPlayers, teamJoinAllowed, botName, requireConfirmation, gameNames=[], mapNames=[], engineVersions=[], users=[]):
		self._root = root
		self.name = name

		self.title = title
		self.description = description
		self.minPlayers = minPlayers
		self.maxPlayers = maxPlayers
		self.teamJoinAllowed = teamJoinAllowed
		self.gameNames = gameNames
		self.mapNames = mapNames
		self.engineVersions = engineVersions
		self.users = users
		self.requireConfirmation = requireConfirmation

		# Matchmaking bot name
		self.botName = botName

		self.__AutoDictInit__()

