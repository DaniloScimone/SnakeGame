# Snake by Danilo
# Usa le freccie direzionali per il movimento

import turtle
import random

# Configurazione dello schermo
WIDTH, HEIGHT = 500, 500
FOOD_SIZE = 10
DELAY = 100  # Millisecondi tra ogni aggiornamento

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset_game():
    global snake, direction, food_position
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    direction = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    update_game()

def update_game():
    global direction
    
    new_head = snake[-1].copy()
    new_head[0] += offsets[direction][0]
    new_head[1] += offsets[direction][1]
    
    if new_head in snake[:-1]:  # Collisione con se stesso
        reset_game()
        return
    
    snake.append(new_head)
    
    if not check_food_collision():
        snake.pop(0)
    
    # Gestione attraversamento bordi
    if new_head[0] > WIDTH / 2:
        new_head[0] -= WIDTH
    elif new_head[0] < -WIDTH / 2:
        new_head[0] += WIDTH
    elif new_head[1] > HEIGHT / 2:
        new_head[1] -= HEIGHT
    elif new_head[1] < -HEIGHT / 2:
        new_head[1] += HEIGHT
    
    pen.clearstamps()
    
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()
    
    screen.update()
    turtle.ontimer(update_game, DELAY)

def check_food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return x, y

def get_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5

def move_up():
    global direction
    if direction != "down":
        direction = "up"

def move_right():
    global direction
    if direction != "left":
        direction = "right"

def move_down():
    global direction
    if direction != "up":
        direction = "down"

def move_left():
    global direction
    if direction != "right":
        direction = "left"

# Impostazioni della finestra di gioco
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0)

pen = turtle.Turtle("square")
pen.color('green')
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Ascolto dei comandi da tastiera
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")

reset_game()
turtle.done()
