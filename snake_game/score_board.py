from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\Python\snake_game\data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0,270)
        self.hideturtle()
        self.color("white")
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.write(f"Score {self.score} High Score {self.high_score}", align=ALIGNMENT,
                   font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("D:\Python\snake_game\data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
    
    def increase_score(self):
        self.score += 1
        self.update_score_board()
        
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over ", align=ALIGNMENT,font=FONT)
        