from turtle import Turtle
FONT = ("Courier", 15, "normal")
FONT2 = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-245, 270)
        self.color("black")
        self.hideturtle()
        self.levelUp(0)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT2)

    def levelUp(self, num):
        if num == 1:
            self.level +=1
        self.clear()

        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)
