from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0) # Turning the animation off

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(fun=snake.up,key="Up")
screen.onkeypress(fun=snake.down,key="Down")
screen.onkeypress(fun=snake.left,key="Left")
screen.onkeypress(fun=snake.right,key="Right")
 

is_game_on = True
score = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_update()
        snake.extend()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or\
          snake.head.ycor() > 280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        is_game_on = False


screen.exitonclick()