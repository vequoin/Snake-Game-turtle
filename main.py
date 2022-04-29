import time
import turtle
from food import  Food
from snake import Snake
from  scoreboard import Scoreboard

src = turtle.Screen()
src.setup(width=600,height=600)
src.bgcolor("black")
src.title("My Snake Game")
src.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard(0)
score.scoring()


src.listen()
src.onkey(fun=snake.on_key_up, key="Up")
src.onkey(fun=snake.on_key_down,key="Down")
src.onkey(fun=snake.on_key_left, key="Left")
src.onkey(fun=snake.on_key_right,key="Right")

game_is_on = True
while game_is_on:
    src.update()
    time.sleep(.1)
    snake.move_snake()

    # detect collistions_with_food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.clear()
        score.scoring_refresh()

    # detect collisions with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    # detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


src.exitonclick()
