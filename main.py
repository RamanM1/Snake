import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("       Created by: Raman Movlodi \nUse the following keys: 'W', 'S', 'A', 'D'", align="center", font=("Courier", 14, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Levels
levels = {
    1: {"speed": 0.1, "score_to_next_level": 80},
    2: {"speed": 0.04, "score_to_next_level": 250},
    3: {"speed": 0.02, "score_to_next_level": 500},
    # Add more levels as needed
}

current_level = 1

# Function to increase the level
def increase_level():
    global current_level, delay
    current_level += 1
    if current_level in levels:
        level_data = levels[current_level]
        delay = level_data["speed"]
        score_to_next_level = level_data["score_to_next_level"]
        pen.clear()
        pen.write(f"Level: {current_level}  Score: {score}  High Score: {high_score}", align="center",
                font=("Courier", 24, "normal"))
        if current_level == 3:  # Check if current level is 3
            head.color("red")  # Change the color of the snake's head to red
            for segment in segments:
                segment.color("red")
            delay = 0.05  # Update the delay to a faster speed
        


    else:
        # Game completed all levels
        pen.clear()
        pen.write("Congratulations! You completed all levels.", align="center",
                font=("Courier", 24, "normal"))
        
# Main game loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
        
        # Reset the current level
        current_level = 1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))
        

    # Check for a collision with the food
    if head.distance(food) < 20:
        
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.
        
        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                font=("Courier", 24, "normal"))

        # Check if the score reaches the next level threshold
        if score >= levels[current_level]["score_to_next_level"]:
            increase_level()


# Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))

    time.sleep(delay)
