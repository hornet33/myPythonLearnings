import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 280
END_X = -280


def add_car():
    new_car = Turtle()
    new_car.shape("square")
    new_car.penup()
    new_car.shapesize(stretch_len=2, stretch_wid=1)
    new_car.color(random.choice(COLORS))
    new_x = random.randint(END_X, START_X)
    new_y = random.randint(-250, 260)
    new_car.goto(new_x, new_y)
    return new_car


class CarManager:
    def __init__(self):
        self.car_list = []
        for _ in range(10):
            self.car_list.append(add_car())

    def move(self):
        for car in self.car_list:
            if car.xcor() < END_X - 40:
                car.goto(START_X + 40, car.ycor())
            else:
                car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def level_up(self):
        last_level_num_cars = len(self.car_list)

        # Every level up should place cars differently from last level
        for car in self.car_list:
            car.hideturtle()
        self.car_list.clear()

        # Every level up increases number of cars by 2
        for _ in range(last_level_num_cars + 2):
            self.car_list.append(add_car())

        # Every level up increases speed of cars
        global MOVE_INCREMENT
        MOVE_INCREMENT += 1
        print(f"Current cars: {len(self.car_list)} | Current Move Increment: {MOVE_INCREMENT}")

    def has_collided_with_player(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:  # Collided - 20 since each car is 40 wide, hence half of it
                return True
        return False
