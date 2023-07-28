from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.display_score()
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    