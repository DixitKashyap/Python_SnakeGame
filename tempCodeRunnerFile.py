      
    snake.move()
    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()