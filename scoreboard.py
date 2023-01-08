import turtle


FONT = ("Courier", 24, "normal")
ALLIGNEMNT = "left"

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, 250)
        self.color('black')
        self.score = 1

    def level_up(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f'Level: {self.score}', False, ALLIGNEMNT, FONT)

    def game_over(self):
        gamover = turtle.Turtle()
        gamover.hideturtle()
        gamover.penup()
        gamover.setpos(0, 0)
        gamover.write('Game Over', False, ALLIGNEMNT, FONT)
