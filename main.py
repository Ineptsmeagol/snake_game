from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("gray")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "e")  # key up
screen.onkey(my_snake.down, "d")  # key down
screen.onkey(my_snake.right, "f")  # key right
screen.onkey(my_snake.left, "s")  # key left
my_snake.snake_forward()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.20)
    my_snake.snake_forward()

    # Ate some food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_score.update_score()
        my_snake.extend()

    # Collided with the wall
    if my_snake.head.xcor() > 285 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 285 or my_snake.head.ycor() < -285:
        my_score.reset()
        my_snake.reset()

    # Detect collision with tail
    for seg in my_snake.segments[1:]:
        if my_snake.head.distance(seg) < 10:
            my_score.reset()
            my_snake.reset


screen.exitonclick()
