from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 4


class CarManager:
    def __init__(self):
        self.brisks = []
        self.brisk_number = 25
        self.place_brisks()
        self.speed = 5

    def place_brisks(self):
        for num in range(self.brisk_number):
            brisk = Turtle()
            brisk.shape("square")
            brisk.shapesize(stretch_wid=1, stretch_len=2.5)
            brisk.penup()
            brisk.color(random.choice(COLORS))
            brisk.setposition(x=random.randint(-325, 325), y=random.randint(-250, 270))
            self.brisks.append(brisk)

    def move_brisks(self):
        for brisk in self.brisks:
            brisk.backward(self.speed)
        self.reset_brisks()

    def reset_brisks(self):
        for brisk in self.brisks:
            if brisk.xcor() < -325:
                brisk.color(random.choice(COLORS))
                brisk.setposition(x=325, y=random.randint(-250, 270))

    def add_level(self):
        self.brisk_number -= 3
        for brisk in self.brisks:
            brisk.hideturtle()
        self.brisks = []
        self.place_brisks()
        self.speed += MOVE_INCREMENT

