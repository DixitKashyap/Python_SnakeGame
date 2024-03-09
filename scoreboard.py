from turtle import Turtle


ALIGMENT = "center"
FONT = ("Arial",24,"normal")
GAME_OVER_TEXT = "Game Over"
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=260)
        self.update_scoreboard()    

    def update_scoreboard(self):
          self.write(f"Score : {self.score}",align=ALIGMENT,font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
         self.clear()
         self.goto(0,0)
         self.write(f"Score : {GAME_OVER_TEXT}",align=ALIGMENT,font=FONT)
     
    