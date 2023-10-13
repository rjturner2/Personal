"""
Cute Little Animation for the group study

Author: (Ryley Turner)
"""

import turtle
from time import sleep
import random

WIDTH = 800
HEIGHT = 600

BALL_SIZE = 100
BALL_COLOR = "green"

DELTA_TIME = 0.01

GRAVITY = 18.6 * DELTA_TIME

DAMPENING = 0.8  # Percentage of rebound velocity

VERTICAL_DEBOUNCE = False
HORIZONTAL_DEBOUNCE = False

MIN_STARTING_VELOCITY = -20
MAX_STARTING_VELOCITY = 20


def draw_ball(my_turtle, x, y, size, color="white"):

	my_turtle.goto(x, y)

	my_turtle.dot(size, color)


def setup_window(width=800, height=600, bg_color="white", pen_color="black"):

    new_turtle = turtle.Turtle()
    new_screen = turtle.Screen()

    new_screen.setup(width, height)

    new_screen.bgcolor(bg_color)
    new_turtle.pencolor(pen_color)

    return new_screen, new_turtle


def hits_boundary(my_turtle, my_screen, ball_size):
	# Get Current Turtle Location
	x, y = my_turtle.xcor(), my_turtle.ycor()

	# Get current window size
	window_width = my_screen.window_width()
	window_height = my_screen.window_height()

	# Check if turtle + ball size exceeds window boundary
	# Returns True if we've hit or exceeded a boundary
	return abs(x) + ball_size / 2 > window_width / 2 or abs(y) + ball_size / 2 > window_height / 2


def new_velocities(my_turtle, my_screen, ball_velocities, ball_size, dampening):
	# get current turtle location
	x, y = my_turtle.xcor(), my_turtle.ycor()

	# Get current window size
	window_width = my_screen.window_width()
	window_height = my_screen.window_height()

	# Get global variables
	global HORIZONTAL_DEBOUNCE
	global VERTICAL_DEBOUNCE

	if not HORIZONTAL_DEBOUNCE:
		if abs(x) + ball_size / 2 > window_width / 2:
			ball_velocities[0] = -(ball_velocities[0] * dampening)
			HORIZONTAL_DEBOUNCE	= True

	if not VERTICAL_DEBOUNCE:
		if abs(y) + ball_size / 2 > window_height / 2:
			ball_velocities[1] = -(ball_velocities[1] * dampening)
			VERTICAL_DEBOUNCE = True

	return ball_velocities


def main():
	global VERTICAL_DEBOUNCE
	global HORIZONTAL_DEBOUNCE
	global MIN_STARTING_VELOCITY
	global MAX_STARTING_VELOCITY
	global BALL_COLOR

	my_screen, my_turtle = setup_window(width=WIDTH, height=HEIGHT, bg_color="black")

	random_x_velocity = random.randint(MIN_STARTING_VELOCITY, MAX_STARTING_VELOCITY)
	random_y_velocity = random.randint(MIN_STARTING_VELOCITY, MAX_STARTING_VELOCITY)

	ball_velocity = [random_x_velocity, random_y_velocity]
	ball_location = [0, 0]

	my_turtle.penup()
	my_turtle.hideturtle()

	my_screen.tracer(0)

	while True:
		# Add gravitational constant
		ball_velocity[1] -= GRAVITY

		# Slow horizontal movement to represent air resistance
		ball_velocity[0] *= 0.999

		# Set new ball position based on the ball's velocity
		ball_location[0] += ball_velocity[0]
		ball_location[1] += ball_velocity[1]

		my_turtle.clear()
		draw_ball(my_turtle, ball_location[0], ball_location[1], BALL_SIZE, BALL_COLOR)

		if hits_boundary(my_turtle, my_screen, BALL_SIZE):
			ball_velocity = new_velocities(my_turtle, my_screen, ball_velocity, BALL_SIZE, DAMPENING)
		else:
			VERTICAL_DEBOUNCE = False
			HORIZONTAL_DEBOUNCE	= False

		my_screen.update()

		sleep(DELTA_TIME)

		if ball_location[1] + BALL_SIZE < -my_screen.window_height() / 2:
			random_x_velocity = random.randint(MIN_STARTING_VELOCITY, MAX_STARTING_VELOCITY)
			random_y_velocity = random.randint(MIN_STARTING_VELOCITY, MAX_STARTING_VELOCITY)

			ball_location = [0, 0]
			ball_velocity = [random_x_velocity, random_y_velocity]


	my_screen.exitonclick()


if __name__ == "__main__":
	main()