from turtle import Screen


from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
is_game_on = True
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game by Ian')

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10 :
            score.reset()
            snake.reset()

screen.exitonclick()
