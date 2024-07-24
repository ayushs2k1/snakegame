from turtle import Turtle
ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 17
FONT_TYPE = "normal"

   
class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.teleport(0,275)
        self.write(arg="score = 0",move=False,align=ALIGNMENT,font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
    
    def score_update(self,):
        self.score += 1
        self.clear()
        self.write(arg=f"score = {self.score}",move=False,align=ALIGNMENT,font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
    
    def game_over(self):
        
        self.home()
        self.write(arg=f"GAME OVER",move=False,align=ALIGNMENT,font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
      