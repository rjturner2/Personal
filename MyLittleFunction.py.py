"""
A collection of functions for use in our CSM 2170 class.
"""
import math
import turtle
import random

# *************************************************************************************************
# Module variables and constants
# *************************************************************************************************

# Here are some module level (global) variables for remembering the turtle's location and heading. We
# normally do not want to use global variables if we can help it, and we will see "better" ways of
# doing this later. However, for now this will work for saving and restoring the turtle's location.
# we could save more information about the turtle's state, but we will not do that for now.
saved_turtle_x = 0.0
saved_turtle_y = 0.0
saved_turtle_heading = 0.0
saved_pen_state = True


# *************************************************************************************************
# Turtle state saving and restoring functions
# *************************************************************************************************
def save_turtle_state(my_turtle):
    """
    Saves the given turtle's state (location, heading, pen state).

    Args:
        my_turtle: the turtle whose state should be saved.

    Return:
        None
    """
    # Let Python know that we want to use the module variables (i.e. global
    # variables). Without the use of the global keyword Python would make
    # new local variables that are just visible inside this function. The
    # use of global variables is often considered bad style. Later we will
    # see better ways of achieving effects like this without having to use
    # global variables.
    global saved_turtle_x, saved_turtle_y, saved_turtle_heading, saved_pen_state

    # Store the values in the module level variables.
    saved_turtle_x = my_turtle.xcor()
    saved_turtle_y = my_turtle.ycor()
    saved_turtle_heading = my_turtle.heading()
    saved_pen_state = my_turtle.isdown()


def restore_turtle_state(my_turtle):
    """
    Restores the given turtle to the last saved state.

    Args:
        my_turtle: the turtle whose state should be restored.

    Return:
        None
    """
    my_turtle.up()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.setheading(saved_turtle_heading)
    if saved_pen_state:
        my_turtle.down()


# *************************************************************************************************
# Letter drawing functions
#
# Each of these functions draws a letter that fits inside a square of the given size (my_turtle
# starts on the baseline of the letter, facing the direction the letter is to be drawn). When the
# function ends the turtle is in the same state it was in when the function was called (you can
# use the save and restore functions to help with this or move the turtle back there yourself).
# *************************************************************************************************
def draw_a(my_turtle, size):
    """Draws an 'A' composed of the specified size with the given turtle."""

    # Save the turtle's state
    save_turtle_state(my_turtle)

    # Compute the angle to turn for the legs of the A. It is computed from the
    # slope of the line rise = 10, run = 5.
    angle = math.degrees(math.atan2(10, 5))

    # Compute the length of the leg from the Pythagorean Theorem
    leg_length = math.sqrt(size ** 2 + (0.5 * size) ** 2)

    # Compute the length to the crossbar of the A
    bottom_length = math.sqrt((0.4 * size) ** 2 + (0.2 * size) ** 2)

    # Size of the crossbar
    cross_length = size * 0.6

    # Draw first leg
    my_turtle.left(angle)
    my_turtle.forward(leg_length)

    # Draw second leg
    my_turtle.right(2 * angle)
    my_turtle.forward(leg_length)

    # Backup and draw crossbar
    my_turtle.backward(bottom_length)
    my_turtle.left(angle)
    my_turtle.backward(cross_length)

    # Restore the turtle's state
    restore_turtle_state(my_turtle)
    # my_turtle.left(angle)
    # my_turtle.backward(bottom_length)
    #
    # # Turn back to initial
    # my_turtle.right(angle)


def draw_b(my_turtle, size):
    # This function will draw a letter 'B' using a turtle that fits within a box
    # of a specified size
    save_turtle_state(my_turtle)

    radius = size / 4
    initial_step = size - radius
    secondary_step = size - radius * 1.1

    my_turtle.forward(initial_step)
    my_turtle.circle(radius, 180)
    my_turtle.forward(initial_step)
    my_turtle.right(180)
    my_turtle.forward(secondary_step)
    my_turtle.circle(radius, 180)
    my_turtle.forward(secondary_step)
    my_turtle.left(90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_c(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = (size / 2)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.pendown()

    my_turtle.left(90)
    my_turtle.circle(radius, 180)
    my_turtle.forward(size - radius)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.pendown()
    my_turtle.forward(size - radius)

    restore_turtle_state(my_turtle)


def draw_d(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = size / 2

    my_turtle.forward(size - radius)
    my_turtle.circle(radius, 180)
    my_turtle.forward(size - radius)
    my_turtle.left(90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_e(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.pendown()
    my_turtle.forward(size)
    my_turtle.right(90)

    for i in range(2):
        my_turtle.forward(size)
        my_turtle.backward(size)
        my_turtle.right(90)
        my_turtle.forward(size / 2)
        my_turtle.left(90)

    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_f(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.pendown()
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.backward(size)
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_g(my_turtle, size):

    save_turtle_state(my_turtle)

    radius = (size / 2)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.pendown()

    my_turtle.left(90)
    my_turtle.circle(radius, 180)
    my_turtle.forward(size - radius)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.pendown()
    my_turtle.forward(size - radius)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size - radius)
    my_turtle.left(90)
    my_turtle.pendown()

    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size / 2)

    restore_turtle_state(my_turtle)


def draw_h(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.backward(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.backward(size / 2)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_i(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.forward(size)
    my_turtle.backward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)

    my_turtle.right(90)
    my_turtle.forward(size / 2)
    my_turtle.backward(size)

    restore_turtle_state(my_turtle)


def draw_j(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = size / 4

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.forward(size / 2)
    my_turtle.backward(size)
    my_turtle.forward(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size - radius)
    my_turtle.circle(-radius, 180)

    restore_turtle_state(my_turtle)


def draw_k(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angled_length = math.sqrt((size / 2) ** 2 + (size) ** 2)
    angle1 = math.degrees(math.atan2(size / 2, size))
    angle2 = math.degrees(math.atan2(-size / 2, size))

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.backward(size / 2)
    my_turtle.setheading(starting_angle + angle1)
    my_turtle.forward(angled_length)
    my_turtle.backward(angled_length)
    my_turtle.setheading(starting_angle + angle2)
    my_turtle.forward(angled_length)

    restore_turtle_state(my_turtle)


def draw_l(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.forward(size)
    my_turtle.backward(size)
    my_turtle.left(90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_m(my_turtle, size):
    save_turtle_state(my_turtle)

    angle1 = math.degrees(math.atan2(-size, size / 2))
    angle2 = math.degrees(math.atan2(size, size / 2))
    angled_length = math.sqrt((size / 3) ** 2 + size ** 2)
    starting_angle = my_turtle.heading()

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.setheading(starting_angle + angle1)
    my_turtle.forward(angled_length)
    my_turtle.setheading(starting_angle + angle2)
    my_turtle.forward(angled_length)
    my_turtle.setheading(starting_angle + 270)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_n(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle = math.degrees(math.atan2(-size, size))

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.setheading(starting_angle + angle)
    my_turtle.forward(math.sqrt((size) ** 2 + (size) ** 2))
    my_turtle.setheading(starting_angle + 90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_o(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.pendown()

    my_turtle.circle(size / 2)

    restore_turtle_state(my_turtle)


def draw_p(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = size / 4
    gap = (size - radius)

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(gap)
    my_turtle.circle(-radius, 180)
    my_turtle.forward(gap)

    restore_turtle_state(my_turtle)


def draw_q(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle = math.degrees(math.atan2(- size / 2, size / 2))
    leg_size = math.sqrt(2 * (size / 2) ** 2)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.circle(-size / 2)

    restore_turtle_state(my_turtle)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size / 2)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.setheading(starting_angle + angle)
    my_turtle.forward(leg_size)

    restore_turtle_state(my_turtle)


def draw_r(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle = math.degrees(math.atan2(-size / 2, size / 3))
    angled_length = math.sqrt((size / 2) ** 2 + (size / 3) ** 2)
    radius = size / 4
    gap_step = size - radius

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(gap_step)
    my_turtle.circle(-radius, 180)
    my_turtle.forward(gap_step)
    my_turtle.right(180)
    my_turtle.forward(size / 3)
    my_turtle.setheading(starting_angle + angle)
    my_turtle.forward(angled_length)

    restore_turtle_state(my_turtle)


def draw_s(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = size / 8
    gap_length = size - radius * 2
    verticle_gap_length = size - radius * 6

    my_turtle.forward(radius)
    my_turtle.forward(gap_length)
    my_turtle.circle(radius, 90)
    my_turtle.forward(verticle_gap_length)
    my_turtle.circle(radius, 90)
    my_turtle.forward(gap_length)
    my_turtle.circle(-radius, 90)
    my_turtle.forward(verticle_gap_length)
    my_turtle.circle(-radius, 90)
    my_turtle.forward(gap_length)
    my_turtle.forward(radius)

    restore_turtle_state(my_turtle)


def draw_t(my_turtle, size):
    save_turtle_state(my_turtle)

    my_turtle.penup()
    my_turtle.forward(size / 2)
    my_turtle.pendown()

    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    my_turtle.backward(size)

    restore_turtle_state(my_turtle)


def draw_u(my_turtle, size):
    save_turtle_state(my_turtle)

    radius = size / 2
    gap_length = size - radius

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.right(90)
    my_turtle.forward(gap_length)
    my_turtle.circle(radius, 180)
    my_turtle.forward(gap_length)

    restore_turtle_state(my_turtle)


def draw_v(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle = math.degrees(math.atan2(- size, size / 2))
    angle2 = math.degrees(math.atan2(size, size / 2, ))
    angled_length = math.sqrt((size / 2) ** 2 + (size) ** 2)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.setheading(angle + starting_angle)
    my_turtle.forward(angled_length)
    my_turtle.setheading(angle2 + starting_angle)
    my_turtle.forward(angled_length)

    restore_turtle_state(my_turtle)


def draw_w(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle1 = math.degrees(math.atan2(size, size / 2))
    angle2 = math.degrees(math.atan2(-size, size / 2))
    angled_length = math.sqrt((size / 3) ** 2 + size ** 2)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.setheading(starting_angle + 270)
    my_turtle.pendown()

    my_turtle.forward(size)
    my_turtle.setheading(starting_angle + angle1)
    my_turtle.forward(angled_length)
    my_turtle.setheading(starting_angle + angle2)
    my_turtle.forward(angled_length)
    my_turtle.setheading(starting_angle + 90)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


def draw_x(my_turtle, size):
    save_turtle_state(my_turtle)

    angled_length = math.sqrt(2 * size ** 2)

    my_turtle.left(45)
    my_turtle.forward(angled_length)

    my_turtle.penup()
    my_turtle.right(45)
    my_turtle.backward(size)
    my_turtle.right(45)
    my_turtle.pendown()

    my_turtle.forward(angled_length)

    restore_turtle_state(my_turtle)


def draw_y(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle1 = math.degrees(math.atan2(-size / 3, size / 2))
    angle2 = math.degrees(math.atan2(size / 3, size / 2))
    angled_length = math.sqrt((size / 3) ** 2 + (size / 2) ** 2)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.setheading(angle1 + starting_angle)
    my_turtle.forward(angled_length)
    my_turtle.setheading(angle2 + starting_angle)
    my_turtle.forward(angled_length)
    my_turtle.backward(angled_length)
    my_turtle.setheading(270 + starting_angle)
    my_turtle.forward(size * 2 / 3)

    restore_turtle_state(my_turtle)


def draw_z(my_turtle, size):
    save_turtle_state(my_turtle)

    starting_angle = my_turtle.heading()
    angle1 = math.degrees(math.atan2(- size, -size))
    angle2 = math.degrees(math.atan2(0 , size))
    angled_length = math.sqrt(size ** 2 + (size) ** 2)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()

    my_turtle.forward(size)
    my_turtle.setheading(angle1 + starting_angle)
    my_turtle.forward(angled_length)
    my_turtle.setheading(angle2 + starting_angle)
    my_turtle.forward(size)

    restore_turtle_state(my_turtle)


# *************************************************************************************************
# Other drawing functions
# *************************************************************************************************
def draw_square(my_turtle, size):
    """
    Causes a turtle to draw a square with side length size

    Args:
        my_turtle: the turtle which is to do the drawing
        size: the length of each side of the square

    Returns:
        None
    """
    for _ in range(4):
        my_turtle.forward(size)
        my_turtle.left(90)


def draw_letter(my_turtle, letter, size):
    """
    Draws the given letter.

    Args:
        my_turtle: the turtle to be used for drawing
        letter: the letter to be drawn
        size: the size of the square to draw the letter in

    Returns:
        None
    """
    eval(f"draw_{letter}(my_turtle, {size})")


def draw_string(my_turtle, s, size, color="black", gap_percentage=0.1):
    """
    Causes a turtle to draw a string of letters

    Args:
        my_turtle: the turtle which is to do the drawing
        s: the string of letters to be drawn
        size: the size of each letter

    Returns:
        None
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    my_turtle.pencolor(color)

    s = s.lower()

    for letter in s:

        if letter == " ":
            my_turtle.penup()
            my_turtle.forward(size)
            my_turtle.pendown()

        elif letter in alphabet:
            draw_letter(my_turtle, letter, size)
            my_turtle.penup()
            my_turtle.forward(size)
            my_turtle.pendown()

        else:
            draw_square(my_turtle, size)

        my_turtle.penup()
        my_turtle.forward(size * gap_percentage)
        my_turtle.pendown()


def compute_size(text, width):
    """returns the size needed for draw_string(my_turtle, text, size) to fit exactly in the given
    width"""

    total_size = len(text) * width

    return total_size


def setup_window(width=800, height=600, bg_color="white", pen_color="black"):

    new_turtle = turtle.Turtle()
    new_screen = turtle.Screen()

    new_screen.setup(width, height)

    new_screen.bgcolor(bg_color)
    new_turtle.pencolor(pen_color)

    return new_screen, new_turtle


def random_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    return r, g, b
