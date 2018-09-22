class GameStats:
	"""Track statistics for Alien Invasion"""

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# Display saved high score, or make a new one if not found.
		# This is in addition to the text.
		try:
			with open('saved_score.txt') as file_object:
				self.high_score = int(file_object.read())
		except FileNotFoundError:
			self.high_score = 0

		# Reset level to 1
		self.level = 1

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
