"""
This is my version of the game Snake in python, created solely with the turtle module.
This will allow me to have my friends make AI for snake and pit them against each other.

Author: (Ryley Turner)
"""

import turtle

# Debug Options
DRAW_BOXES = False
PRINT_INDEXES = False

# Turtle constants
RESOLUTION_X, RESOLUTION_Y = 1280, 720
GRID_DENSITY_WIDTH = 60
GRID_DENSITY_HEIGHT = 30
MARGIN = 20
BOX_WIDTH = (RESOLUTION_X - MARGIN * 2) / GRID_DENSITY_WIDTH
BOX_HEIGHT = (RESOLUTION_Y - MARGIN * 2) / GRID_DENSITY_HEIGHT
FPS = 60


# Snake specific Boolean constants
HEADING = [False for _ in range(4)]
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

sleep_time = 1000 / FPS
canvas, draw = turtle.Screen(), turtle.Turtle()


def main():
    setup()
    temporary_draw_boxes()
    setup_key_bindings()

    canvas.mainloop()


def get_indecies(x_pixel, y_pixel):
    width, height = canvas.window_width(), canvas.window_height()
    x_index, y_index = (x_pixel + width / 2) // BOX_WIDTH, (y_pixel + height / 2) // BOX_HEIGHT

    return int(x_index) - 1, int(y_index) - 1


def get_draw_pos():

    return get_indecies(draw.xcor(), draw.ycor())


def draw_box():
    if DRAW_BOXES:
        draw.pendown()

    for _ in range(2):
        draw.forward(BOX_WIDTH)
        draw.right(90)
        draw.forward(BOX_HEIGHT)
        draw.right(90)

    draw.penup()

def temporary_draw_boxes():
    width, height = canvas.window_width(), canvas.window_height()
    draw.goto(-width / 2 + MARGIN, height / 2 - MARGIN)

    for i in range(GRID_DENSITY_HEIGHT):
        for _ in range(GRID_DENSITY_WIDTH):
            draw.setheading(0)
            draw_box()
            draw.forward(BOX_WIDTH)
        draw.goto(-width / 2 + MARGIN, height / 2 - BOX_HEIGHT * (i + 1) - MARGIN)


def print_coords(x, y):
    print(get_indecies(x, y), x, y)


def heading_up():
    global HEADING

    HEADING[RIGHT] = False
    HEADING[DOWN] = False
    HEADING[LEFT] = False
    HEADING[UP] = True


def heading_left():
    global HEADING

    HEADING[RIGHT] = False
    HEADING[DOWN] = False
    HEADING[LEFT] = True
    HEADING[UP] = False


def heading_down():
    global HEADING

    HEADING[RIGHT] = False
    HEADING[DOWN] = True
    HEADING[LEFT] = False
    HEADING[UP] = False


def heading_right():
    global HEADING

    HEADING[RIGHT] = True
    HEADING[DOWN] = False
    HEADING[LEFT] = False
    HEADING[UP] = False


def setup():
    canvas.tracer(0)
    canvas.setup(RESOLUTION_X, RESOLUTION_Y)
    canvas.bgcolor("black")
    draw.pencolor("white")
    draw.penup()


def setup_key_bindings():
    canvas.onkeypress(heading_up, "Up")
    canvas.onkeypress(heading_left, "Left")
    canvas.onkeypress(heading_down, "Down")
    canvas.onkeypress(heading_right, "Right")
    canvas.onkeypress(heading_up, "W")
    canvas.onkeypress(heading_left, "A")
    canvas.onkeypress(heading_down, "S")
    canvas.onkeypress(heading_right, "D")

    if PRINT_INDEXES:
        canvas.onclick(print_coords)


if __name__ == "__main__":
    main()
