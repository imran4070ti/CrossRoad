from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto((320, random.randint(-250, 250)))
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.current_speed)

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT

