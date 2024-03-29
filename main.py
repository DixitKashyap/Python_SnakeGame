from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# Setting Up The Compose
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turing off tracer to remove turtle drawing animation
screen.tracer(0)

# Creating Snake Object
snake = Snake()
# Creating Food Object
food = Food()
# Creating A Score Board
score = ScoreBoard()
# Accessing Key for moving snake object
screen.listen()

# Mapping KeyBoard
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
      
    snake.move()
    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect Collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor()<-280:
       score.reset()
       snake.reset()

    #Detect Collison with the tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()




screen.exitonclick()