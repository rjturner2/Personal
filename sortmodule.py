"""
This will be the framework for different sorting algorithms I want to test, it will create n rectangles
of varying sizes and distribute them randomly across a window created by the turtle module.

Author: Ryley Turner
"""

import random
import turtle
import time
import sys

TITLE = "RSort 1.0"

WIDTH = 1200
HEIGHT = 800
MARGIN = 40


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


def bubble_sort(value_list):
	for i in range(len(value_list) - 1):
		for j in range(len(value_list) - 1 - i):
			if value_list[i] > value_list[i + 1]:
				value_list[i], value_list[i + 1] = value_list[i + 1], value_list[i]
			else:
				break

	return value_list
			

def bogosort(value_list):
	return random_order(len(value_list))


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


def draw_screen(screen_object, given_turtle, heights, number_of_rectangles):
	"""This will draw the entire screen full of rectangles before updating the display to show the
	current step the algorithm is on"""
	width_delta = (screen_object.window_width() - MARGIN * 2) / number_of_rectangles
	height_scale = (screen_object.window_height() - MARGIN * 2) / number_of_rectangles

	given_turtle.penup()
	given_turtle.goto(MARGIN - (screen_object.window_width() / 2), MARGIN - (screen_object.window_height() / 2))
	given_turtle.pendown()

	for i in range(len(heights)):
		draw_rectangle(given_turtle, width_delta, heights[i] * height_scale, "white")
		given_turtle.forward(width_delta)

	screen_object.update()


def main():
	sorting_method = sys.argv[1]
	NUMBER_OF_RECTANGLES = int(input("How many rectangles would you like to sort?: "))

	runtime = time.time()

	my_screen = turtle.Screen()
	my_screen.setup(WIDTH, HEIGHT)
	my_screen.title(TITLE)
	my_screen.tracer(0)
	my_screen.bgcolor("black")

	rectangle_artist = turtle.Turtle()
	rectangle_artist.pencolor("black")
	rectangle_artist.hideturtle()
	rectangle_artist.speed(0)

	current_order = random_order(NUMBER_OF_RECTANGLES)
	correct_order = [i + 1 for i in range(NUMBER_OF_RECTANGLES)]

	frames = 0

	while current_order != correct_order:
		rectangle_artist.clear()
		draw_screen(my_screen, rectangle_artist, current_order, NUMBER_OF_RECTANGLES)
		current_order = eval(f"{sorting_method}(current_order)")
		frames += 1
	
	rectangle_artist.clear()
	draw_screen(my_screen, rectangle_artist, current_order, NUMBER_OF_RECTANGLES)

	runtime = time.time() - runtime

	my_screen.title(f"Sorted {NUMBER_OF_RECTANGLES} rectangles in {runtime:.2f} seconds using {frames} comparisons.")
	my_screen.exitonclick()


if __name__ == "__main__":
	main()
	