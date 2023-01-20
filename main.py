import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("cross road")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    if car_manager.all_cars[-1].xcor() <= 270:
        car_manager.ccar()
    time.sleep(0.1)
    car_manager.cars_move()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 290:
        player.start()
        scoreboard.levelUp(1)
        car_manager.increse()

screen.exitonclick()
