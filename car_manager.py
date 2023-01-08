import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 7


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.setheading(180)
        self.shapesize(1, 3)
        self.penup()
        self.color(random.choice(COLORS))
        self.setpos(300, random.randint(-260, 260))
        self.move_speed = STARTING_MOVE_DISTANCE
        self.current_cars = [self]


    def level_up(self):
        self.move_speed += MOVE_INCREMENT

    def add_cars(self):
        for _ in range(random.randint(0,4)):
            self.current_cars.append(CarManager())

    def move(self,player):
        for car in self.current_cars:
            car.fd(self.move_speed)
            if car.distance(player) < 20:
                return False
            if car.xcor() < -300:
                self.remove_cars(car)
        return True

    def remove_cars(self, car):
        car.reset()
        car.ht()
        self.current_cars.remove(car)
