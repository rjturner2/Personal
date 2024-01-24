import turtle
import random

# Set up the screen
turtle.bgcolor("black")
turtle.title("Particle Simulation")
turtle.hideturtle()
turtle.tracer(0)

# Function to create a particle
def create_particle():
    particle = turtle.Turtle()
    particle.shape("circle")
    particle.color("white")
    particle.penup()
    particle.speed(0)
    particle.goto(random.uniform(-290, 290), random.uniform(-290, 290))
    particle.dx = random.uniform(-2, 2)
    particle.dy = random.uniform(-2, 2)
    return particle

# Function to move a particle
def move_particle(particle):
    particle.dy -= gravity  # Apply gravity
    x = particle.xcor()
    y = particle.ycor()
    x += particle.dx
    y += particle.dy

    # Bounce off the walls
    if x > 290 or x < -290:
        particle.dx *= -1
    if y > 290:
        particle.dy *= -1  # Bounce back up
        y = 290
    if y < -290:
        particle.dy *= -1
        y = -290

    particle.goto(x, y)

gravity = 0.1  # Adjust the strength of gravity
num_particles = 20
particles = [create_particle() for _ in range(num_particles)]

# Main simulation loop
while True:
    for particle in particles:
        move_particle(particle)

    turtle.update()
