from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.ccar()

    def ccar(self):
        car = Turtle()
        car.color(choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(x=300, y=randint(-270, 280))
        self.all_cars.append(car)

    def cars_move(self):
        for car in range(len(self.all_cars)):
            new_x = self.all_cars[car].xcor() - STARTING_MOVE_DISTANCE
            self.all_cars[car].goto(new_x, self.all_cars[car].ycor())

    def increse(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

