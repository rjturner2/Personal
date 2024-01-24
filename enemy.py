class Enemy:


	def __init__(self, starting_health=100):
		self.health = starting_health
		self.position = [0, 0]


	def __del__(self):
		print("YEEEEOWCH")


	def move(self, x, y):
		self.position = [x, y]


	def take_damage(self, damage):
		self.health -= damage


	def get_position(self):
		return self.position


	def get_health(self):
		return self.health


	def check_status(self):
		if self.health <= 0:
			del self
		else:
			return self.health


def main():

	archers = [Enemy() for _ in range(10)]

	archers[0].move(10, 10)

	print(archers[0].position, archers[7].position)

	for archer in archers:
		del archer


if __name__ == "__main__":
	main()