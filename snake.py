import turtle
import random

# Screen Configuration
WIDTH, HEIGHT = 500, 500
FOOD_SIZE = 10
DELAY = 100  # Milliseconds between updates

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def show_menu():
    screen.clear()
    screen.bgcolor("pink")
    screen.title("Snake Game by Danilo")
    
    menu_turtle = turtle.Turtle()
    menu_turtle.hideturtle()
    menu_turtle.penup()
    menu_turtle.goto(0, 100)
    menu_turtle.write("SNAKE GAME BY DANILO", align="center", font=("Arial", 24, "bold"))
    menu_turtle.goto(0, 50)
    menu_turtle.write("Press SPACE to Play", align="center", font=("Arial", 16, "normal"))
    menu_turtle.goto(0, 0)
    menu_turtle.write("Press Q to Quit", align="center", font=("Arial", 16, "normal"))
    
    screen.listen()
    screen.onkey(start_game, "space")
    screen.onkey(exit_game, "q")

def start_game():
    screen.clear()
    screen.bgcolor("pink")
    screen.tracer(0)
    setup_game()
    reset_game()

def exit_game():
    turtle.bye()

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
    
    if new_head in snake[:-1]:  # Collision with itself
        show_menu()
        return
    
    snake.append(new_head)
    
    if not check_food_collision():
        snake.pop(0)
    
    # Border crossing management
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

def setup_game():
    global pen, food
    
    pen = turtle.Turtle("square")
    pen.color('green')
    pen.penup()
    
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.shapesize(FOOD_SIZE / 20)
    food.penup()
    
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_right, "Right")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(exit_game, "q")

# Game window settings
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
show_menu()
turtle.done()
