from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake Game/high_score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.display_score()
    
    def increase_score(self):
        self.score+=1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Snake Game/high_score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.display_score()
            
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    