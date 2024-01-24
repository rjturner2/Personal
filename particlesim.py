import random
import time
import turtle

DELTA_TIME = 0.1
GRAVITY = 9.8 * DELTA_TIME

PARTICLE_COUNT = 20
PARTICLE_DIST_VARIANCE = 50

particle_list = []


class Particle():

	def __init__(self, x, y):
		self.position = [x, y]
		self.velocity = [random.Randint(-10,10), random.Randint(-10, 10)]
		self.creation_time = time.time()


	def check_status(self):
		if time.time() - self.creation_time >= 10:
			del self


def draw_particles(my_turtle, my_screen):
	global particle_list
	for particle in particle_list:
		particle.check_status()
		my_turtle.goto(particle.position[0], particle.position[1])
		my_turtle.dot(10)


def step_velocity():
	global particle_list
	for particle in particle_list:
		particle.position[0] += particle.velocity[0]
		particle.position[1] += particle.velocity[1] - GRAVITY


def create_particles(x, y):
	global particle_list
	print(f"clicked {x}, {y}")
	new_x = x + random.randint(-PARTICLE_DIST_VARIANCE, PARTICLE_DIST_VARIANCE)
	new_y = y + random.randint(-PARTICLE_DIST_VARIANCE, PARTICLE_DIST_VARIANCE)
	particle_list = [Particle(new_x, new_y) for _ in range(PARTICLE_COUNT)]


def main():
	my_screen, my_turtle = turtle.Screen(), turtle.Turtle()

	my_turtle.hideturtle()
	my_turtle.penup()

	my_screen.onclick(create_particles, btn=1)
	my_screen.listen()
	my_screen.tracer(0)

	while True:
		draw_particles(my_turtle, my_screen)
		step_velocity()
		time.sleep(DELTA_TIME)
		my_turtle.clear()
		print(particle_list)


if __name__ == "__main__":
	main()

