import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TIME_SLEEP = 0.1

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
scoreboard.write_new_score()
cars = []

screen.listen()
screen.onkey(player.move_up, "Up")

pace = STARTING_MOVE_DISTANCE
hit_count = 0
# car_generation_for_loops = 0
game_is_on = True
while game_is_on:
    time.sleep(TIME_SLEEP)
    hit_count += 1
    # car_generation_for_loops += 1
    car_generation_rand = random.randint(1, 7)

    if car_generation_rand == 1:
        new_car = CarManager()
        cars.append(new_car)
        car_generation_for_loops = 0

    for car in cars:
        car.move_right(pace)

        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            # time.sleep(3)
            # screen.bye()

    if player.ycor() > 280:
        player.level_up()
        pace = pace + MOVE_INCREMENT
        scoreboard.change_score()

    screen.update()

screen.exitonclick()
