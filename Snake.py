"""
This is my version of the game Snake in python, created solely with the turtle module.
This will allow me to have my friends make AI for snake and pit them against each other.

Author: (Ryley Turner)
"""

import turtle
import random

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
FPS = 15

# We will store the Snake as a list and the length the snake should be as an integer
snake = [(GRID_DENSITY_WIDTH // 2 - 1, GRID_DENSITY_HEIGHT // 2 - 1)]
snake_length = 3
has_eaten = False

# We need to setup where the food will be
food_location = (random.randint(0, GRID_DENSITY_WIDTH), random.randint(0, GRID_DENSITY_HEIGHT))
print(food_location)

# Snake specific Boolean constants
HEADING = [False for _ in range(4)]
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
HEADING[UP] = True

sleep_time = int(round(1000 / FPS))
canvas, draw = turtle.Screen(), turtle.Turtle()

boundary_draw = turtle.Turtle()


def main():
    # We need to do some basic setup of our screen, including dimensions and turtle housekeeping items
    setup()

    # We'll draw the bounding boxes if we have that debug option enabled
    if DRAW_BOXES:
        debug_draw_boxes()

    # Now we'll setup our key bindings, which allow us to actually play the game
    setup_key_bindings()

    # We also need to call mainloop so that our events are handled correctly
    canvas.mainloop()


def get_indecies(x_pixel, y_pixel):
    # First we will grab our current width and height of the window, just incase the user has
    # resized the window
    width, height = canvas.window_width(), canvas.window_height()

    # Then we assign our indexes based on integer division of the remaining amount of pixels we have
    # after we account for the margins on either side of the screen
    x_index, y_index = (x_pixel + width / 2) // BOX_WIDTH, (y_pixel + height / 2) // BOX_HEIGHT

    # Then we convert those suckers to ints and send them on their way
    return int(x_index) - 1, int(y_index) - 1


def draw_box(fill):
    # first we start actually drawing the outline of the box we are on
    # draw.pendown()
    draw.fillcolor(fill)
    draw.begin_fill()

    # Then we draw the box!
    for _ in range(2):
        draw.forward(BOX_WIDTH)
        draw.left(90)
        draw.forward(BOX_HEIGHT)
        draw.left(90)

    draw.end_fill()

    # Last we need to pull the pen back up in case between calls of this function we move the
    # turtle all around our screen
    draw.penup()

def debug_draw_boxes():
    width, height = canvas.window_width(), canvas.window_height()
    draw.goto(-width / 2 + MARGIN, -height / 2 + MARGIN)

    for i in range(GRID_DENSITY_HEIGHT):
        for _ in range(GRID_DENSITY_WIDTH):
            draw.setheading(0)
            draw_box()
            draw.forward(BOX_WIDTH)
        draw.goto(-width / 2 + MARGIN, -height / 2 + BOX_HEIGHT * (i + 1) + MARGIN)


def update_box(x_index, y_index, fill="white"):
    half_width, half_height = canvas.window_width() / 2, canvas.window_height() / 2
    x_pixel, y_pixel = x_index * BOX_WIDTH + MARGIN - half_width, y_index * BOX_HEIGHT + MARGIN - half_height

    draw.penup()

    draw.goto(x_pixel, y_pixel)

    draw_box(fill)


def print_coords(x, y):
    print(get_indecies(x, y), x, y)


def heading_up():
    global HEADING

    if not HEADING[DOWN]:
        HEADING[RIGHT] = False
        HEADING[DOWN] = False
        HEADING[LEFT] = False
        HEADING[UP] = True


def heading_left():
    global HEADING

    if not HEADING[RIGHT]:
        HEADING[RIGHT] = False
        HEADING[DOWN] = False
        HEADING[LEFT] = True
        HEADING[UP] = False


def heading_down():
    global HEADING

    if not HEADING[UP]:
        HEADING[RIGHT] = False
        HEADING[DOWN] = True
        HEADING[LEFT] = False
        HEADING[UP] = False


def heading_right():
    global HEADING

    if not HEADING[LEFT]:
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
    draw.hideturtle()

    boundary_draw.penup()
    boundary_draw.goto(-RESOLUTION_X / 2 + MARGIN, -RESOLUTION_Y / 2 + MARGIN)
    boundary_draw.pendown()
    boundary_draw.pencolor("white")
    boundary_draw.hideturtle()
    for _ in range(2):
        boundary_draw.forward(RESOLUTION_X - MARGIN * 2)
        boundary_draw.left(90)
        boundary_draw.forward(RESOLUTION_Y - MARGIN * 2)
        boundary_draw.left(90)


def setup_key_bindings():
    canvas.onkeypress(heading_up, "Up")
    canvas.onkeypress(heading_left, "Left")
    canvas.onkeypress(heading_down, "Down")
    canvas.onkeypress(heading_right, "Right")
    canvas.onkeypress(heading_up, "w")
    canvas.onkeypress(heading_left, "a")
    canvas.onkeypress(heading_down, "s")
    canvas.onkeypress(heading_right, "d")

    canvas.ontimer(animate, sleep_time)
    canvas.listen()

    # This is just a debug option I setup so that I could see exactly where the bounding box of each
    # in-game "pixel" was vs. where I thought it was
    if PRINT_INDEXES:
        canvas.onclick(print_coords)


def animate():
    # first we grab our global variables that we want to use and initialize a temporary snake to store the updated
    # locations of the next frame of the snake animation
    global snake
    global snake_length
    global game_running
    global has_eaten
    global food_location
    new_snake = []

    # I want to look at if the snake's head is occupying the same position as the food pretty
    # early on.
    if snake[0] == food_location:
        has_eaten = True
        food_location = (random.randint(0, GRID_DENSITY_WIDTH), random.randint(0, GRID_DENSITY_HEIGHT))

        # Just in case the food spawns inside of the snake, we want to reroll the food location until it isn't
        # Which gets more and more likely as the snake continues to grow.
        while food_location in snake:
            food_location = (random.randint(0, GRID_DENSITY_WIDTH), random.randint(0, GRID_DENSITY_HEIGHT))

    # Now we look at what our heading is, and place the head of the snake one more in that direction
    if HEADING[LEFT] and snake[0][0] >= 0:
        new_snake.append((snake[0][0] - 1, snake[0][1]))

    elif HEADING[DOWN] and snake[0][1] >= 0:
        new_snake.append((snake[0][0], snake[0][1] - 1))

    elif HEADING[RIGHT] and snake[0][0] <= GRID_DENSITY_WIDTH:
        new_snake.append((snake[0][0] + 1, snake[0][1]))

    elif HEADING[UP] and snake[0][1] <= GRID_DENSITY_HEIGHT:
        new_snake.append((snake[0][0], snake[0][1] + 1))

    # This functions as our edge detection, since if we go outside of 0 or the horizontal or vertical
    # densities, we want to stop the game.
    else:
        game_running = False

    # Now we append all previous positions the snake occupied to the new/temporary snake
    for position in snake:
        new_snake.append(position)

    if new_snake[0] in snake:
        game_running = False

    # If our new snake is longer than it is supposed to be (Which should only ever be by one) we 
    # want to pop the tail of the snake off.
    if len(new_snake) > snake_length:
        new_snake.pop()

    # Now we set the global snake equal to the temporary snake that has moved by one in the direction
    # That the player wanted to move in
    snake = new_snake.copy()

    # We also want to update the total length of the snake if we have eaten
    if has_eaten:
        snake_length += 3
        has_eaten = False

    # UPDATE SCREEN
    # First we need to clear the screen
    draw.clear()

    for coordinate_pair in snake:
        update_box(coordinate_pair[0], coordinate_pair[1])

    update_box(food_location[0], food_location[1], fill="red")

    # Finally we want to queue up the next frame of animation so we can do it all again.
    if game_running:
        canvas.title(f"Snake Length: {len(snake)}")
        canvas.ontimer(animate, sleep_time)

    else:
        canvas.clear()
        canvas.bgcolor("white")
        canvas.title("GAME OVER")


if __name__ == "__main__":
    main()
