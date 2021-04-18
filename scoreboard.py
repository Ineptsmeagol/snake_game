from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-30, 270)
        self.show_scoreboard()


    def show_scoreboard(self):
        """Method to display the scoreboard at the top of the screen"""
        self.clear()
        new_score = f"Score: {self.score}"
        self.write(new_score, font=("courier", 12, "bold"))

    def update_score(self):
        """Update the Score by 1 and refresh"""
        self.score += 1
        self.show_scoreboard()

    def game_over(self):
        new_score = "GAME OVER"
        self.goto(-30, 0)
        self.write(new_score, font=("courier", 12, "bold"))