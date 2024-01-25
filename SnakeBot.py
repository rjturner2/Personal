"""
This is a basic framework for the fellas that will help them setup snake AI's.
There are some constants and functions I want you guys to be able to use to control the Snake itself, You'll see
them imported below. Feel free to rename anything you want, this is your file and can do whatever you want it to.

All of that being said, I will only take this file back from you, if you make changes to Snake.py itself, I will not be using those.

The goal is to - on average - have your bot achieve the longest snake possible.

We will run your bot through its paces an arbitrary number of times, but all bots will get the same number of chances to achieve high scores.

There is a prize for winning this competition

Please name your bot and uniquely name this file after your chosen bot name.

Author: (Your name here)
"""

from Snake import heading_left as left, heading_down as down, heading_right as right, heading_up as up
from Snake import main as run


def main():
	left()
	run()


if __name__ == "__main__":
	main()
