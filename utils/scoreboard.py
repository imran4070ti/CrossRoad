from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self, position = (0, 250)):
        super().__init__()
        self.score = 0
        self.level = 1
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.color('black')

    def update_score(self):
        self.score += 1

    def update_level(self):
        self.level += 1

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def display(self):
        self.write(f'Level: {self.level}\tScore: {self.score}', align='center', font=FONT)

    def refresh_scoreboard(self):
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 50, 'normal'))
