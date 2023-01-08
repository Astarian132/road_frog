import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
brave_turtle = Player()
score = Scoreboard()
screen.listen()
damn_cars = CarManager()
damn_cars.add_cars()
screen.onkeypress(brave_turtle.move_up, 'Up')

score.show_score()
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    game_is_on = damn_cars.move(brave_turtle)
    if brave_turtle.ycor() > 280:
        brave_turtle.reset_turtle()
        score.level_up()
        damn_cars.level_up()

    if random.randint(0, 100) > 88:
        damn_cars.add_cars()
    screen.update()

score.game_over()
print(len(damn_cars.current_cars))

screen.exitonclick()
