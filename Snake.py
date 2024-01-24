"""
This is my version of the game Snake in python, created solely with the turtle module.
This will allow me to have my friends make AI for snake and pit them against each other.

Author: (Ryley Turner)
"""

import turtle

# Constant that determines if the game is currently running
game_running = True

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
FPS = 5

# We will store the Snake as a list and the length the snake should be as an integer
snake = [(GRID_DENSITY_WIDTH // 2 - 1, GRID_DENSITY_HEIGHT // 2 - 1)]
snake_length = 1

# Snake specific Boolean constants
HEADING = [False for _ in range(4)]
HAS_EATEN = False
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
    animate()

    canvas.mainloop()


def get_indecies(x_pixel, y_pixel):
    width, height = canvas.window_width(), canvas.window_height()
    x_index, y_index = (x_pixel + width / 2) // BOX_WIDTH, (y_pixel + height / 2) // BOX_HEIGHT

    return int(x_index), int(y_index)


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


def update_boxes():
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

    canvas.ontimer(animate, sleep_time)

    if PRINT_INDEXES:
        canvas.onclick(print_coords)


def animate():
    # first we grab our global variables that we want to use and initialize a temporary snake to store the updated
    # locations of the next frame of the snake animation
    global snake
    global snake_length
    global game_running
    new_snake = []

    # Now we look at what our heading is, and place the head of the snake one more in that direction
    if HEADING[LEFT] and snake[0][0] > 0:
        new_snake.append((snake[0][0] - 1, snake[0][1]))

    elif HEADING[DOWN] and snake[0][1] > 0:
        new_snake.append((snake[0][0], snake[0][1] - 1))

    elif HEADING[RIGHT] and snake[0][0] < GRID_DENSITY_WIDTH:
        new_snake.append((snake[0][0] + 1, snake[0][1]))

    elif HEADING[UP] and snake[0][1] < GRID_DENSITY_HEIGHT:
        new_snake.append((snake[0][0], snake[0][1] + 1))

    # This functions as our edge detection, since if we go outside of 0 or the horizontal or vertical
    # densities, we want to stop the game.
    else:
        game_running = False

    # Now we append all previous positions the snake occupied to the new/temporary snake
    for posiition in snake:
        new_snake.append(position)

    # We also want to update the total length of the snake if we have eaten
    if HAS_EATEN:
        snake_length += 1
        HAS_EATEN = False

    # UPDATE SCREEN
    

    # If our new snake is longer than it is supposed to be (Which should only ever be by one) we 
    # want to pop the tail of the snake off.
    if len(new_snake) > snake_length:
        new_snake.pop()

    # Now we set the global snake equal to the temporary snake that has moved by one in the direction
    # That the player wanted to move in
    snake = new_snake.copy()

    # Finally we want to queue up the next frame of animation so we can do it all again.
    if game_running:
        canvas.ontimer(animate, sleep_time)


if __name__ == "__main__":
    main()
