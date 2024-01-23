"""
Here I will be trying to create a merge sort function using recursion

Author: Ryley Turner
"""

import random
from sortmodule import *

LIST_LENGTH = 100


def merge(left, right):
	left_index, right_index = 0, 0
	result = []

	while left_index < len(left) and right_index < len(right):
		if left[left_index] > right[right_index]:
			result.append(right[right_index])
			right_index += 1
		else:
			result.append(left[left_index])
			left_index += 1

	result += left[left_index:]
	result += right[right_index:]

	return result


def merge_sort(array):
	if len(array) <= 1:
		return array

	half = len(array) // 2
	left = merge_sort(array[:half])
	right = merge_sort(array[half:])
	
	return merge(left, right)


def main():
	current_order = random_order(LIST_LENGTH)
	
	rectangle_artist = turtle.Turtle()
	my_screen = turtle.Screen()

	setup_screen(my_screen, rectangle_artist)

	my_screen.exitonclick()


if __name__ == "__main__":
	main()
	