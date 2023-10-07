"""
This will be the framework for different sorting algorithms I want to test, it will create n rectangles
of varying sizes and distribute them randomly across a window created by the turtle module.

Author: Ryley Turner
"""

import random
import turtle
import time

TITLE = "RSort 1.0"

WIDTH = 1200
HEIGHT = 800
MARGIN = 40

NUMBER_OF_RECTANGLES = 200

width_delta = (WIDTH - MARGIN * 2) / NUMBER_OF_RECTANGLES
height_scale = (HEIGHT - MARGIN * 2) / NUMBER_OF_RECTANGLES


def current_sort(values):
	new_values = []
	i = 0
	while i < len(values) - 1:
		if values[i] > values[i + 1]:
			new_values.append(values[i + 1])
			new_values.append(values[i])
			i += 2
		else:
			new_values.append(values[i])
			i += 1
	if len(new_values) < len(values):
		new_values.append(values[len(values) - 1])
	return new_values


def random_order(rectangle_quantity):
	"""Takes in the number of rectangles we would like to use and returns a numbered list that
	contains each position only once in a random order.
	INPUTS:
		rectangle_quantity (Integer): amount of rectangles you want
	OUTPUTS
		heights (list): """
	heights = []
	while len(heights) < rectangle_quantity:
		new_height = random.randint(1, rectangle_quantity)
		if new_height not in heights:
			heights.append(new_height)
	return heights


def draw_rectangle(given_turtle, width, height, fill_color):
	"""Draws a rectangle with a given width and height using a provided turtle"""
	given_turtle.fillcolor(fill_color)
	given_turtle.begin_fill()

	for _ in range(2):
		given_turtle.forward(width)
		given_turtle.left(90)
		given_turtle.forward(height)
		given_turtle.left(90)

	given_turtle.end_fill()


def draw_screen(screen_object, given_turtle, heights):
	given_turtle.penup()
	given_turtle.goto(MARGIN - (WIDTH / 2), MARGIN - (HEIGHT / 2))
	given_turtle.pendown()

	for height in heights:
		draw_rectangle(given_turtle, width_delta, height * height_scale, "white")
		given_turtle.forward(width_delta)

	screen_object.update()


def main():
	runtime = time.time()

	my_screen = turtle.Screen()
	my_screen.setup(WIDTH, HEIGHT)
	my_screen.title(TITLE)
	my_screen.tracer(0)

	rectangle_artist = turtle.Turtle()
	rectangle_artist.pencolor("White")
	rectangle_artist.hideturtle()
	rectangle_artist.speed(0)

	current_order = random_order(NUMBER_OF_RECTANGLES)
	correct_order = [i + 1 for i in range(NUMBER_OF_RECTANGLES)]
	my_screen.tracer(0)
	my_screen.bgcolor("black")

	frames = 0

	while current_order != correct_order:
		rectangle_artist.clear()
		draw_screen(my_screen, rectangle_artist, current_order)
		current_order = current_sort(current_order)
		frames += 1
	
	rectangle_artist.clear()
	draw_screen(my_screen, rectangle_artist, current_order)

	runtime = time.time() - runtime

	print(f"Sorted {NUMBER_OF_RECTANGLES} rectangles in {runtime:.2f} seconds using {frames} comparisons.")
	my_screen.exitonclick()


if __name__ == "__main__":
	main()