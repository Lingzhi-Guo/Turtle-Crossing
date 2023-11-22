from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.setposition(x=-280, y=250)
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.setposition(x=-280, y=250)
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def fail(self):
        self.hideturtle()
        self.home()
        self.write(arg="You Lose!", move=False, align="center", font=("Courier", 35, "normal"))

    def win(self):
        self.hideturtle()
        self.home()
        self.color("red")
        self.write(arg="Congratulations! You win!", move=False, align="center", font=("Courier", 33, "bold"))
