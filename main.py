import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()


def check_hit():
    global game_is_on
    for brisk in car.brisks:
        x = brisk.xcor()
        y = brisk.ycor()
        if x - 30 < player.xcor() < x + 35 and y - 22 < player.ycor() < y + 15:
            game_is_on = False
            scoreboard.fail()
        else:
            pass


def check_success():
    global game_is_on
    if player.if_success():
        scoreboard.add_level()
        car.add_level()
        time.sleep(1)
    if scoreboard.level == 6:
        game_is_on = False
        scoreboard.win()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_brisks()
    screen.listen()
    screen.onkey(fun=player.move_up, key="Up")
    screen.onkey(fun=player.move_down, key="Down")
    check_hit()
    check_success()

screen.exitonclick()